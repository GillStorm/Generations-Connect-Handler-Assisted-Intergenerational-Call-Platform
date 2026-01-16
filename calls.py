from fastapi import APIRouter, Request
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse, Gather
from ..models.schemas import CallRequest
from ..call_service import call_handler, call_student
from app import database
from datetime import datetime
import os

router = APIRouter(prefix="/calls", tags=["Calls"])

BASE_URL = os.getenv("BASE_URL")
conference_name = "elder_student_conference"

@router.post("/request")
def request_call(data: CallRequest):
    database.db.collection("call_requests").add({
        "handler_phone": data.handler_phone,
        "student_name": data.student_name,
        "elder_name": data.elder_name,
        "timestamp": datetime.utcnow()
    })
    call_handler(
        handler_phone=data.handler_phone,
        student_name=data.student_name,
        student_phone=data.student_phone,
        elder_name=data.elder_name
    )
    return {
        "status":"success",
        "message": "Call request sent to handler"
        }


@router.api_route("/handler-voice", methods=["GET", "POST"])
def handler_voice(student: str, student_phone: str, elder: str):
    response = VoiceResponse()
    gather = Gather(
        num_digits=1,
        action=f"{BASE_URL}/calls/handler-response?student={student}&student_phone={student_phone}",
        method="POST"
    )
    gather.say(
        f"A student named {student} wants to talk to {elder}. "
        "Press 1 to approve. Press 2 to reject."
    )
    response.append(gather)
    return Response(content=str(response), media_type="application/xml")


@router.post("/handler-response")
async def handler_response(request: Request):
    form = await request.form()
    digit = form.get("Digits")

    student_phone = request.query_params.get("student_phone")

    response = VoiceResponse()

    if digit == "1":
        response.say("Call approved. Connecting student.")
        call_student(
            student_phone=student_phone,
            conference_name=conference_name
        )
    else:
        response.say("Call rejected. Thank you.")

    return Response(content=str(response), media_type="application/xml")


@router.api_route("/student-voice", methods=["GET", "POST"])
def student_voice(conf: str):
    response = VoiceResponse()
    response.say("Connecting you now.")
    response.dial().conference(conf)
    return Response(content=str(response), media_type="application/xml")

    

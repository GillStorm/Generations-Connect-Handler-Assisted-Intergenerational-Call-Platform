from fastapi import APIRouter, Request
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse, Gather
from ..models.schemas import CallRequest
from ..call_service import call_handler, call_student

router = APIRouter(prefix="/calls", tags=["Calls"])

conference_name = "elder_student_conference"


@router.post("/request")
def request_call(data: CallRequest):
    call_handler(
        data.handler_phone,
        data.student_name,
        data.elder_name
    )
    return {"message": "Call request sent to handler"}


@router.get("/handler-voice")
def handler_voice(student: str, elder: str):
    response = VoiceResponse()
    gather = Gather(num_digits=1, action="/calls/handler-response")
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

    response = VoiceResponse()

    if digit == "1":
        response.say("Call approved. Connecting student.")
        call_student(
            student_phone=form.get("From"),
            conference_name=conference_name
        )
    else:
        response.say("Call rejected. Thank you.")

    return Response(content=str(response), media_type="application/xml")


@router.get("/student-voice")
def student_voice(conf: str):
    response = VoiceResponse()
    response.say("Connecting you now.")
    response.dial().conference(conf)
    return Response(content=str(response), media_type="application/xml")

from twilio.rest import Client
from dotenv import load_dotenv
from urllib.parse import quote
import os

load_dotenv()

client = Client(
    os.getenv("TWILIO_ACCOUNT_SID"),
    os.getenv("TWILIO_AUTH_TOKEN")
)

TWILIO_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
BASE_URL = os.getenv("BASE_URL")


def call_handler(handler_phone, student_name, student_phone, elder_name):
    return client.calls.create(
        to=handler_phone,
        from_=TWILIO_NUMBER,
        url=f"{BASE_URL}/calls/handler-voice?student={quote(student_name)}&student_phone={quote(student_phone)}&elder={quote(elder_name)}"
    )


def call_student(student_phone, conference_name):
    return client.calls.create(
        to=student_phone,
        from_=TWILIO_NUMBER,
        url=f"{BASE_URL}/calls/student-voice?conf={quote(conference_name)}"
    )

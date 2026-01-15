# 📞 Generations Connect – Handler-Assisted Intergenerational Call Platform

## 📌 Overview

**Generations Connect** is a backend system designed to enable **safe, consent-based phone conversations between students and elderly individuals** living in old age homes.

Many elderly individuals are unable to use smartphones or modern communication platforms due to physical, cognitive, or technological barriers. At the same time, students seek meaningful conversations with elders for learning, empathy, and emotional connection.

This project bridges that gap using a **handler-assisted phone call workflow**, ensuring **comfort, consent, and safety** for elderly participants.


## 🔄 Call Flow (Core Feature)

1. A **student initiates a call request** via an API
2. A **handler receives a phone call** asking for approval
3. The handler:

   * Presses **1** → Call approved
   * Presses **2** → Call rejected
4. If approved, the **student is connected to the elder**
5. If rejected, the call ends safely

✔ Ensures elder consent
✔ Prevents misuse
✔ No smartphone required for elders

---

## 🏗️ System Architecture

```
Student (API Request)
        |
        v
FastAPI Backend
        |
        v
Twilio Voice API
        |
        v
Handler Phone (Approval)
        |
        v
Student ↔ Elder Phone Call
```

* **FastAPI** handles API logic
* **Twilio** manages phone calls
* **ngrok** exposes local backend for webhooks
* **Firebase (Firestore)** used for data storage (users, logs)

---

## 🧩 Tech Stack

### Backend

* **Python 3.9**
* **FastAPI** – REST API framework
* **Uvicorn** – ASGI server

### Communication

* **Twilio Voice API** – Phone call automation
* **TwiML** – Call flow instructions

### Database

* **Firebase Admin SDK**
* **Cloud Firestore**

### Development Tools

* **Swagger UI** – API testing
* **ngrok** – Public webhook exposure
* **python-dotenv** – Environment variables

---

## 📁 Project Structure

```
generations-connect-backend/
│
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── database.py          # Firebase initialization
│   ├── call_service.py      # Twilio call logic
│   │
│   ├── models/
│   │   └── schemas.py       # Pydantic request schemas
│   │
│   ├── routes/
│   │   ├── users.py         # User-related APIs
│   │   ├── menu.py          # Conversation topics
│   │   ├── memories.py      # Memory storage APIs
│   │   └── calls.py         # Handler-based call flow
│
├── serviceAccountKey.json   # Firebase service account key
├── requirements.txt
├── .env                     # Environment variables
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/generations-connect-backend.git
cd generations-connect-backend
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_PHONE_NUMBER=+1XXXXXXXXXX
BASE_URL=https://your-ngrok-url.ngrok-free.app
```

⚠️ Never commit `.env` to GitHub.

---

### 5️⃣ Firebase Setup

* Download **Firebase Admin SDK JSON**
* Rename to `serviceAccountKey.json`
* Place it in the project root

---

### 6️⃣ Run the Backend

```bash
python -m uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### 7️⃣ Start ngrok

```bash
.\ngrok.exe http 8000
```

Copy the HTTPS URL and update `BASE_URL`.

---

## 🧪 Testing with Swagger

Open:

```
http://127.0.0.1:8000/docs
```

### Test Endpoint:

**POST `/calls/request`**

Example request body:

```json
{
  "student_name": "Ananya",
  "student_phone": "+91XXXXXXXXXX",
  "elder_name": "Mr Kumar",
  "handler_phone": "+91YYYYYYYYYY"
}
```

---

## ✅ Expected Outcome

* Handler receives approval call
* Press **1** → Student connects to elder
* Press **2** → Call ends safely

---

## 🔐 Safety & Ethics

* Elder consent ensured via handler
* No smartphone usage required for elders
* Trial account restrictions respected
* No personal data stored without permission

---

## 🎓 Academic Relevance

* Aligns with **Design Thinking methodology**
* Addresses **real-world social problem**
* Demonstrates **backend engineering + cloud + telephony**
* Suitable for:

  * Capstone projects
  * Design Thinking labs
  * AI/ML department evaluations

---

## 🚀 Future Enhancements

* Call duration limits
* Call logs & analytics dashboard
* Admin panel for handlers
* Frontend for students
* Multi-language voice prompts

---

## 🧠 Key Takeaway

> *Generations Connect demonstrates how technology can be designed around people — not the other way around.*

---

## 📜 License

This project is developed for **educational purposes**.



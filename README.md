# FastAPI IVR-Style Static Chatbot

## 📌 Overview
This project implements an **IVR-style static chatbot backend** using **FastAPI**.  
The chatbot behaves like a traditional IVR (Interactive Voice Response) system where users do not type free-text queries. Instead, they select a numbered option and receive a predefined response.

The application is designed as a **foundation for future AI/LLM integration**, where static responses can later be replaced with AI-generated responses without changing the API structure.

---
## 🎯 Objectives
- Build a menu-driven chatbot backend (IVR style)
- Manage session-based conversations
- Separate conversation flow logic from response generation
- Design a clean, modular, and scalable FastAPI application

---
## 🏗 Project Structure
```

fastapi-ivr-chatbot/
│
├── main.py        # FastAPI application and API routes
├── models.py      # Pydantic request and response models
├── data.py        # Static knowledge base (questions & answers)
├── requirements.txt
└── README.md

````
---

## ⚙️ Installation & Setup

### 1️⃣ Create Virtual Environment
```bash
python -m venv venv
````

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Application

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 🔌 API Endpoints

### 1️⃣ Start Chat Session

**Endpoint**

```
POST /start-chat
```

**Description**

* Creates a new chat session
* Returns a session ID and available question options

**Sample Response**

```json
{
  "session_id": "abc123",
  "options": [
    "1. Temple Timings",
    "2. Darshan Ticket Booking",
    "3. Accommodation Availability",
    "4. Speak to Support"
  ]
}
```

---

### 2️⃣ Select Question Option

**Endpoint**

```
POST /select-option
```

**Request Body**

```json
{
  "session_id": "abc123",
  "option_number": 2
}
```

**Sample Response**

```json
{
  "question": "Darshan Ticket Booking",
  "answer": "Darshan tickets can be booked online 90 days in advance through the official portal.",
  "status": "success"
}
```

---

## 🧠 Static Knowledge Base

All chatbot responses are stored in a static dictionary inside `data.py`.

```python
QUESTIONS = {
  1: {
    "question": "Temple Timings",
    "answer": "The temple is open from 3:00 AM to 11:00 PM."
  }
}
```

> **Note:** Answers are NOT hardcoded inside API functions.
> This allows easy replacement with AI/LLM-based responses in the future.

---

## 🧪 Error Handling

The application properly handles:

* Invalid session ID
* Invalid option number
* Missing or invalid request fields

**Example Error Response**

```json
{
  "detail": "Invalid option selected"
}
```

---

## 🔮 Future Enhancements

* Replace static responses with LLM-based responses
* Add conversation history per session
* Implement `/end-chat` endpoint
* Integrate persistent storage (Redis / Database)

---

## 🏁 Conclusion

This project demonstrates a clean and modular **chatbot backend architecture** using FastAPI.
It mimics IVR-style interaction and serves as a strong backend foundation for future AI-powered chatbot systems.

---

````

---

## ✅ What to do next

1. Save file as **README.md**
2. Run:
```bash
git add README.md
git commit -m "Add README documentation"
git push

from fastapi import FastAPI, HTTPException
import uuid

from models import (
    StartChatResponse,
    SelectOptionRequest,
    SelectOptionResponse
)
from data import QUESTIONS

app = FastAPI(title="IVR Style Static Chatbot")

# In-memory session storage
sessions = set()


@app.post("/start-chat", response_model=StartChatResponse)
def start_chat():
    session_id = str(uuid.uuid4())
    sessions.add(session_id)

    options = [
        f"{key}. {value['question']}"
        for key, value in QUESTIONS.items()
    ]

    return {
        "session_id": session_id,
        "options": options
    }


@app.post("/select-option", response_model=SelectOptionResponse)
def select_option(request: SelectOptionRequest):

    if request.session_id not in sessions:
        raise HTTPException(status_code=400, detail="Invalid session ID")

    if request.option_number not in QUESTIONS:
        raise HTTPException(status_code=400, detail="Invalid option selected")

    selected = QUESTIONS[request.option_number]

    return {
        "question": selected["question"],
        "answer": selected["answer"],
        "status": "success"
    }

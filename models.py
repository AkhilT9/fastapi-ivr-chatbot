from pydantic import BaseModel
#from typing import List

class StartChatResponse(BaseModel):
    session_id: str
    options: list[str]

class SelectOptionRequest(BaseModel):
    session_id: str
    option_number: int

class SelectOptionResponse(BaseModel):
    question: str
    answer: str
    status: str

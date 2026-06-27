from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    question: str
    subject: str = "general"

class MCQRequest(BaseModel):
    topic: str
    subject: str
    num_questions: int = 5
    difficulty: str = "medium"  # easy, medium, hard

class ExamRequest(BaseModel):
    topic: str
    subject: str
    num_mcqs: int = 10
    num_short: int = 5
    num_long: int = 3
    difficulty: str = "medium"
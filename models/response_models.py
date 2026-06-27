from pydantic import BaseModel
from typing import List

class MCQOption(BaseModel):
    option: str
    is_correct: bool

class MCQ(BaseModel):
    question: str
    options: List[str]
    correct_answer: str

class MCQResponse(BaseModel):
    topic: str
    subject: str
    mcqs: List[MCQ]

class ExamResponse(BaseModel):
    topic: str
    subject: str
    mcqs: List[MCQ]
    short_questions: List[str]
    long_questions: List[str]
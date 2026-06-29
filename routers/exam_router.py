from fastapi import APIRouter, HTTPException
from models.request_models import MCQRequest, ExamRequest
from models.response_models import MCQResponse, ExamResponse
from services.groq_service import generate_mcqs, generate_exam

router = APIRouter(
    prefix="/exam",
    tags=["Exam Generator"]
)


@router.post("/generate-mcqs", response_model=MCQResponse)
def generate_mcqs_endpoint(request: MCQRequest):
    """
    MCQs generate karta hai given topic ke liye.
    
    - **topic**: Jis topic pe MCQs chahiye (e.g. "Photosynthesis")
    - **subject**: Subject name (e.g. "Biology")
    - **num_questions**: Kitne MCQs chahiye (default: 5)
    - **difficulty**: easy / medium / hard (default: medium)
    """
    try:
        result = generate_mcqs(
            topic=request.topic,
            subject=request.subject,
            num_questions=request.num_questions,
            difficulty=request.difficulty
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"MCQ generation failed: {str(e)}"
        )


@router.post("/generate-exam", response_model=ExamResponse)
def generate_exam_endpoint(request: ExamRequest):
    """
    Complete exam paper generate karta hai.
    
    - **topic**: Exam topic (e.g. "Newton's Laws of Motion")
    - **subject**: Subject name (e.g. "Physics")
    - **num_mcqs**: MCQs count (default: 10)
    - **num_short**: Short questions count (default: 5)
    - **num_long**: Long questions count (default: 3)
    - **difficulty**: easy / medium / hard (default: medium)
    """
    try:
        result = generate_exam(
            topic=request.topic,
            subject=request.subject,
            num_mcqs=request.num_mcqs,
            num_short=request.num_short,
            num_long=request.num_long,
            difficulty=request.difficulty
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Exam generation failed: {str(e)}"
        )
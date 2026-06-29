import json
import re
from groq import Groq
from configs.settings import settings
from models.response_models import MCQ, MCQResponse, ExamResponse


# Groq client initialize
client = Groq(api_key=settings.GROQ_API_KEY)


def _call_groq(prompt: str, system_prompt: str) -> str:
    """Base function — Groq API call karta hai"""
    response = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=4096,
    )
    return response.choices[0].message.content


def _parse_json_response(raw: str) -> dict:
    """
    Groq ka response parse karta hai — 
    markdown code blocks bhi handle karta hai
    """
    # ```json ... ``` blocks remove karo
    cleaned = re.sub(r"```(?:json)?", "", raw).strip().rstrip("`").strip()
    return json.loads(cleaned)


def generate_mcqs(
    topic: str,
    subject: str,
    num_questions: int = 5,
    difficulty: str = "medium"
) -> MCQResponse:
    """
    MCQs generate karta hai given topic aur subject ke liye.
    Returns MCQResponse object.
    """

    system_prompt = """You are an expert teacher and exam paper creator.
Your job is to generate high-quality multiple choice questions (MCQs).
ALWAYS respond with valid JSON only — no extra text, no markdown explanation.
JSON format must be exactly as instructed."""

    user_prompt = f"""Generate {num_questions} MCQs for the following:

Topic: {topic}
Subject: {subject}  
Difficulty: {difficulty}

Return ONLY this JSON structure (no extra text):
{{
  "mcqs": [
    {{
      "question": "Question text here?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_answer": "Option A"
    }}
  ]
}}

Rules:
- Each MCQ must have exactly 4 options
- correct_answer must exactly match one of the options
- Questions should match {difficulty} difficulty level
- Make questions educationally relevant to {subject}
"""

    raw = _call_groq(user_prompt, system_prompt)
    data = _parse_json_response(raw)

    mcqs = [MCQ(**m) for m in data["mcqs"]]

    return MCQResponse(
        topic=topic,
        subject=subject,
        mcqs=mcqs
    )


def generate_exam(
    topic: str,
    subject: str,
    num_mcqs: int = 10,
    num_short: int = 5,
    num_long: int = 3,
    difficulty: str = "medium"
) -> ExamResponse:
    """
    Complete exam paper generate karta hai:
    - MCQs
    - Short questions
    - Long questions
    Returns ExamResponse object.
    """

    system_prompt = """You are an expert teacher and professional exam paper creator.
Your job is to generate complete, well-structured exam papers.
ALWAYS respond with valid JSON only — no extra text, no markdown explanation.
JSON format must be exactly as instructed."""

    user_prompt = f"""Generate a complete exam paper for the following:

Topic: {topic}
Subject: {subject}
Difficulty: {difficulty}
Number of MCQs: {num_mcqs}
Number of Short Questions: {num_short}
Number of Long Questions: {num_long}

Return ONLY this JSON structure (no extra text):
{{
  "mcqs": [
    {{
      "question": "MCQ question text?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_answer": "Option A"
    }}
  ],
  "short_questions": [
    "Short question 1?",
    "Short question 2?"
  ],
  "long_questions": [
    "Long/detailed question 1?",
    "Long/detailed question 2?"
  ]
}}

Rules:
- Each MCQ must have exactly 4 options
- correct_answer must exactly match one of the options
- Short questions: 2-3 lines answer expected
- Long questions: detailed essay/paragraph answer expected
- All questions relevant to topic: {topic}, subject: {subject}
- Difficulty level: {difficulty}
"""

    raw = _call_groq(user_prompt, system_prompt)
    data = _parse_json_response(raw)

    mcqs = [MCQ(**m) for m in data["mcqs"]]

    return ExamResponse(
        topic=topic,
        subject=subject,
        mcqs=mcqs,
        short_questions=data["short_questions"],
        long_questions=data["long_questions"]
    )
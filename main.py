from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from configs.settings import settings
from agent.graph import agent_graph

app = FastAPI(
    title=settings.APP_TITLE,
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ChatRequest(BaseModel):
    question: str
    subject: str = "general"

@app.get("/")
def root():
    return {"message": "AI Teacher Assistant is running!"}

@app.get("/health")
def health():
    return {"status": "ok", "model": settings.MODEL_NAME}

@app.post("/chat")
def chat(request: ChatRequest):
    result = agent_graph.invoke({
        "question": request.question,
        "subject": request.subject,
        "messages": [],
        "context": None,
        "answer": None
    })
    return {
        "question": request.question,
        "answer": result["answer"]
    }
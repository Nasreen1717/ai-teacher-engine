# AI Teacher Assistant - Progress Tracker

## 🎯 PROJECT PURPOSE
Teachers ke liye exam paper generator:
- Topic do → MCQs ready
- Short/Long questions generate karna
- Complete exam paper banana
- Document upload karke questions banana (ChromaDB)
- PDF export karna
- Streamlit frontend (teacher-friendly UI)

## ✅ COMPLETED (27 June 2026)
- uv project init ✅
- Dependencies install ✅
- Folder structure complete ✅
- .env setup (GROQ_API_KEY working) ✅
- Groq API test — llama-3.3-70b-versatile ✅
- configs/settings.py ✅
- agent/state.py ✅
- agent/graph.py (basic LangGraph flow) ✅
- main.py (FastAPI server running on port 8000) ✅
- /chat endpoint working ✅
- Swagger UI working at /docs ✅
- models/request_models.py ✅
- models/response_models.py ✅

## 📁 FILE STATUS
configs/settings.py ✅
agent/state.py ✅
agent/graph.py ✅ (basic — exam nodes pending)
main.py ✅
models/request_models.py ✅
models/response_models.py ✅
routers/document_router.py ❌ empty
routers/exam_router.py ❌ empty
services/chroma_service.py ❌ empty
services/groq_service.py ❌ empty
services/pdf_service.py ❌ empty
streamlit_app.py ❌ empty

## 🔄 CURRENT STATUS
- Basic FastAPI server running ✅
- Basic /chat endpoint working ✅
- MCQ/Exam models ready ✅
- Ab exam-specific features banana hai

## ⏭️ KAL KA PLAN (Step by Step)

### Step 1 — services/groq_service.py
MCQ generation logic likhna:
- generate_mcqs(topic, subject, num_questions, difficulty)
- generate_exam(topic, subject, num_mcqs, num_short, num_long)

### Step 2 — routers/exam_router.py
Exam endpoints banana:
- POST /generate-mcqs
- POST /generate-exam

### Step 3 — main.py update
exam_router include karna

### Step 4 — Test
Swagger UI se MCQs generate karke test karna

### Step 5 — services/chroma_service.py (agar time ho)
ChromaDB setup — document upload + search

## 🏗️ TECH STACK
- Backend: FastAPI
- AI Framework: LangGraph + LangChain
- LLM: Groq — llama-3.3-70b-versatile
- Vector DB: ChromaDB (pending)
- Embeddings: sentence-transformers (pending)
- Frontend: Streamlit (pending)
- Package Manager: uv
- Project Path: D:\code\ai-teacher-engine

## 🚀 HOW TO START SERVER
cd D:\code\ai-teacher-engine
uv run python -m uvicorn main:app --reload
Browser: http://127.0.0.1:8000/docs

## 🐛 KNOWN FIXES
- uvicorn direct nahi chalta → uv run python -m uvicorn use karo
- .env extra fields error → extra="ignore" in Settings fixed
# AI Teacher Assistant - Progress Tracker

## 🎯 PROJECT PURPOSE
Teachers ke liye AI-powered exam paper generator:
- **MAIN GOAL:** Teacher ek book/PDF upload kare → AI us book ko padhe → Usi book ke content se exam paper ready kare
- Topic manually deke bhi MCQs banana (basic feature)
- Short/Long questions generate karna
- Complete exam paper banana
- PDF export karna
- Streamlit frontend (teacher-friendly UI — koi coding nahi)

## 🏗️ TECH STACK
- **Backend:** FastAPI
- **AI Framework:** LangGraph + LangChain
- **LLM:** Groq — llama-3.3-70b-versatile
- **Vector DB:** ChromaDB (PDF content store karne ke liye)
- **Embeddings:** sentence-transformers
- **PDF Reading:** PyMuPDF (fitz) ya pdfplumber
- **Frontend:** Streamlit (teacher-friendly UI)
- **Package Manager:** uv
- **Project Path:** D:\code\ai-teacher-engine
- **GitHub:** github.com/Nasreen1717/ai-teacher-engine

## 🚀 HOW TO START SERVER
```
cd D:\code\ai-teacher-engine
uv run python -m uvicorn main:app --reload
Browser: http://127.0.0.1:8000/docs
```

---

## ✅ COMPLETED (29 June 2026)

### Infrastructure
- uv project init ✅
- Dependencies install ✅
- Folder structure complete ✅
- .env setup (GROQ_API_KEY working) ✅
- Groq API test — llama-3.3-70b-versatile ✅

### Core Files
- `configs/settings.py` ✅
- `agent/state.py` ✅
- `agent/graph.py` (basic LangGraph flow) ✅
- `main.py` (FastAPI server on port 8000) ✅
- `models/request_models.py` ✅
- `models/response_models.py` ✅

### Exam Generation (Topic-based)
- `services/groq_service.py` ✅
  - `generate_mcqs(topic, subject, num_questions, difficulty)` ✅
  - `generate_exam(topic, subject, num_mcqs, num_short, num_long)` ✅
- `routers/exam_router.py` ✅
  - `POST /exam/generate-mcqs` ✅ TESTED — 200 OK ✅
  - `POST /exam/generate-exam` ✅

### Testing
- Swagger UI `/docs` working ✅
- `/exam/generate-mcqs` tested — Photosynthesis/Biology MCQs perfectly generated ✅
- Groq API response accurate ✅

---

## 📁 FILE STATUS

```
configs/settings.py          ✅ Complete
agent/state.py               ✅ Complete
agent/graph.py               ✅ Basic (exam nodes pending)
main.py                      ✅ Complete (exam_router included)
models/request_models.py     ✅ Complete
models/response_models.py    ✅ Complete
routers/exam_router.py       ✅ Complete
routers/document_router.py   ❌ Empty
services/groq_service.py     ✅ Complete
services/chroma_service.py   ❌ Empty
services/pdf_service.py      ❌ Empty
streamlit_app.py             ❌ Empty
```

---

## ⏭️ REMAINING WORK — RAG PIPELINE (Book → Exam)

### 🎯 MAIN FEATURE: Teacher Book Upload → Exam Generate

**Flow:**
```
Teacher PDF upload kare
        ↓
PDF ke pages text mein convert hon
        ↓
Text chunks mein toot jaye (e.g. 500 words each)
        ↓
Chunks ChromaDB mein store hon (with embeddings)
        ↓
Teacher bole "Chapter 3 ka exam banao"
        ↓
ChromaDB se relevant chunks niklen
        ↓
Groq un chunks ko padhe
        ↓
Usi content se MCQs + Questions ready!
```

---

### Step 1 — services/chroma_service.py
**Kya karna hai:**
```python
# PDF text extract karna
extract_text_from_pdf(pdf_path) -> str

# Text ko chunks mein todna
chunk_text(text, chunk_size=500) -> List[str]

# ChromaDB mein store karna
store_document(chunks, doc_id) -> None

# Query karna — relevant chunks nikalna
search_similar(query, top_k=5) -> List[str]
```
**Dependencies needed:**
```
uv add chromadb sentence-transformers pdfplumber
```

---

### Step 2 — services/groq_service.py UPDATE
**Kya karna hai:**
- Naya function add karna:
```python
# Book context se MCQs banana
generate_mcqs_from_context(context, topic, num_questions, difficulty)

# Book context se complete exam banana  
generate_exam_from_context(context, topic, num_mcqs, num_short, num_long)
```
- Existing functions touch nahi karne (topic-based still work karega)

---

### Step 3 — models/request_models.py UPDATE
**Kya karna hai:**
```python
# Naya model add karna
class DocumentExamRequest(BaseModel):
    doc_id: str          # Konsi book se
    topic: str           # Konsa chapter/topic
    num_mcqs: int = 10
    num_short: int = 5
    num_long: int = 3
    difficulty: str = "medium"
```

---

### Step 4 — routers/document_router.py
**Kya karna hai:**
```python
POST /document/upload     # PDF upload → ChromaDB mein store
POST /document/generate-exam  # Book se exam generate
GET  /document/list       # Uploaded books list
```

---

### Step 5 — main.py UPDATE
```python
from routers.document_router import router as document_router
app.include_router(document_router)
```

---

### Step 6 — streamlit_app.py (Teacher UI)
**Teacher ka experience:**
```
1. Browser kholo → Streamlit app
2. "Upload Book" → PDF select karo
3. Topic/Chapter likho → "Photosynthesis" ya "Chapter 3"
4. Difficulty chuno → Easy/Medium/Hard
5. Questions count set karo
6. "Generate Exam" button dabao
7. Exam screen pe aa jata hai
8. "Download PDF" → Exam paper download!
```

**UI mein yeh hoga:**
- Sidebar: PDF upload + settings
- Main area: Generated exam display
- Download button: PDF export

---

### Step 7 — services/pdf_service.py
**Kya karna hai:**
```python
# Generated exam ko PDF mein export karna
export_exam_to_pdf(exam_data, filename) -> bytes
```
**Dependencies:**
```
uv add reportlab
```

---

## 🐛 KNOWN FIXES
- uvicorn direct nahi chalta → `uv run python -m uvicorn` use karo
- .env extra fields error → `extra="ignore"` in Settings
- Groq response mein markdown blocks aate hain → `_parse_json_response()` handle karta hai

---

## 📊 PROGRESS SUMMARY
```
Overall:     ████████░░░░░░░░░░░░  35% Complete
Backend:     ████████████░░░░░░░░  60% Complete  
RAG/ChromaDB:░░░░░░░░░░░░░░░░░░░░   0% Complete
Frontend:    ░░░░░░░░░░░░░░░░░░░░   0% Complete
PDF Export:  ░░░░░░░░░░░░░░░░░░░░   0% Complete
```

---

## 🔄 NEW CHAT MEIN KAISE START KAREN
1. Ye PROGRESS.md Claude ko do
2. Claude khud samjh jaega kya hua aur kya karna hai
3. Seedha Step 1 (chroma_service.py) se shuru karo
4. Pehle dependencies install karen:
   ```
   uv add chromadb sentence-transformers pdfplumber reportlab
   ```
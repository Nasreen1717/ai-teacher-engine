from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Groq LLM
    GROQ_API_KEY: str
    MODEL_NAME: str = "llama-3.3-70b-versatile"
    
    # ChromaDB
    CHROMA_DB_PATH: str = "./chroma_db"
    COLLECTION_NAME: str = "teacher_docs"
    
    # Embeddings
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    
    # App
    APP_TITLE: str = "AI Teacher Assistant"
    DEBUG: bool = False

    class Config:
        env_file = ".env"
        extra = "ignore"

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
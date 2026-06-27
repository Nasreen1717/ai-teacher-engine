from typing import TypedDict, List, Optional
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    # User ka question
    question: str
    
    # Chat history
    messages: List[BaseMessage]
    
    # ChromaDB se retrieved context
    context: Optional[str]
    
    # Final answer
    answer: Optional[str]
    
    # Subject (math, science, etc.)
    subject: Optional[str]
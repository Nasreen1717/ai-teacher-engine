from langgraph.graph import StateGraph, END
from agent.state import AgentState
from configs.settings import settings
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage

# LLM initialize
llm = ChatGroq(
    api_key=settings.GROQ_API_KEY,
    model=settings.MODEL_NAME
)

# Node 1 — question process karo
def process_question(state: AgentState) -> AgentState:
    question = state["question"]
    state["messages"] = [HumanMessage(content=question)]
    return state

# Node 2 — LLM se answer lo
def generate_answer(state: AgentState) -> AgentState:
    messages = state["messages"]
    response = llm.invoke(messages)
    state["answer"] = response.content
    state["messages"].append(AIMessage(content=response.content))
    return state

# Graph banana
def create_graph():
    graph = StateGraph(AgentState)
    
    graph.add_node("process_question", process_question)
    graph.add_node("generate_answer", generate_answer)
    
    graph.set_entry_point("process_question")
    graph.add_edge("process_question", "generate_answer")
    graph.add_edge("generate_answer", END)
    
    return graph.compile()

agent_graph = create_graph()
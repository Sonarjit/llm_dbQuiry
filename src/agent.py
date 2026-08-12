from langchain_groq import ChatGroq
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langgraph.prebuilt import create_react_agent
from src.config import GROQ_API_KEY
# from src.database import get_db_connection
from src.microsoft_sql_connection import get_db_connection

def create_sql_reasoning_agent():
    """Initializes the Groq LLM, database tools, and execution graph."""
    db = get_db_connection()

    llm = ChatGroq(
        model="llama-3.3-70b-versatile", 
        groq_api_key=GROQ_API_KEY,
        temperature=0  # CRITICAL: keep at 0 for deterministic SQL generation
    )

    # Wrap the database into tools the agent can use
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    tools = toolkit.get_tools()

    # Create the stateful agent
    return create_react_agent(model=llm, tools=tools)
import streamlit as st
from src.prompts import build_dynamic_prompt
from src.agent import create_sql_reasoning_agent

# ==========================================
# 1. PAGE SETUP & SIDEBAR (Interview Flex)
# ==========================================
st.set_page_config(page_title="AI SQL Analyst", page_icon="📊", layout="wide")

with st.sidebar:
    st.header("⚙️ Architecture Details")
    st.markdown("""
    **Tech Stack:**
    * **LLM:** Llama 3.3 70B (via Groq)
    * **Vector DB:** Chroma (Local)
    * **Embeddings:** HuggingFace MiniLM
    * **Framework:** LangGraph
    """)
    
    st.divider()
    st.subheader("Database Schema")
    st.code("""
    t_shirts (
        t_shirt_id, brand, color, 
        size, price, stock_quantity
    )
    discounts (
        discount_id, t_shirt_id, 
        pct_discount
    )
    """, language="sql")

# ==========================================
# 2. INITIALIZE AI STATE
# ==========================================
st.title("👕 Sonar Store: AI Data Analyst")
st.write("Ask natural language questions to query the MySQL database.")

# Cache the agent and prompt so they don't rebuild on every click
@st.cache_resource
def load_ai_engine():
    agent = create_sql_reasoning_agent()
    prompt_template = build_dynamic_prompt()
    return agent, prompt_template

agent, dynamic_prompt_template = load_ai_engine()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================================
# 3. CHAT INTERFACE & EXECUTION
# ==========================================
if user_question := st.chat_input("E.g., What is our total revenue for white Nike shirts?"):
    
    # Show user message instantly
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    # Generate AI Response
    with st.chat_message("assistant"):
        with st.spinner("Searching Vector DB for few-shots & writing SQL..."):
            
            # Trigger your dynamic few-shot logic
            system_instructions = dynamic_prompt_template.format(Question=user_question)
            
            # Execute the LangGraph Agent
            response = agent.invoke({
                "messages": [
                    ("system", system_instructions),
                    ("user", user_question)
                ]
            })  
            
            final_answer = response["messages"][-1].content
            st.markdown(final_answer)
            
            # Save to history
            st.session_state.messages.append({"role": "assistant", "content": final_answer})
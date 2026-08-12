# Sonar Store: AI Data Analyst 

An advanced **Hybrid Text-to-SQL Agent** that allows users to query a MySQL inventory database using natural language. 

Unlike standard single-shot text-to-SQL scripts, this project utilizes an **Exemplar RAG (Retrieval-Augmented Generation) layer** combined with a **Stateful LangGraph ReAct Agent** to guarantee high-accuracy, syntax-perfect database queries.

## Key Features

* **Dynamic Few-Shot RAG:** Uses Hugging Face local embeddings and a Chroma vector database to semantically match the user's question with the most relevant SQL examples before execution.
* **Self-Correcting Agentic Loop:** Powered by LangGraph and Groq (Llama-3.3-70b), the agent natively interacts with database tools to explore schemas and autonomously fix SQL syntax errors if a query fails.
* **Secure Read-Only Execution:** Enforces strict dialect guardrails and executes entirely through a read-only database user profile to prevent data mutation.
* **Interactive Chat UI:** Built with Streamlit, featuring real-time reasoning spinners, chat history, and architectural transparency.

---

## System Architecture

This application merges two distinct AI design patterns:

1. **The RAG Layer (Prompt Optimization):**
   * The user submits a natural language question.
   * The input is embedded locally using `sentence-transformers/all-MiniLM-L6-v2`.
   * A similarity search runs against an in-memory **Chroma DB** to retrieve the top 2 structurally similar SQL examples.
   * These examples are dynamically injected into a LangChain `FewShotPromptTemplate`.

2. **The Agent Layer (Execution):**
   * The optimized prompt is passed to a **LangGraph ReAct Agent**.
   * The agent utilizes the `SQLDatabaseToolkit` to query the live MySQL database.
   * The agent analyzes the returned data, formats a human-readable answer, and sends it to the Streamlit UI.

---

## Tech Stack

* **Large Language Model:** Llama 3.3 70B (via Groq API)
* **Framework:** LangChain & LangGraph
* **Vector Database:** Chroma (Local)
* **Embeddings:** Hugging Face (`all-MiniLM-L6-v2`)
* **Relational Database:** MySQL (PyMySQL)
* **Frontend UI:** Streamlit

## OS Requirement

Microsoft Windows 10 or 11

## Set up and Run

1. Download and install python:Python 3.12.3

2. Clone repository
```bash
git clone https://github.com/Sonarjit/llm_dbQuiry.git
```

3. Create a Virtual Environment (Python 3.12.3) and activate the environment
```bash
python -m venv vEnv
```

```bash
.\vEnv\Scripts\activate
```

4. Install the requiremtns
```bash
pip install -r requirements.txt
```

5. Set up database
Follow the steps provided in [SQL connection set up.md](SQL%20connection%20set%20up.md).

6. Setup .env
Create a file named as .env in the parent folder. Inside that file, fill these

GROQ_API_KEY = "your-api-key-here"(visit this to get api key https://console.groq.com/home)

DB_USER = "sa"

DB_PASSWORD = "your-db-password-here"

DB_NAME = "sonar_store"

DB_SERVER = ".\SQLEXPRESS"


7. Run
```bash
streamlit run app.py
```
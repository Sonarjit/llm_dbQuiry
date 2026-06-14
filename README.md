# 👕 Sonar Inventory: AI Data Analyst 

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

## 🛠️ Tech Stack

* **Large Language Model:** Llama 3.3 70B (via Groq API)
* **Framework:** LangChain & LangGraph
* **Vector Database:** Chroma (Local)
* **Embeddings:** Hugging Face (`all-MiniLM-L6-v2`)
* **Relational Database:** MySQL (PyMySQL)
* **Frontend UI:** Streamlit

---

## 📁 Project Structure

```text
atliq-ai-analyst/
│
├── .env                    # Environment variables (not tracked by git)
├── requirements.txt        # Python dependencies
├── app.py                  # Streamlit frontend entry point
│
└── src/
    ├── __init__.py
    ├── config.py           # Centralized environment configurations
    ├── database.py         # Secure MySQL connection logic
    ├── few_shots.py        # Library of highly curated Text-to-SQL examples
    ├── prompts.py          # Vector store initialization and dynamic prompt templating
    └── agent.py            # LangGraph agent setup and tool binding
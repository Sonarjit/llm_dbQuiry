import os
from dotenv import load_dotenv

# Load environment variables once
load_dotenv()

# Database Config
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "")

DB_SERVER = os.getenv("DB_SERVER", "localhost")  # For Microsoft SQL Server

# LLM Config
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
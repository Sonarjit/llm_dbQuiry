import urllib.parse
from langchain_community.utilities.sql_database import SQLDatabase
from src.config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

def get_db_connection() -> SQLDatabase:
    """Creates a secure, read-only connection to the MySQL database."""
    safe_password = urllib.parse.quote_plus(DB_PASSWORD)
    db_uri = f"mysql+pymysql://{DB_USER}:{safe_password}@{DB_HOST}/{DB_NAME}"
    
    return SQLDatabase.from_uri(db_uri, sample_rows_in_table_info=3)
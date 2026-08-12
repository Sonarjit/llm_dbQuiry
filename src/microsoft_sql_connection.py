import urllib.parse
from langchain_community.utilities.sql_database import SQLDatabase

from src.config import (
    DB_SERVER,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)

def get_db_connection() -> SQLDatabase:
    """
    Creates a connection to Microsoft SQL Server.
    """

    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={DB_SERVER};"
        f"DATABASE={DB_NAME};"
        f"UID={DB_USER};"
        f"PWD={DB_PASSWORD};"
        f"TrustServerCertificate=yes;"
    )

    params = urllib.parse.quote_plus(connection_string)

    db_uri = f"mssql+pyodbc:///?odbc_connect={params}"

    return SQLDatabase.from_uri(
        db_uri,
        sample_rows_in_table_info=3
    )
import os
from dotenv import load_dotenv
import pyodbc

load_dotenv()

def get_db_connection():
    DB_DRIVER = os.getenv('DB_DRIVER', '{ODBC Driver 18 for SQL Server}')
    DB_SERVER = os.getenv('DB_SERVER', '100.117.127.91,1433')
    DB_NAME = os.getenv('DB_NAME', 'ParticipARD_DB')
    DB_USER = os.getenv('DB_USER', 'amigo')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '123456')

    conn_str = (
        f"DRIVER={DB_DRIVER};"
        f"SERVER={DB_SERVER};"
        f"DATABASE={DB_NAME};"
        f"UID={DB_USER};"
        f"PWD={DB_PASSWORD};"
        "Encrypt=no;"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conn_str)
import pyodbc

def check_contributors():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM tblContribuidores")
        rows = cursor.fetchall()
        print(f"Total contributors: {len(rows)}")
        for row in rows:
            print(row)
        
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_contributors()

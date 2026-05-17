import os
from dotenv import load_dotenv
import pyodbc

load_dotenv()

def check_schema():
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
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    print("Columns in tblContribuidores:")
    cursor.execute("SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'tblContribuidores'")
    for row in cursor.fetchall():
        print(row)
        
    conn.close()

if __name__ == "__main__":
    check_schema()

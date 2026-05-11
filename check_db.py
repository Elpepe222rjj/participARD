import app
import pyodbc

def check_table():
    try:
        conn = app.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'tblContribuidores'")
        row = cursor.fetchone()
        if row:
            print("EXISTS")
            cursor.execute("SELECT TOP 1 * FROM tblContribuidores")
            columns = [column[0] for column in cursor.description]
            print(f"Columns: {columns}")
        else:
            print("NOT_FOUND")
        conn.close()
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == '__main__':
    check_table()

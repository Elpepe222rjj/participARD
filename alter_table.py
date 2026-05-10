from app import get_db_connection

try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("ALTER TABLE tblActividades ALTER COLUMN FechaCierre DATE NULL;")
    conn.commit()
    print('FechaCierre altered to allow NULL successfully.')
except Exception as e:
    print(f"Error: {e}")

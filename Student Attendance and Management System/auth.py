from database import get_connection

def authenticate_teacher(username, password):
    """Authenticate teacher login."""
    conn = get_connection()
    if conn is None:
        return False
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teachers WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result is not None

def add_default_teacher():
    """Add a default teacher if not exists."""
    conn = get_connection()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("INSERT IGNORE INTO teachers (username, password) VALUES (%s, %s)", ('admin', 'admin'))
    conn.commit()
    cursor.close()
    conn.close()

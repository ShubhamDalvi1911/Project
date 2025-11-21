import mysql
from database import get_connection

def register_student(name, roll_no, class_name):
    """Register a new student."""
    conn = get_connection()
    if conn is None:
        return False
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (name, roll_no, class) VALUES (%s, %s, %s)", (name, roll_no, class_name))
        conn.commit()
        return True
    except mysql.connector.Error:
        return False
    finally:
        cursor.close()
        conn.close()

def get_students():
    """Retrieve all students."""
    conn = get_connection()
    if conn is None:
        return []
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return students

import mysql
from database import get_connection
from datetime import date

def mark_attendance(student_id, status):
    """Mark attendance for a student on today's date."""
    conn = get_connection()
    if conn is None:
        return False
    cursor = conn.cursor()
    today = date.today()
    try:
        cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (%s, %s, %s)", (student_id, today, status))
        conn.commit()
        return True
    except mysql.connector.Error:
        return False
    finally:
        cursor.close()
        conn.close()

def calculate_attendance_percentage(student_id):
    """Calculate attendance percentage for a student."""
    conn = get_connection()
    if conn is None:
        return 0
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM attendance WHERE student_id = %s", (student_id,))
    total_days = cursor.fetchone()[0]
    if total_days == 0:
        return 0
    cursor.execute("SELECT COUNT(*) FROM attendance WHERE student_id = %s AND status = 'present'", (student_id,))
    present_days = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return (present_days / total_days) * 100

def get_attendance_records():
    """Retrieve all attendance records with student details."""
    conn = get_connection()
    if conn is None:
        return []
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT s.name, s.roll_no, s.class, a.date, a.status
        FROM attendance a
        JOIN students s ON a.student_id = s.id
        ORDER BY a.date DESC
    """)
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records

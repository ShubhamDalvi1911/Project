import mysql.connector
from config import DB_CONFIG

def get_connection():
    """Establish a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database():
    """Create the attendance_system database if it doesn't exist."""
    conn = mysql.connector.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password']
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS attendance_system")
    conn.commit()
    cursor.close()
    conn.close()

def create_tables():
    """Create necessary tables in the database."""
    conn = get_connection()
    if conn is None:
        return
    cursor = conn.cursor()

    # Create teachers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)

    # Create students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            roll_no VARCHAR(20) UNIQUE NOT NULL,
            class VARCHAR(50) NOT NULL
        )
    """)

    # Create attendance table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT NOT NULL,
            date DATE NOT NULL,
            status ENUM('present', 'absent') NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

def initialize_database():
    """Initialize the database and tables."""
    create_database()
    DB_CONFIG['database'] = 'attendance_system'  # Update config to include database
    create_tables()

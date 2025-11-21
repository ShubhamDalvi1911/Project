# Project
Student Attendance Management System (Python + MySQL + Tkinter)
A desktop application for managing student registration and daily attendance with a simple teacher login. Built with Python, Tkinter for the GUI, and MySQL as the database backend.

Key features
Teacher authentication with a default admin account.

Register students with name, roll number, and class.

Mark daily attendance as present/absent via a checklist UI.

View attendance records joined with student details in a tabular view.

Tech stack
Python 3.x, Tkinter (GUI)

MySQL, mysql-connector-python

Project structure
database.py

Creates database and tables, manages DB connections.

auth.py

Teacher authentication and default admin seeding.

student.py

Student registration and retrieval.

attendance.py

Mark attendance, compute attendance percentage, fetch attendance records.

gui.py

Tkinter application frames: login, main menu, register student, mark attendance, view records.

config.py

Centralized DB_CONFIG dictionary with connection parameters.

main.py

Entry point: initialize DB, seed default admin, launch GUI.

Note: If your current code is in a single file, consider refactoring into the above modules for maintainability; names here match the imports already present in the shared code.

Prerequisites
Python 3.9+ installed.

MySQL Server running locally or remotely.

A MySQL user with privileges to create databases and tables.

Installation
Clone the repository

git clone https://github.com/your-username/attendance-system.git

cd attendance-system

Create a virtual environment

python -m venv .venv

On Windows: .venv\Scripts\activate

On macOS/Linux: source .venv/bin/activate

Install dependencies

pip install -r requirements.txt

Sample requirements.txt:

mysql-connector-python

python-dotenv (optional, if using .env)

Configuration
Create config.py at the project root with your MySQL credentials:

DB_CONFIG = {
'host': 'localhost',
'user': 'root',
'password': 'your_password',
'database': 'attendance_system'
}

Security tips:

Do not commit real credentials to GitHub; use environment variables or .env with python-dotenv for production.

Replace plaintext admin password with a hashed password (e.g., bcrypt) and parameterized queries (already used).

Optional .env approach:

DB_HOST=localhost

DB_USER=root

DB_PASSWORD=your_password

DB_NAME=attendance_system

Then load into config.py:

from os import getenv

from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
'host': getenv('DB_HOST', 'localhost'),
'user': getenv('DB_USER', 'root'),
'password': getenv('DB_PASSWORD', ''),
'database': getenv('DB_NAME', 'attendance_system')
}

Database schema
teachers

id INT PK AUTO_INCREMENT

username VARCHAR(50) UNIQUE NOT NULL

password VARCHAR(255) NOT NULL

students

id INT PK AUTO_INCREMENT

name VARCHAR(100) NOT NULL

roll_no VARCHAR(20) UNIQUE NOT NULL

class VARCHAR(50) NOT NULL

attendance

id INT PK AUTO_INCREMENT

student_id INT NOT NULL FK -> students(id)

date DATE NOT NULL

status ENUM('present', 'absent') NOT NULL

Constraints/notes:

Foreign key from attendance.student_id to students.id.

Consider a unique constraint on (student_id, date) to prevent duplicate daily entries.

How it works
Initialization

On first run, the app creates the database (attendance_system) and required tables.

Seeds a default teacher: username admin, password admin. Change immediately.

Authentication

Login screen checks credentials in teachers table.

Student management

Register students with Name, Roll No, Class; Roll No is unique.

Attendance

Mark today’s attendance as present/absent per student using checkboxes.

View attendance records with student name, roll, class, date, and status.

Running the app
python main.py

Default credentials

Username: admin

Password: admin

Change the admin password after first login by updating the record in the teachers table or adding a UI for password change.

Screens and flows
Login: Enter teacher username and password.

Main menu: Register Student, Mark Attendance, View Attendance Records, Logout.

Register Student: Inputs for Name, Roll No, Class, then Save.

Mark Attendance: List of students with checkboxes defaulting to absent; submit to save today’s attendance.

View Records: Table view (Treeview) of historical attendance joined with student details.

Common issues and fixes
MySQL connection error: Ensure MySQL service is running and credentials in config.py are correct.

Import errors: Verify files match module names used in imports (database.py, auth.py, student.py, attendance.py, gui.py, main.py).

Duplicate roll number: Roll No must be unique; choose a new roll number or update the existing student.

Duplicate attendance for a day: Add a unique index on (student_id, date) to prevent duplicates.

SQL to enforce unique daily attendance:

ALTER TABLE attendance ADD UNIQUE KEY uniq_student_date (student_id, date);

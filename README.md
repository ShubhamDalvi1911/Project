#📘 Student Attendance & Management System (Python + MySQL)
A desktop-based GUI application built using Python (Tkinter) and MySQL to manage students, track attendance, and generate attendance records efficiently.

#🚀 Features
🔐 Secure Teacher Login
👨‍🎓 Student Registration (Name, Roll No, Class)
✔ Mark Daily Attendance (Present/Absent)
📊 View Attendance Records
🗄 MySQL Database Storage
📁 Organized Code Structure
🎯 Error handling & form validation

#🛠 Tech Stack
1]Component	Technology
2]Language	Python
3]GUI	Tkinter
4]Database	MySQL
5]Connector	mysql-connector-python

#📂 Project Structure
attendance-system/
│── database.py              # DB connection & table creation
│── auth.py                  # Teacher login authentication
│── student.py               # Student registration & fetching
│── attendance.py            # Mark attendance & calculations
│── gui.py                   # Tkinter GUI
│── main.py                  # Application entry point
│── config.py                # Database credentials
│── README.md                # Documentation

#🗄️ Database Schema
#teachers
Field	Type	Description
id	INT	Primary Key
username	VARCHAR(50)	Login username
password	VARCHAR(255)	Login password

#students
Field	Type	Description
id	INT	Student ID
name	VARCHAR(100)	Full Name
roll_no	VARCHAR(20)	Unique Roll Number
class	VARCHAR(50)	Class/Division

#attendance
Field	Type	Description
id	INT	Attendance entry ID
student_id	INT	FK referencing students
date	DATE	Attendance date
status	ENUM('present', 'absent')	Attendance status

#▶️ How to Run
1. Install required packages
pip install mysql-connector-python

2. Update MySQL credentials in config.py
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'YourPassword',
    'database': 'attendance_system'
}

3. Run the application
python main.py

Default Login
Username: admin  
Password: admin

#📸 Screenshots

(Add images here after uploading them to GitHub)

#🧪 Testing Performed
Unit testing of all modules
Integration testing with database
GUI testing (Tkinter widget behavior)
Login authentication validation
Attendance submission tests

#🚀 Future Enhancements
Face recognition attendance
Export records to Excel/PDF
Multi-teacher login
Attendance summary charts
Cloud-based sync

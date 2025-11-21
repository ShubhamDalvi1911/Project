import tkinter as tk
from tkinter import messagebox, ttk
from auth import authenticate_teacher
from student import register_student, get_students
from attendance import mark_attendance, calculate_attendance_percentage, get_attendance_records
from datetime import date

class AttendanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Attendance Management System")
        self.root.geometry("800x600")

        self.current_frame = None
        self.show_login_frame()

    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

    def show_login_frame(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(pady=20)

        tk.Label(self.current_frame, text="Teacher Login", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.current_frame, text="Username:").pack()
        self.username_entry = tk.Entry(self.current_frame)
        self.username_entry.pack()

        tk.Label(self.current_frame, text="Password:").pack()
        self.password_entry = tk.Entry(self.current_frame, show="*")
        self.password_entry.pack()

        tk.Button(self.current_frame, text="Login", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if authenticate_teacher(username, password):
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def show_main_menu(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(pady=20)

        tk.Label(self.current_frame, text="Main Menu", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.current_frame, text="Register Student", command=self.show_register_student_frame).pack(pady=5)
        tk.Button(self.current_frame, text="Mark Attendance", command=self.show_mark_attendance_frame).pack(pady=5)
        tk.Button(self.current_frame, text="View Attendance Records", command=self.show_view_records_frame).pack(pady=5)
        tk.Button(self.current_frame, text="Logout", command=self.show_login_frame).pack(pady=5)

    def show_register_student_frame(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(pady=20)

        tk.Label(self.current_frame, text="Register Student", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.current_frame, text="Name:").pack()
        self.name_entry = tk.Entry(self.current_frame)
        self.name_entry.pack()

        tk.Label(self.current_frame, text="Roll No:").pack()
        self.roll_no_entry = tk.Entry(self.current_frame)
        self.roll_no_entry.pack()

        tk.Label(self.current_frame, text="Class:").pack()
        self.class_entry = tk.Entry(self.current_frame)
        self.class_entry.pack()

        tk.Button(self.current_frame, text="Register", command=self.register_student).pack(pady=10)
        tk.Button(self.current_frame, text="Back", command=self.show_main_menu).pack()

    def register_student(self):
        name = self.name_entry.get()
        roll_no = self.roll_no_entry.get()
        class_name = self.class_entry.get()
        if register_student(name, roll_no, class_name):
            messagebox.showinfo("Success", "Student registered successfully")
            self.name_entry.delete(0, tk.END)
            self.roll_no_entry.delete(0, tk.END)
            self.class_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Failed to register student (Roll No may already exist)")

    def show_mark_attendance_frame(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(pady=20)

        tk.Label(self.current_frame, text="Mark Attendance", font=("Arial", 16)).pack(pady=10)

        students = get_students()
        self.student_vars = {}
        for student in students:
            var = tk.StringVar(value="absent")
            self.student_vars[student['id']] = var
            tk.Checkbutton(self.current_frame, text=f"{student['name']} ({student['roll_no']})", variable=var, onvalue="present", offvalue="absent").pack()

        tk.Button(self.current_frame, text="Submit Attendance", command=self.submit_attendance).pack(pady=10)
        tk.Button(self.current_frame, text="Back", command=self.show_main_menu).pack()

    def submit_attendance(self):
        for student_id, var in self.student_vars.items():
            status = var.get()
            mark_attendance(student_id, status)
        messagebox.showinfo("Success", "Attendance marked successfully")

    def show_view_records_frame(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(pady=20)

        tk.Label(self.current_frame, text="Attendance Records", font=("Arial", 16)).pack(pady=10)

        records = get_attendance_records()
        tree = ttk.Treeview(self.current_frame, columns=("Name", "Roll No", "Class", "Date", "Status"), show="headings")
        tree.heading("Name", text="Name")
        tree.heading("Roll No", text="Roll No")
        tree.heading("Class", text="Class")
        tree.heading("Date", text="Date")
        tree.heading("Status", text="Status")
        tree.pack(fill=tk.BOTH, expand=True)

        for record in records:
            tree.insert("", tk.END, values=(record['name'], record['roll_no'], record['class'], record['date'], record['status']))

        tk.Button(self.current_frame, text="Back", command=self.show_main_menu).pack(pady=10)

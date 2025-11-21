from database import initialize_database
from auth import add_default_teacher
from gui import AttendanceSystem
import tkinter as tk

if __name__ == "__main__":
    # Initialize database and tables
    initialize_database()

    # Add default teacher
    add_default_teacher()

    # Launch GUI
    root = tk.Tk()
    app = AttendanceSystem(root)
    root.mainloop()

import tkinter as tk
from tkinter import Frame, ttk, messagebox
import sqlite3


class MyApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        TABLE_NAME = "management_table"
        STUDENT_ID = "student_id"
        STUDENT_NAME = "student_name"
        STUDENT_COLLEGE = "student_college"
        STUDENT_ADDRESS = "student_address"
        STUDENT_EMAIL = "student_email"

        connection = sqlite3.connect("database.db")
        connection.execute(
            "CREATE TABLE IF NOT EXISTS "
            + TABLE_NAME
            + " ("
            + STUDENT_ID
            + " INTEGER PRIMARY KEY AUTOINCREMENT, "
            + STUDENT_NAME
            + " TEXT, "
            + STUDENT_COLLEGE
            + " TEXT, "
            + STUDENT_ADDRESS
            + " TEXT, "
            + STUDENT_EMAIL
            + " TEXT);"
        )

        self.title("Management")
        self.form_frame = FormFrame(self)
        self.display_frame = DisplayFrame(self)
        self.show_frame(self.form_frame)

    def show_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


class DisplayFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.app_label = tk.Label(
            self, text="Student Management System", fg="#06a099", width=40
        )
        self.app_label.config(font=("Sylfaen", 30))
        self.app_label.pack()

        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("one", "two", "three", "four")

        self.tree.column("one", width=75)
        self.tree.column("two", width=75)
        self.tree.heading("one", text="Student Name")
        self.tree.heading("two", text="College Name")
        self.tree.heading("three", text="Address")
        self.tree.heading("four", text="Email")

        self.load_data()

        self.tree.pack()

        delete_button = tk.Button(
            self,
            text="Remove Student",
            width=25,
            command=lambda: self.removeSelection(),
        )
        delete_button.pack()

    def load_data(self):
        # Fetch the data from database and puts it into TreeView
        TABLE_NAME = "management_table"
        connection = sqlite3.connect("database.db")
        cursor = connection.execute(
            "SELECT * FROM " + TABLE_NAME + ";"
        )
        i = 0

        for row in cursor:
            self.tree.insert(
                "",
                i,
                text="Student " + str(row[0]),
                values=(row[1], row[2], row[3], row[4]),
            )
            i = i + 1
        
        connection.close()
    
    def removeSelection(self):
        # Removes the selected student from the database and the display
        TABLE_NAME = "management_table"
        STUDENT_NAME = "student_name"
        STUDENT_COLLEGE = "student_college"
        STUDENT_ADDRESS = "student_address"
        STUDENT_EMAIL = "student_email"
        
        connection = sqlite3.connect("database.db")
        student_removed = self.tree.selection()[0]
        list_of_values = self.tree.item(student_removed)["values"]

        student_name = list_of_values[0]
        student_college = list_of_values[1]
        student_address = list_of_values[2]
        student_email = list_of_values[3]

        connection.execute(
            "DELETE FROM "
            + TABLE_NAME
            + " WHERE "
            + STUDENT_NAME
            + " = '"
            + student_name
            + "' AND "
            + STUDENT_COLLEGE
            + " = '"
            + student_college
            + "' AND "
            + STUDENT_ADDRESS
            + " = '"
            + student_address
            + "' AND "
            + STUDENT_EMAIL
            + " = '"
            + student_email
            + "';"
        )
        connection.commit()
        messagebox.showinfo("Success", "Data Deleted Successfully.")
        self.tree.delete(student_removed)


class FormFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.TABLE_NAME = "management_table"
        self.STUDENT_ID = "student_id"
        self.STUDENT_NAME = "student_name"
        self.STUDENT_COLLEGE = "student_college"
        self.STUDENT_ADDRESS = "student_address"
        self.STUDENT_EMAIL = "student_email"

        self.app_label = tk.Label(
            self, text="Student Management System", fg="#06a099", width=40
        )
        self.app_label.config(font=("Sylfaen", 30))
        self.app_label.grid(row=0, columnspan=2, padx=(10, 0), pady=(30, 0))

        self.name_label = tk.Label(
            self, text="Enter your name here:", width=40, anchor="w"
        )
        self.name_label.config(font=("Sylfaen", 12))
        self.name_label.grid(row=1, column=0, padx=(10, 0), pady=(30, 0))

        self.college_label = tk.Label(
            self, text="Enter your college here:", width=40, anchor="w"
        )
        self.college_label.config(font=("Sylfaen", 12))
        self.college_label.grid(row=2, column=0, padx=(10, 0), pady=(30, 0))

        self.email_label = tk.Label(
            self, text="Enter your email here:", width=40, anchor="w"
        )
        self.email_label.config(font=("Sylfaen", 12))
        self.email_label.grid(row=3, column=0, padx=(10, 0), pady=(30, 0))

        self.address_label = tk.Label(
            self, text="Enter your address here:", width=40, anchor="w"
        )
        self.address_label.config(font=("Sylfaen", 12))
        self.address_label.grid(row=4, column=0, padx=(10, 0), pady=(30, 0))

        self.name_entry = tk.Entry(self, width=30)
        self.name_entry.grid(row=1, column=1, padx=(0, 10), pady=20)

        self.college_entry = tk.Entry(self, width=30)
        self.college_entry.grid(row=2, column=1, padx=(0, 10), pady=20)

        self.email_entry = tk.Entry(self, width=30)
        self.email_entry.grid(row=3, column=1, padx=(0, 10), pady=20)

        self.address_entry = tk.Entry(self, width=30)
        self.address_entry.grid(row=4, column=1, padx=(0, 10), pady=20)

        self.input_button = tk.Button(
            self, text="Take Input", command=lambda: self.takeStudentInput()
        )
        self.input_button.grid(row=5, column=0, padx=(10, 0), pady=(30, 20))

        self.display_button = tk.Button(self, text="Display Results", command=lambda: master.show_frame(master.display_frame))
        self.display_button.grid(row=5, column=1, padx=(10, 0), pady=(30, 20))


    def takeStudentInput(self):
        connection = sqlite3.connect("database.db")
        username = self.name_entry.get()
        self.name_entry.delete(0, tk.END)
        college_name = self.college_entry.get()
        self.college_entry.delete(0, tk.END)
        email = self.email_entry.get()
        self.email_entry.delete(0, tk.END)
        address = self.address_entry.get()
        self.address_entry.delete(0, tk.END)

        connection.execute(
            "INSERT INTO "
            + self.TABLE_NAME
            + " ( "
            + self.STUDENT_NAME
            + ", "
            + self.STUDENT_COLLEGE
            + ", "
            + self.STUDENT_ADDRESS
            + ", "
            + self.STUDENT_EMAIL
            + " ) VALUES ( '"
            + username
            + "', '"
            + college_name
            + "', '"
            + address
            + "', '"
            + email
            + "' );"
        )
        connection.commit()
        messagebox.showinfo("Success", "Data Saved Successfully.")

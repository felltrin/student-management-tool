import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
import sqlite3


class MyApp(ttk.Window):
    def __init__(self):
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
        self.update_title(frame)  # Call the method to update the title

    def update_title(self, frame):
        if frame == self.form_frame:
            self.title("Management")
        elif frame == self.display_frame:
            self.title("Display Results")


class DisplayFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        style = ttk.Style(theme="superhero")
        style.configure("CenterLabel.TLabel", anchor="center")

        self.app_label = ttk.Label(
            self, text="Student Management System", style="CenterLabel.TLabel", width=40
        )
        self.app_label.config(font=("Sylfaen", 30))
        self.app_label.grid(row=0, columnspan=2, padx=(10, 0), pady=(10, 0))

        self.tree = ttk.Treeview(self, bootstyle="info", show="headings")
        self.tree["columns"] = ("one", "two", "three", "four")

        # Define headings
        self.tree.heading(
            "one", text="Student Name", command=lambda: self.sort_by_name("one", False)
        )
        self.tree.heading(
            "two", text="College Name", command=lambda: self.sort_by_name("two", False)
        )
        self.tree.heading("three", text="Address")
        self.tree.heading("four", text="Email")

        self.load_data()

        self.tree.grid(row=1, columnspan=2, padx=(10, 0), pady=(30, 0))

        delete_button = ttk.Button(
            self,
            text="Remove Student",
            width=20,
            command=lambda: self.removeSelection(),
        )
        delete_button.grid(row=2, column=0, padx=(10, 0), pady=20)

        self.back_button = ttk.Button(
            self,
            text="Back",
            command=lambda: master.show_frame(master.form_frame),
            width=20,
        )
        self.back_button.grid(row=2, column=1, padx=(10, 0), pady=20)

    def sort_by_name(self, col, reverse):
        data = [(self.tree.set(item, col), item) for item in self.tree.get_children("")]
        data.sort(reverse=reverse)
        for index, (val, item) in enumerate(data):
            self.tree.move(item, "", index)
        self.tree.heading(col, command=lambda: self.sort_by_name(col, not reverse))

    def load_data(self):
        # Fetch the data from database and puts it into TreeView
        TABLE_NAME = "management_table"
        connection = sqlite3.connect("database.db")
        cursor = connection.execute("SELECT * FROM " + TABLE_NAME + ";")
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
            + str(student_name)
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
        Messagebox.show_info("Success", "Data Deleted Successfully.")
        self.tree.delete(student_removed)


class FormFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        style = ttk.Style(theme="superhero")
        style.configure("CenterLabel.TLabel", anchor="center")

        self.master = master

        self.TABLE_NAME = "management_table"
        self.STUDENT_ID = "student_id"
        self.STUDENT_NAME = "student_name"
        self.STUDENT_COLLEGE = "student_college"
        self.STUDENT_ADDRESS = "student_address"
        self.STUDENT_EMAIL = "student_email"

        self.app_label = ttk.Label(
            self, text="Student Management System", style="CenterLabel.TLabel", width=40
        )
        self.app_label.config(font=("Sylfaen", 30))
        self.app_label.grid(row=0, columnspan=2, padx=(10, 0), pady=(30, 0))

        self.name_label = ttk.Label(
            self, text="Enter your name here:", width=40, anchor="w"
        )
        self.name_label.config(font=("Sylfaen", 12))
        self.name_label.grid(row=1, column=0, padx=(10, 0), pady=(30, 20))

        self.college_label = ttk.Label(
            self, text="Enter your college here:", width=40, anchor="w"
        )
        self.college_label.config(font=("Sylfaen", 12))
        self.college_label.grid(row=2, column=0, padx=(10, 0), pady=(30, 20))

        self.email_label = ttk.Label(
            self, text="Enter your email here:", width=40, anchor="w"
        )
        self.email_label.config(font=("Sylfaen", 12))
        self.email_label.grid(row=3, column=0, padx=(10, 0), pady=(30, 20))

        self.address_label = ttk.Label(
            self, text="Enter your address here:", width=40, anchor="w"
        )
        self.address_label.config(font=("Sylfaen", 12))
        self.address_label.grid(row=4, column=0, padx=(10, 0), pady=(30, 20))

        self.name_entry = ttk.Entry(self, width=30)
        self.name_entry.grid(row=1, column=1, padx=(0, 10), pady=20)

        self.college_entry = ttk.Entry(self, width=30)
        self.college_entry.grid(row=2, column=1, padx=(0, 10), pady=20)

        self.email_entry = ttk.Entry(self, width=30)
        self.email_entry.grid(row=3, column=1, padx=(0, 10), pady=20)

        self.address_entry = ttk.Entry(self, width=30)
        self.address_entry.grid(row=4, column=1, padx=(0, 10), pady=20)

        self.input_button = ttk.Button(
            self, text="Take Input", command=lambda: self.takeStudentInput()
        )
        self.input_button.grid(row=5, column=0, padx=(10, 0), pady=(30, 20))

        self.display_button = ttk.Button(
            self,
            text="Display Results",
            command=lambda: master.show_frame(master.display_frame),
        )
        self.display_button.grid(row=5, column=1, padx=(10, 0), pady=(30, 20))

    def takeStudentInput(self):
        connection = sqlite3.connect("database.db")
        username = self.name_entry.get()
        self.name_entry.delete(0, ttk.END)
        college_name = self.college_entry.get()
        self.college_entry.delete(0, ttk.END)
        email = self.email_entry.get()
        self.email_entry.delete(0, ttk.END)
        address = self.address_entry.get()
        self.address_entry.delete(0, ttk.END)

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
        # Clear the Treeview and then reload the data
        self.master.display_frame.tree.delete(
            *self.master.display_frame.tree.get_children()
        )
        # Load the data into the tree view after taking input
        self.master.display_frame.load_data()
        Messagebox.show_info("Success", "Data Saved Successfully.")

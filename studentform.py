import tkinter as tk


class MyApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Management")
        self.form_frame = FormFrame(self)
        # self.frame2 = Frame2(self)
        self.show_frame(self.form_frame)

    def show_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


class FormFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

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

    def takeStudentInput(self):
        username = self.name_entry.get()
        self.name_entry.delete(0, tk.END)
        print(username)

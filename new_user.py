import tkinter as tk
from tkinter import messagebox
from base_dialog import BaseDialog
from user_manager import UserManager

class NewUserDialog(BaseDialog):
    def __init__(self, parent):
        super().__init__(parent, "Create New User", bg_color="white")
        self._user_manager = UserManager()

    def _setup_ui(self):
         # filler1 label
        filler1Label = tk.Label(self, text="Enroll in Online Banking", font=("Times New Roman", 16), bg="red",fg="white",anchor='w',padx=10)      # <-- little padding from the left edge
        filler1Label.pack(fill='x', pady=(0, 0))
        tk.Label(self, text="Let's get started",
                font=("Times New Roman", 14, "bold"), bg="white", fg="black").place(x=10,y=30)

        tk.Label(self, text="Please provide the following information to being your enrollment.",
                font=("Times New Roman", 10), bg="white", fg="black").place(x=10,y=60)


        tk.Label(self, text="Enter username:",
                font=("Times New Roman", 12), bg="white", fg="black").place(x=10,y=80)

        self._username_entry = tk.Entry(self, width=30, font=("Times New Roman", 12))
        self._username_entry.place(x=10,y=100)

        tk.Label(self, text="Enter password:",
                font=("Times New Roman", 12), bg="white", fg="black").place(x=10,y=140)

        self._password_entry = tk.Entry(self, width=30, show='*', font=("Times New Roman", 12))
        self._password_entry.place(x=10,y=160)

        submit_button = tk.Button(self, text="Submit",
                                command=self._submit_user,
                                bg="dark blue", fg="white", width=15)
        
        submit_button.place(x=10,y=200)
        tk.Button(self, text="Cancel", command=self.destroy,
                  bg="white", fg="dark blue", width=15, borderwidth=2,relief="flat").place(x=150,y=200)


    def _submit_user(self):
        username = self._username_entry.get().strip()
        password = self._password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        # Force immediate save after adding user
        if self._user_manager.add_user(username, password):
            self._user_manager._save_users()  # Explicit save
            print(f"User created: {username}")  # Debug
            print(f"Current users: {self._user_manager._users}")  # Debug
            messagebox.showinfo("Success", f"User {username} created successfully!")
            self.destroy()
        else:
            messagebox.showerror("Error", f"Username {username} already exists")
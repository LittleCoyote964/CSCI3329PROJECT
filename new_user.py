import tkinter as tk
from tkinter import messagebox
from base_dialog import BaseDialog
from user_manager import UserManager

class NewUserDialog(BaseDialog):
    def __init__(self, parent):
        super().__init__(parent, "Create New User", bg_color="gray")
        self._user_manager = UserManager()

    def _setup_ui(self):
        tk.Label(self, text="Create Username and Password",
                font=("Times New Roman", 20), bg="gray", fg="white").pack(pady=10)

        tk.Label(self, text="Enter username:",
                font=("Times New Roman", 14), bg="gray", fg="white").pack()

        self._username_entry = tk.Entry(self, width=30, font=("Times New Roman", 12))
        self._username_entry.pack(pady=5)

        tk.Label(self, text="Enter password:",
                font=("Times New Roman", 14), bg="gray", fg="white").pack()

        self._password_entry = tk.Entry(self, width=30, show='*', font=("Times New Roman", 12))
        self._password_entry.pack(pady=5)

        submit_button = tk.Button(self, text="Submit",
                                command=self._submit_user,
                                bg="white", fg="black", width=15)
        submit_button.pack(pady=20)

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
import tkinter as tk
from tkinter import messagebox
from base_dialog import BaseDialog
from user_manager import UserManager

class ForgotPasswordDialog(BaseDialog):
    def __init__(self, parent):
        # Sets up the forgot password window
        super().__init__(parent, "Forgot Password", bg_color="gray")
        self._user_manager = UserManager()  # Load user manager to access user data

    def _setup_ui(self):
        # Pops out a window to ask for username
        tk.Label(self, text="Reset Password",
                 font=("Times New Roman", 20), bg="gray", fg="white").pack(pady=10)

        tk.Label(self, text="Enter your username:",
                 font=("Times New Roman", 14), bg="gray", fg="white").pack()

        self._username_entry = tk.Entry(self, width=30, font=("Times New Roman", 12))
        self._username_entry.pack(pady=5)

        submit_button = tk.Button(self, text="Next",
                                  command=self._verify_username,  # Calls function to verify user exists
                                  bg="white", fg="black", width=15)
        submit_button.pack(pady=20)

    def _verify_username(self):
        # Checks if username exists in users.json
        username = self._username_entry.get().strip()
        if not username:
            messagebox.showerror("Error", "Please enter a username.")
            return

        self._user_manager.reload_users()  # Refreshes the user data
        if username in self._user_manager._users:
            self._username = username
            self._show_new_password_entry()
        else:
            messagebox.showerror("Error", f"Username '{username}' not found!")

    def _show_new_password_entry(self):
        # Creats a new window to enter a new password
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Enter New Password",
                 font=("Times New Roman", 20), bg="gray", fg="white").pack(pady=10)

        self._new_password_entry = tk.Entry(self, width=30, font=("Times New Roman", 12), show="*")
        self._new_password_entry.pack(pady=5)

        submit_button = tk.Button(self, text="Reset Password",
                                  command=self._reset_password,  # Calls function to save new password
                                  bg="white", fg="black", width=15)
        submit_button.pack(pady=20)

    def _reset_password(self):
        # Saves the new password to the user.json
        new_password = self._new_password_entry.get().strip()
        if not new_password:
            messagebox.showerror("Error", "Please enter a new password.")
            return

        # Updates password 
        self._user_manager._users[self._username]["password"] = new_password
        self._user_manager._save_users()

        messagebox.showinfo("Success", "Password reset successfully!")
        self.destroy()

import tkinter as tk
from tkinter import messagebox
from base_dialog import BaseDialog
from user_manager import UserManager

class ForgotPasswordDialog(BaseDialog):
    def __init__(self, parent):
        # Sets up the forgot password window
        super().__init__(parent, "Forgot Password", bg_color="white")
        self._user_manager = UserManager()  # Load user manager to access user data

    def _setup_ui(self):
        # Pops out a window to ask for username
        tk.Label(self, text="Forgot Password",
                 font=("Times New Roman", 14, "bold"), bg="white", fg="black").place(x=10,y=35)
        # filler label
        tk.Label(self, text="Please provide some basic information and we'll help with your Password.",
                 font=("Times New Roman", 9), bg="white", fg="black").place(x=10,y=70)
        # filler1 label
        tk.Label(self, text="Forgot User Password", font=("Times New Roman", 16), bg="red",fg="white",anchor='w', padx=10).pack(fill='x')

        tk.Label(self, text="User ID",
                 font=("Times New Roman", 12), bg="white", fg="black").place(x=10,y=100)

        self._username_entry = tk.Entry(self, width=30, font=("Times New Roman", 12))
        self._username_entry.place(x=10,y=120)

        submit_button = tk.Button(self, text="Continue",
                                  command=self._verify_username,  # Calls function to verify user exists
                                  bg="dark blue", fg="white", width=15, relief="flat")
        submit_button.place(x=10,y=180)
        tk.Button(self, text="Cancel", command=self.destroy,
                  bg="white", fg="dark blue", width=15, borderwidth=2,relief="flat").place(x=150,y=180)

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
        # filler1 label
        tk.Label(self, text="Forgot User Password", font=("Times New Roman", 16), bg="red",fg="white",anchor='w', padx=10).pack(fill='x')
        tk.Label(self, text="Forgot Password",
                 font=("Times New Roman", 14, "bold"), bg="white", fg="black").place(x=10,y=45)
        tk.Label(self, text="Enter New Password",
                 font=("Times New Roman", 12), bg="white", fg="black").place(x=10,y=110)
        # filler2 label
        tk.Label(self, text="Please provide the new password and we'll help with your Password.",
                 font=("Times New Roman", 9), bg="white", fg="black").place(x=10,y=80)

        self._new_password_entry = tk.Entry(self, width=30, font=("Times New Roman", 12), show="*")
        self._new_password_entry.place(x=10,y=130)

        submit_button = tk.Button(self, text="Reset Password",
                                  command=self._reset_password,  # Calls function to save new password
                                  bg="dark blue", fg="white", width=15)
        submit_button.place(x=10,y=200)

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

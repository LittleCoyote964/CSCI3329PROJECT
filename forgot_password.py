import tkinter as tk
from base_dialog import BaseDialog


class ForgotPasswordDialog(BaseDialog):
    def __init__(self, parent):
        super().__init__(parent, "Forgot Password", bg_color="gray")

    def _setup_ui(self):
        tk.Label(self, text="Reset Password",
                 font=("Times New Roman", 20), bg="gray", fg="white").pack(pady=10)

        tk.Label(self, text="Enter your username:",
                 font=("Times New Roman", 14), bg="gray", fg="white").pack()

        self._username_entry = tk.Entry(self, width=30, font=("Times New Roman", 12))
        self._username_entry.pack(pady=5)

        submit_button = tk.Button(self, text="Submit",
                                  command=self._reset_password,
                                  bg="white", fg="black", width=15)
        submit_button.pack(pady=20)

    def _reset_password(self):
        username = self._username_entry.get().strip()
        if not username:
            print("Please enter a valid username.")
            return

        print(f"Password reset sent to {username}")
        self.destroy()
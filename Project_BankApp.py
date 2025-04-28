import tkinter as tk
import tkinter.font as tkFont
from new_user import NewUserDialog
from forgot_password import ForgotPasswordDialog
from user_manager import UserManager


class BankApp:
    def __init__(self, master):
        self.master = master
        self.user_manager = UserManager()
        self.master.title("Bank Account Login")
        self.master.configure(bg="maroon")
        self._setup_window()
        self._setup_login_ui()

    def _setup_window(self):
        self.master.geometry("600x600")
        self.master.resizable(False, False)
        self._center_window()

    def _center_window(self):
        self.master.update_idletasks()
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width // 2) - (600 // 2)
        y = (screen_height // 2) - (600 // 2)
        self.master.geometry(f"+{x}+{y}")

    def _setup_login_ui(self):
        # header
        tk.Label(self.master, text="Bank of Project",
                 font=("Times New Roman", 30), bg="maroon", fg="white").place(x=175, y=50)

        # username
        tk.Label(self.master, text="Username:",
                 font=("Times New Roman", 20), bg="maroon", fg="white").place(x=100, y=150)
        self.user_entry = tk.Entry(self.master, font=("Times New Roman", 20), fg="maroon", bg="white", width=15)
        self.user_entry.place(x=340, y=150)

        # password
        tk.Label(self.master, text="Password:",
                 font=("Times New Roman", 20), bg="maroon", fg="white").place(x=100, y=250)
        self.pass_entry = tk.Entry(self.master, font=("Times New Roman", 20), show="*", bg="white", fg="black",
                                   width=15)
        self.pass_entry.place(x=340, y=250)

        # buttons
        tk.Button(self.master, text="Login", width=23, height=2, bg="gray", fg="black",
                  command=self._handle_login).place(x=200, y=350)

        tk.Button(self.master, text="Forgot Password?", width=23, height=2, bg="gray", fg="black",
                  command=lambda: ForgotPasswordDialog(self.master)).place(x=200, y=400)

        tk.Button(self.master, text="Create New User", width=23, height=2, bg="gray", fg="black",
                  command=lambda: NewUserDialog(self.master)).place(x=200, y=450)

    def _handle_login(self):
        username = self.user_entry.get().strip()
        password = self.pass_entry.get().strip()

        if self.user_manager.authenticate(username, password):
            balances = self.user_manager.get_balances(username)
            if balances:
                self.master.withdraw()
                from Project_menu import UserMenu
                UserMenu(self.master, username, balances, self._show_login)
        else:
            tk.Label(self.master, text="Invalid credentials!", fg="red", bg="maroon").place(x=200, y=500)

    def _show_login(self):
        self.user_entry.delete(0, tk.END)
        self.pass_entry.delete(0, tk.END)
        self.master.deiconify()


if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
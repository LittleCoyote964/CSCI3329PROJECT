import tkinter as tk
from tkinter import messagebox
from base_dialog import BaseDialog
from user_manager import UserManager


class UserMenu(BaseDialog):
    def __init__(self, parent, user_id, balances, show_login_callback):
        self._user_id = user_id
        self._show_login_callback = show_login_callback
        self._balances = balances
        # Initialize StringVars before calling parent
        self._balance_var_checking = tk.StringVar()
        self._balance_var_savings = tk.StringVar()
        super().__init__(parent, "User Menu", width=600, height=600, bg_color="maroon")

    def _setup_ui(self):

        # header
        tk.Label(self, text="User Menu",
                 font=("Times New Roman", 30), bg="maroon", fg="white").place(x=200, y=50)

        # buttons
        tk.Button(self, text="Check Balance", width=23, height=2, bg="gray", fg="black",
                  command=self._handle_account_details).place(x=200, y=100)

        tk.Button(self, text="Withdraw", width=23, height=2, bg="gray", fg="black",
                  command=self._handle_withdrawal).place(x=200, y=150)

        tk.Button(self, text="Deposit", width=23, height=2, bg="gray", fg="black",
                  command=self._handle_deposit).place(x=200, y=200)

        tk.Button(self, text="Transfer to Savings", width=23, height=2, bg="gray", fg="black",
                  command=self._handle_transfer).place(x=200, y=250)

        tk.Button(self, text="Logout", width=23, height=2, bg="gray", fg="black",
                  command=self._handle_logout).place(x=200, y=300)

    def _handle_account_details(self):
        messagebox.showinfo("Account Details",
                            f"Checking: ${self._balances[0]:.2f}\n"
                            f"Savings: ${self._balances[1]:.2f}")

    def _handle_withdrawal(self):
        withdrawal_dialog = WithdrawalDialog(self, self._user_id, self._balance_var_checking)
        withdrawal_dialog.grab_set()

    def _handle_deposit(self):
        deposit_dialog = DepositDialog(self, self._user_id, self._balance_var_checking)
        deposit_dialog.grab_set()

    def _handle_transfer(self):
        transfer_dialog = TransferDialog(self, self._user_id, self._balance_var_checking, self._balance_var_savings)
        transfer_dialog.grab_set()

    def _handle_logout(self):
        self.destroy()
        self._show_login_callback()


class WithdrawalDialog(BaseDialog):
    def __init__(self, parent, user_id, balance_var):
        self._user_id = user_id
        self._balance_var = balance_var
        super().__init__(parent, "Withdraw", bg_color="gray")

    def _setup_ui(self):
        tk.Label(self, text="Withdraw", font=("Times New Roman", 20), bg="gray", fg="white").pack(pady=10)
        tk.Label(self, text="Enter withdrawal amount:", font=("Times New Roman", 14), bg="gray", fg="white").pack()

        self._amount_entry = tk.Entry(self, font=("Times New Roman", 14))
        self._amount_entry.pack(pady=5)

        self._result_label = tk.Label(self, text="", font=("Times New Roman", 12), bg="gray", fg="white")
        self._result_label.pack(pady=5)

        tk.Button(self, text="Withdraw", command=self._process_withdrawal,
                  bg="white", fg="black", width=15).pack(pady=5)
        tk.Button(self, text="Close", command=self.destroy,
                  bg="white", fg="black", width=15).pack(pady=20)

    def _process_withdrawal(self):
        amount = self._amount_entry.get().strip()
        try:
            amount = float(amount.replace(",", ""))
            if amount <= 0:
                self._result_label.config(text="Enter a valid positive amount!", fg="red")
                return

            user_manager = UserManager()
            current_balance = user_manager.get_balances(self._user_id)[0]

            if amount > current_balance:
                self._result_label.config(text="Insufficient funds for this withdrawal!", fg="red")
                return

            if not user_manager.update_balance(self._user_id, "checking", -amount):
                self._result_label.config(text="Transaction failed!", fg="red")
                return

            new_balance = user_manager.get_balances(self._user_id)[0]
            self._balance_var.set(f"Checking: ${new_balance:.2f}")
            self._result_label.config(text=f"Withdrawal Successful: ${amount:.2f}", fg="green")

        except ValueError:
            self._result_label.config(text="Invalid input! Enter a number.", fg="red")


class DepositDialog(BaseDialog):
    def __init__(self, parent, user_id, balance_var):
        self._user_id = user_id
        self._balance_var = balance_var
        super().__init__(parent, "Deposit", bg_color="gray")

    def _setup_ui(self):
        tk.Label(self, text="Deposit", font=("Times New Roman", 20), bg="gray", fg="white").pack(pady=10)
        tk.Label(self, text="Enter deposit amount:", font=("Times New Roman", 14), bg="gray", fg="white").pack()

        self._amount_entry = tk.Entry(self, font=("Times New Roman", 14))
        self._amount_entry.pack(pady=5)

        self._result_label = tk.Label(self, text="", font=("Times New Roman", 12), bg="gray", fg="white")
        self._result_label.pack(pady=5)

        tk.Button(self, text="Deposit", command=self._process_deposit,
                  bg="white", fg="black", width=15).pack(pady=5)
        tk.Button(self, text="Close", command=self.destroy,
                  bg="white", fg="black", width=15).pack(pady=20)

    def _process_deposit(self):
        amount = self._amount_entry.get().strip()
        try:
            amount = float(amount.replace(",", ""))
            if amount <= 0:
                self._result_label.config(text="Enter a valid positive amount!", fg="red")
                return

            user_manager = UserManager()
            if not user_manager.update_balance(self._user_id, "checking", amount):
                self._result_label.config(text="User not found!", fg="red")
                return

            new_balance = user_manager.get_balances(self._user_id)[0]
            self._balance_var.set(f"Checking: ${new_balance:.2f}")
            self._result_label.config(text=f"Deposit Successful: ${amount:.2f}", fg="green")

        except ValueError:
            self._result_label.config(text="Invalid input! Enter a number.", fg="red")

#child class to transfer funds from checkings to savings
class TransferDialog(BaseDialog):
    def __init__(self, parent, user_id, checking_var, savings_var):
        self._user_id = user_id
        self._checking_var = checking_var
        self._savings_var = savings_var
    
        super().__init__(parent, "Transfer to Savings", bg_color="gray")
    #adjusting the gui for the transfer button when pressed
    def _setup_ui(self):
        tk.Label(self, text="Transfer to Savings", font = ("Time New Roman", 12), bg = "gray", fg = "white").pack(pady=10)
        tk.Label(self, text="Enter the amount you want to transfer:", font = ("Times New Roman", 14), bg = "gray", fg = "white").pack()

        self._amount_entry = tk.Entry(self, font = ("Times New Roman", 12))
        self._amount_entry.pack(pady=5)

        self._result_label = tk.Label(self, text="", font=("Times New Roman", 12), bg="gray", fg="white")
        self._result_label.pack(pady=5)

        tk.Button(self, text="Transfer", command=self._process_transfer,
                  bg="white", fg="black", width=15).pack(pady=5)
        tk.Button(self, text="Close", command=self.destroy,
                  bg="white", fg="black", width=15).pack(pady=20)
    
    #this will calculate and enter the amount that is stored into the savings account. 
    def _process_transfer(self):
        amount = self._amount_entry.get().strip()

    #will add error handling to the process
        try:
            amount = float(amount.replace(",", ""))
            if amount <= 0:
                self._result_label.config(text="Please enter a valid amount.", fg = "red")
                return
            #checks to see if the user is logged in
            um = UserManager() 
            #to subtract the amount from the checkings
            ok_checkings = um.update_balance(self._user_id, "checkings", -amount)
            if not ok_checkings:
                self._result_label.config(text="User not found or insufficient funds!", fg = "red")
                return
            #to add the amount to the savings
            ok_savings = um.update_balance(self._user_id, "savings", amount)
            if not ok_savings:
                self._result_label.config(text="Transfer failed!", fg = "red")
            
            check, saving = um.get_balances(self._user_id)
            self._checking_var.set(f"Checking: ${check: .2f}")
            self._savings_var.set(f"Savings: ${saving: .2f}")

            self._result_label.config(text = f"Transferred ${amount: .2f}", fg = "green")

        except ValueError:
            self.result_label.config(text="Invalid amount format.", fg="red")


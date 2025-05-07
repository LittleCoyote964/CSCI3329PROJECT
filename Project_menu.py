import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
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
        super().__init__(parent, "User Menu", width=600, height=600, bg_color="white")

    def _setup_ui(self):
        # Welcome message
        message = tk.Label(self, text=f"Hello, {self._user_id}",font=("bold", 16), bg="white",fg="black")
        message.place(x=25,y=110)
        # Title label
        titleLabel = tk.Label(self, text="Personal accounts", 
                            font=("Times New Roman", 11), 
                            bg="white", fg="black", anchor="w",width=36, padx=15)
        titleLabel.place(x=25, y=172)

        # Divider line
        divider = tk.Frame(self, bg="dark blue", height=2, width=360)
        divider.place(x=25, y=197)

        self._balance_var_checking.set(f"${self._balances[0]:.2f}")
        self._balance_var_savings.set(f"${self._balances[1]:.2f}")

        # "Checking" label (left)
        checkingLabel = tk.Label(self, text="My Checking\n", 
                                font=("Times New Roman", 15),
                                bg="lightgrey",
                                fg="dark blue",
                                anchor="w",  # west (left) alignment
                                width=15,
                                padx=15)
        checkingLabel.place(x=25, y=200)

        # Checking amount (right)
        checkingAmount = tk.Label(self, textvariable=self._balance_var_checking, 
                                font=("Times New Roman", 15),
                                bg="lightgrey",
                                fg="dark blue",
                                anchor="e",  # east (right) alignment
                                width=17)
        checkingAmount.place(x=190, y=200)

        # "Savings" label (left)
        savingsLabel = tk.Label(self, text="My Savings\n", 
                                font=("Times New Roman", 15),
                                bg="lightgrey",
                                fg="dark blue",
                                anchor="w",
                                width=15,
                                padx=15)
        savingsLabel.place(x=25, y=260)

        # Savings amount (right)
        savingsAmount = tk.Label(self, textvariable=self._balance_var_savings, 
                                font=("Times New Roman", 15),
                                bg="lightgrey",
                                fg="dark blue",
                                anchor="e",
                                width=17)
        savingsAmount.place(x=190, y=260)

        # header
        tk.Label(self, text="Accounts",
                 font=("Times New Roman", 15), width=14, height=2, bg="white", fg="black",pady=2, relief="ridge").place(x=0, y=50)

        # buttons
        
        tk.Button(self, text="Withdraw", font=("Times New Roman", 13), width=17, height=2, bg="light grey", fg="black",
                  command=self._handle_withdrawal).place(x=450, y=50)

        tk.Button(self, text="Deposit", font=("Times New Roman", 13), width=17, height=2, bg="light grey", fg="black",
                  command=self._handle_deposit).place(x=300, y=50)

        tk.Button(self, text="Transfer",font=("Times New Roman", 13), width=17, height=2, bg="light grey", fg="black",
                  command=self._handle_transfer).place(x=150, y=50)
        # top border
        tk.Label(self, text="BANK OF AMERICA",font=("Calibri",13,"bold"),bg="red",fg="white", anchor="w", padx=10,pady=14).pack(fill='x', pady=(0, 0))

        # filler
        tk.Label(self, text="Online Banking",font=("Times New Roman",13),bg="red",fg="white").place(x=210,y=15)

        # Load the image
        logo_image = Image.open("logo1.png")  
        logo_image = logo_image.resize((49, 49))  # Resize as needed
        logo_photo = ImageTk.PhotoImage(logo_image)

        # Create label with image
        headerLabel = tk.Label(self,image=logo_photo, bg="red")
        headerLabel.image = logo_photo  # Keep a reference to avoid garbage collection
        headerLabel.place(x=150, y=0)

        # filler2
        tk.Label(self, text="Update profile  |  Security Center",font=("Times New Roman",10),bg="white",fg="blue").place(x=150,y=115)

        tk.Button(self, text="Log Out", bg="red", fg="white", relief="flat", borderwidth=0,
                  command=self._handle_logout).place(x=535, y=5)

    def _handle_account_details(self):
        um = UserManager()
        updated_balances = um.get_balances(self._user_id)

        if updated_balances:
            self._balances = updated_balances
            messagebox.showinfo("Account Details",
                                f"Checking: ${self._balances[0]:.2f}\n"
                                f"Savings: ${self._balances[1]:.2f}")
        else:
            messagebox.showerror("Error", "Failed to retrieve account details.")

    def _handle_withdrawal(self):
        withdrawal_dialog = WithdrawalDialog(self, self._user_id, self._balance_var_checking)
        withdrawal_dialog.grab_set()

    def _handle_deposit(self):
        deposit_dialog = DepositDialog(self, self._user_id, self._balances, self._balance_var_checking, self._balance_var_savings)
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
        super().__init__(parent, "Withdraw", bg_color="white")

    def _setup_ui(self):
        tk.Label(self,
        text="Withdraw",
        font=("Times New Roman", 14),
        bg="red",
        fg="white",
        padx=10,
        anchor="center",      # <--- center text inside label
        justify="center"      # <--- if multiline, center each line
    ).pack(fill='x', pady=(0, 0))  # <--- removes any space at the top

        
        tk.Label(self, text="Enter withdrawal amount:", font=("Times New Roman", 14), bg="white", fg="black").pack()

        self._amount_entry = tk.Entry(self, font=("Times New Roman", 14), justify="right")
        self._amount_entry.pack(pady=5)

        self._result_label = tk.Label(self, text="", font=("Times New Roman", 12), bg="white", fg="white")
        self._result_label.pack(pady=5)

        tk.Button(self, text="Withdraw", command=self._process_withdrawal,
                  bg="dark blue", fg="white", width=15).pack(pady=5)
        tk.Button(self, text="Close", command=self.destroy,
                  bg="red", fg="white", width=15).pack(pady=20)

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
            self._balance_var.set(f"${new_balance:.2f}")
            self._result_label.config(text=f"Withdrawal Successful: ${amount:.2f}", fg="green")

        except ValueError:
            self._result_label.config(text="Invalid input! Enter a number.", fg="red")


class DepositDialog(BaseDialog):
    def __init__(self, parent, user_id, balances, checking_var, savings_var):
        self._user_id = user_id
        self._checking_var = checking_var
        self._savings_var = savings_var 
        self._balances = balances
        super().__init__(parent, "Deposit", bg_color="white")

    def _setup_ui(self):

        tk.Label(self,
        text="Deposit",
        font=("Times New Roman", 14),
        bg="light grey",
        fg="grey",
        padx=10,
        anchor="center",      # <--- center text inside label
        justify="center"      # <--- if multiline, center each line
    ).pack(fill='x', pady=(0, 0))  # <--- removes any space at the top


        tk.Label(self, text="Deposit To:", font=("Times New Roman", 14), bg="light gray", fg="black",anchor="w",padx=15, width=500).place(x=0, y=30)

        tk.Label(self, text="Amount:", font = ("Times New Roman", 14), bg = "light gray", fg = "black",anchor="w",padx=15, width=500).place(x=0, y=60)

        # Savings amount (right)
        self._amount_entry = tk.Entry(self, font = ("Times New Roman", 12),justify='right', bg="light gray", fg="dark blue")
        self._amount_entry.place(x=225, y=62)         

        #will give the user the choice to pick where to deposit their funds
        self._account_var = tk.StringVar(value="checking")
        choices_frame = tk.Frame(self, bg ="light gray")
        tk.Radiobutton(choices_frame, text = "Checking",variable=self._account_var, value="checking", bg="light gray", fg="black").pack(side="left",padx=10)
        tk.Radiobutton(choices_frame, text="Savings", variable=self._account_var, value="savings", bg="light gray", fg="black").pack(side="left",padx=10)
        choices_frame.place(x=220, y=32)


        #self._amount_entry = tk.Entry(self, font=("Times New Roman", 14))
        #self._amount_entry.pack(pady=5)

        self._result_label = tk.Label(self, text="", font=("Times New Roman", 12), bg="white", fg="white")
        self._result_label.place(x=90,y=90)

        # filler label
        tk.Label(self, text="Investment, insurace and annuity products:                                                                                                                 \n   Are not FDIC Insured\n   Are Not Bank Guaranteed\n   May Lose Value\n   Are Not Deposits\n   Are Not Insured by Any Governmental Agency\n   Are Not a Condition to Any Banking Service or Activity"
                 , font = ("Times New Roman", 10), bg = "light gray", fg = "grey",justify="left",padx=15).place(x=0, y=115)

        tk.Button(self, text="Deposit", command=self._process_deposit,
                  bg="dark blue", fg="white", width=15).place(x=160,y=250)
        tk.Button(self, text="Close", command=self.destroy,
                  bg="white", fg="dark blue", width=15, relief="flat", borderwidth=0).place(x=20,y=250)

    def _process_deposit(self):
        #depending on the account the user picks
        account = self._account_var.get()
        amount = self._amount_entry.get().strip()
        try:
            amount = float(amount.replace(",", ""))
            if amount <= 0:
                self._result_label.config(text="Enter a valid positive amount!", fg="red")
                return

            user_manager = UserManager()
            if not user_manager.update_balance(self._user_id, account, amount):
                self._result_label.config(text="User not found!", fg="red")
                return
            
            #to refresh the display
            checking, savings = user_manager.get_balances(self._user_id)

            if account == "checking":
                self._checking_var.set(f"${checking:.2f}")
            else:
                self._savings_var.set(f"${savings:.2f}")

            self._result_label.config(
                text=f"Deposit Successful: ${amount:.2f} to {account}", fg="green")

        except ValueError:
            self._result_label.config(text="Invalid input! Enter a number.", fg="red")

#child class to transfer funds from checkings to savings
class TransferDialog(BaseDialog):
    def __init__(self, parent, user_id, checking_var, savings_var):
        self._user_id = user_id
        self._checking_var = checking_var
        self._savings_var = savings_var
    
        super().__init__(parent, "Transfer to Savings", bg_color="white")
    #adjusting the gui for the transfer button when pressed
    def _setup_ui(self):
        tk.Label(self,
        text="Transfer",
        font=("Times New Roman", 14),
        bg="light grey",
        fg="grey",
        padx=10,
        anchor="center",      # <--- center text inside label
        justify="center"      # <--- if multiline, center each line
    ).pack(fill='x', pady=(0, 0))  # <--- removes any space at the top
        
        # "Checking" label (left)
        checking = tk.Label(self, text="From\n", 
                                font=("Times New Roman", 14),
                                bg="lightgrey",
                                fg="black",
                                anchor="w",  # west (left) alignment
                                width=15,
                                padx=12)
        checking.place(x=0, y=30)

        # Checking amount (right)
        checkingA = tk.Label(self, text="My Checking\n", 
                                font=("Times New Roman", 14),
                                bg="lightgrey",
                                fg="dark blue",
                                anchor="e",  # east (right) alignment
                                width=23,padx=15)
        checkingA.place(x=145, y=30)

        # "Savings" label (left)
        savings = tk.Label(self, text="To\n", 
                                font=("Times New Roman", 14),
                                bg="lightgrey",
                                fg="black",
                                anchor="w",
                                width=15,
                                padx=12)
        savings.place(x=0, y=80)

        # Savings amount (right)
        savingsA = tk.Label(self, text="My Savings\n", 
                                font=("Times New Roman", 14),
                                bg="lightgrey",
                                fg="dark blue",
                                anchor="e",
                                width=23,padx=15)
        savingsA.place(x=145, y=80)        
        
        
        
        tk.Label(self, text="Amount", font = ("Times New Roman", 14), bg = "light gray", fg = "black",anchor="w",padx=15, width=500).place(x=0, y=140)

        # Savings amount (right)
        self._amount_entry = tk.Entry(self, font = ("Times New Roman", 12),justify='right', bg="light grey", fg="dark blue")
        self._amount_entry.place(x=225, y=142)         
        
        # filler label
        tk.Label(self, text="Investing involves risk. There is alwaysthe potential of losing money when you\ninvest in securities. Asset allocation, diversification, and rebalancing do not ensure\na profit or protect against loss in declining markets."
                 , font = ("Times New Roman", 8), bg = "light gray", fg = "grey",justify="left",padx=15).place(x=0, y=200)


        # show balances
        um=UserManager()
        check, saving = um.get_balances(self._user_id)
        tk.Label(self, text=f"Available balance ${check}", 
                                font=("Times New Roman", 8),
                                bg="lightgrey",
                                fg="grey",
                                anchor="e",  # east (right) alignment
                                width=33).place(x=190, y=53)
        tk.Label(self, text=f"Available balance ${saving}", 
                                font=("Times New Roman", 8),
                                bg="lightgrey",
                                fg="grey",
                                anchor="e",  # east (right) alignment
                                width=33).place(x=190, y=103)


        
        #tk.Label(self, text="Amount", font = ("Times New Roman", 14), bg = "light gray", fg = "black").place(x=10,y=100)

        #self._amount_entry = tk.Entry(self, font = ("Times New Roman", 12))
        #self._amount_entry.pack(pady=5)

        self._result_label = tk.Label(self, text="", font=("Times New Roman", 12), bg="white", fg="white")
        self._result_label.place(x=10,y=170)

        tk.Button(self, text="Transfer", command=self._process_transfer,
                  bg="dark blue", fg="white", width=15).place(x=150,y=250)
        tk.Button(self, text="Close", command=self.destroy,
                  bg="white", fg="dark blue", width=15, relief="flat",borderwidth=0).place(x=10,y=250)
    
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
            ok_checkings = um.update_balance(self._user_id, "checking", -amount)
            if not ok_checkings:
                self._result_label.config(text="User not found or insufficient funds!", fg = "red")
                return
            #to add the amount to the savings
            ok_savings = um.update_balance(self._user_id, "savings", amount)
            if not ok_savings:
                self._result_label.config(text="Transfer failed!", fg = "red")
            
            check, saving = um.get_balances(self._user_id)
            self._checking_var.set(f"${check: .2f}")
            self._savings_var.set(f"${saving: .2f}")

            self._result_label.config(text = f"Transferred ${amount: .2f}", fg = "green")

        except ValueError:
            self._result_label.config(text="Invalid amount format.", fg="red")


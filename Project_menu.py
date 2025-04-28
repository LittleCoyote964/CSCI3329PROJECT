import tkinter as tk
import tkinter.font as tkFont
import Project_BankApp
#will work on menu for action user picks
#menu for whenever the user is able to log in, will be imported to the Project_main.py

def handle_accountdetails(user_id, checking, savings):
    account_window = tk.Toplevel()
    account_window.title("Account Details")
    account_window.geometry("400x300")
    account_window.configure(bg="gray")

    tk.Label(account_window, text="Account Details", font=("Times New Roman", 20), bg="gray", fg="white").pack(pady=10)

    tk.Label(account_window, text=f"Username: {user_id}", font=("Times New Roman", 14), bg="gray", fg="white").pack(pady=5)

    tk.Label(account_window, text=f"Checking Balance: ${checking:.2f}", font=("Times New Roman", 14), bg="gray", fg="white").pack(pady=5)

    tk.Label(account_window, text=f"Savings Balance: ${savings:.2f}", font=("Times New Roman", 14), bg="gray", fg="white").pack(pady=5)

    close_button = tk.Button(account_window, text="Close", command=account_window.destroy, bg="white", fg="black", width=15)
    close_button.pack(pady=20)

def handle_withdrawal(user_id, balance_var):
    withdrawal_window = tk.Toplevel()
    withdrawal_window.title("Withdraw")
    withdrawal_window.geometry("400x300")
    withdrawal_window.configure(bg="gray")

    tk.Label(withdrawal_window, text="Withdraw", font=("Times New Roman", 20), bg="gray", fg="white").pack(pady=10)
    tk.Label(withdrawal_window, text="Enter withdrawal amount:", font=("Times New Roman", 14), bg="gray", fg="white").pack(pady=5)

    withdrawal_entry = tk.Entry(withdrawal_window, font=("Times New Roman", 14))
    withdrawal_entry.pack(pady=5)

    result_label = tk.Label(withdrawal_window, text="", font=("Times New Roman", 12), bg="gray", fg="white")
    result_label.pack(pady=5)

    def process_withdrawal():
        amount = withdrawal_entry.get().strip()
        print(f"Raw input: '{amount}'")  # Debugging

        try:
            amount = float(amount.replace(",", ""))
            print(f"Converted amount: {amount}")  # Debugging

            if amount <= 0:
                result_label.config(text="Enter a valid positive amount!", fg="red")
                return

            updated_lines = []
            found_user = False

            with open("user_balance.txt", "r") as f:
                lines = f.readlines()

            for line in lines:
                parts = line.strip().split(", ")
                if len(parts) == 3 and parts[0] == user_id:
                    checking = float(parts[1])
                    savings = float(parts[2])
                    if amount > checking:
                        result_label.config(text="Insufficient funds!", fg="red")
                        return
                    new_checking = checking - amount
                    updated_lines.append(f"{user_id}, {new_checking:.2f}, {savings:.2f}\n")
                    found_user = True
                else:
                    updated_lines.append(line)

            if not found_user:
                result_label.config(text="User not found!", fg="red")
                return

            with open("user_balance.txt", "w") as f:
                f.writelines(updated_lines)

            balance_var.set(f"Checking: ${new_checking:.2f}")
            result_label.config(text=f"Withdrawal Successful: ${amount:.2f}", fg="green")

        except ValueError as e:
            print(f"ValueError: {e}")
            result_label.config(text="Invalid input! Enter a number.", fg="red")

    withdraw_button = tk.Button(withdrawal_window, text="Withdraw", command=process_withdrawal, bg="white", fg="black", width=15)
    withdraw_button.pack(pady=5)

    close_button = tk.Button(withdrawal_window, text="Close", command=withdrawal_window.destroy, bg="white", fg="black", width=15)
    close_button.pack(pady=20)


def handle_deposit(user_id, balance_var):
    deposit_window = tk.Toplevel()
    deposit_window.title("Deposit")
    deposit_window.geometry("400x300")
    deposit_window.configure(bg="gray")

    tk.Label(deposit_window, text="Deposit", font=("Times New Roman", 20), bg="gray", fg="white").pack(pady=10)
    tk.Label(deposit_window, text="Enter deposit amount:", font=("Times New Roman", 14), bg="gray", fg="white").pack(pady=5)

    deposit_entry = tk.Entry(deposit_window, font=("Times New Roman", 14))
    deposit_entry.pack(pady=5)

    result_label = tk.Label(deposit_window, text="", font=("Times New Roman", 12), bg="gray", fg="white")
    result_label.pack(pady=5)

    def process_deposit():
        amount = deposit_entry.get().strip()
        print(f"Raw input: '{amount}'")

        try:
            amount = float(amount.replace(",", ""))
            print(f"Converted amount: {amount}")

            if amount <= 0:
                result_label.config(text="Enter a valid positive amount!", fg="red")
                return

            updated_lines = []
            found_user = False

            with open("user_balance.txt", "r") as f:
                lines = f.readlines()

            for line in lines:
                parts = line.strip().split(", ")
                if len(parts) == 3 and parts[0] == user_id:
                    checking = float(parts[1])
                    savings = float(parts[2])
                    new_checking = checking + amount
                    updated_lines.append(f"{user_id}, {new_checking:.2f}, {savings:.2f}\n")
                    found_user = True
                else:
                    updated_lines.append(line)

            if not found_user:
                result_label.config(text="User not found!", fg="red")
                return

            with open("user_balance.txt", "w") as f:
                f.writelines(updated_lines)

            balance_var.set(f"Checking: ${new_checking:.2f}")
            result_label.config(text=f"Deposit Successful: ${amount:.2f}", fg="green")

        except ValueError as e:
            print(f"ValueError: {e}")
            result_label.config(text="Invalid input! Enter a number.", fg="red")

    deposit_button = tk.Button(deposit_window, text="Deposit", command=process_deposit, bg="white", fg="black", width=15)
    deposit_button.pack(pady=5)

    close_button = tk.Button(deposit_window, text="Close", command=deposit_window.destroy, bg="white", fg="black", width=15)
    close_button.pack(pady=20)


#will create a new button to transfer money from a their "checkings to a savings account"
def handle_transfer(user_id, balance_var, balance_var_savings):
    print('this is a test to make sure the transfer button works')
#continuing from the root window. 
def open_menu(w, user_id, balance,show_login_callback):
    def handle_logout():
        print("Testing, this is for logging the user out")
        menu.destroy()
        show_login_callback()

    menu = tk.Toplevel(w)
    menu.title("User menu")
    menu.configure(bg="Maroon")
    menu.geometry("600x600")

    # make StringVar for balance display
    balance_var_checking = tk.StringVar()
    balance_var_savings = tk.StringVar()

    balance_var_checking.set(f"Checking: ${balance[0]:.2f}")
    balance_var_savings.set(f"Savings: ${balance[1]:.2f}")

    # balance display label
    balance_label_checking = tk.Label(menu,
                                  textvariable=balance_var_checking,
                                  font=("Times New Roman", 14),
                                  bg="maroon",
                                  fg="white")
    balance_label_checking.place(x=200, y=100)

    balance_label_savings = tk.Label(menu,
                                 textvariable=balance_var_savings,
                                 font=("Times New Roman", 14),
                                 bg="maroon",
                                 fg="white")
    balance_label_savings.place(x=200, y=130)

    # menu header
    menuHeader = tk.Label(menu,
                          text="User Menu",
                          font=("Times New Roman", 30),
                          bg="maroon",
                          fg="white")
    menuHeader.place(x=200, y=50)

    # check balance button
    detailOpt = tk.Button(menu,
                          text="Check Balance",
                          width=23,
                          height=2,
                          bg="gray",
                          fg="black",
                          command=lambda: handle_accountdetails(user_id, balance[0], balance[1]))
    detailOpt.place(x=200, y=150)

    # withdrawal button
    withdrawal = tk.Button(menu,
                           text="Withdraw",
                           width=23,
                           height=2,
                           bg="gray",
                           fg="black",
                           command=lambda: handle_withdrawal(user_id, balance_var_checking))
    withdrawal.place(x=200, y=200)

    # deposit button
    deposit = tk.Button(menu,
                        text="Deposit",
                        width=23,
                        height=2,
                        bg="gray",
                        fg="black",
                        command=lambda: handle_deposit(user_id, balance_var_checking))
    deposit.place(x=200, y=250)

    transfer_to_savings = tk.Button(menu,
                                    text= "Transfer to Savings",
                                    width = 23,
                                    height = 2,
                                    bg = "gray",
                                    fg = "black",
                                    command=lambda: handle_transfer(user_id, balance_var_checking, balance_var_savings))
    transfer_to_savings.place(x = 200, y = 300)

    # logout button
    logOut = tk.Button(menu,
                       text="Log out user",
                       width=23,
                       height=2,
                       bg="gray",
                       fg="black",
                       command=handle_logout)
    logOut.place(x=200, y=350)

    



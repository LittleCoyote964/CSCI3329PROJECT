import tkinter as tk
import tkinter.font as tkFont
import Project_BankApp
#will work on menu for action user picks
#menu for whenever the user is able to log in, will be imported to the Project_main.py

def handle_accountdetails(user_id, balance):
    account_window = tk.Toplevel()
    account_window.title("Account Details")
    account_window.geometry("400x300")
    account_window.configure(bg="gray")

    tk.Label(account_window, text="Account Details", font=("Times New Roman", 20), bg="gray", fg="white").pack(pady=10)

    tk.Label(account_window, text=f"Username: {user_id}", font=("Times New Roman", 14), bg="gray", fg="white").pack(pady=5)

    tk.Label(account_window, text=f"Balance: {balance}", font=("Times New Roman", 14), bg="gray", fg="white").pack(pady=5)

    close_button = tk.Button(account_window, text="Close", command=account_window.destroy, bg="white", fg="black", width=15)
    close_button.pack(pady=20)

def handle_withdrawal(user_id, balance):
    def process_withdrawal():
        try:
            amount = float(amount_entry.get())
            if amount > balance:
                result_label.config(text="Insufficient funds.", fg="red")
            elif amount <= 0:
                result_label.config(text="Enter a valid amount.", fg="red")
            else:
                new_balance = balance - amount
                result_label.config(text=f"Withdrawal successful. New balance: ${new_balance:.2f}", fg="green")
                # You'd also update the user's balance in a file here if needed
        except ValueError:
            result_label.config(text="Please enter a number.", fg="red")

    account_window = tk.Toplevel()
    account_window.title("Withdrawal Request")
    account_window.geometry("400x300")
    account_window.configure(bg="gray")

    tk.Label(account_window, text="Withdrawal Request", font=("Times New Roman", 20), bg="gray", fg="white").pack(pady=10)
    tk.Label(account_window, text=f"Username: {user_id}", font=("Times New Roman", 14), bg="gray", fg="white").pack(pady=5)
    tk.Label(account_window, text=f"Balance: ${balance:.2f}", font=("Times New Roman", 14), bg="gray", fg="white").pack(pady=5)

    tk.Label(account_window, text="Amount to withdraw:", font=("Times New Roman", 14), bg="gray", fg="white").pack(pady=5)
    amount_entry = tk.Entry(account_window, font=("Times New Roman", 14))
    amount_entry.pack(pady=5)

    tk.Button(account_window, text="Withdraw", command=process_withdrawal, bg="white", fg="black", width=15).pack(pady=10)

    result_label = tk.Label(account_window, font=("Times New Roman", 12), bg="gray")
    result_label.pack()


def handle_deposit():
    print("Testing, this is for depositing money")



#continuing from the root window. 
def open_menu(w, user_id, balance):
    def handle_logout():
        print("Testing, this is for logging the user out")
        menu.destroy()
        Project_BankApp.show_login()

    menu = tk.Toplevel(w)
    menu.title("User menu")
    menu.configure(bg = "Maroon")
    menu.geometry("600x600")

    #fontStyle = tkFont.Font(family = "Times New Roman", size=18)

    #this is the header for the user menu window
    menuHeader = tk.Label(menu,
                          text="User Menu",
                          font = ("Times New Roman", 30) , 
                          bg = "maroon",
                          fg = "white")
    menuHeader.place(x = 200, y = 50)


#this button will be used to get the account details such as the balance
    detailOpt = tk.Button(menu,
                      text="Check Balance", 
                      width =23, 
                      height = 2, 
                      bg="gray", 
                      fg = "black", 
                      command=lambda: handle_accountdetails(user_id, balance)) # will have to edit this to where we are able to display the detail on the GUI
    detailOpt.place(x = 200, y = 150)


#these buttons will be used to withdraw and deposit fund
    withdrawal = tk.Button(menu,
                           text="Withdraw",
                           width = 23,
                           height = 2,
                           bg = "gray",
                           fg = "black",
                           command=lambda: handle_withdrawal(user_id, balance))
    withdrawal.place(x=200, y = 200)

    deposit = tk.Button(menu,
                        text = "Deposit",
                        width = 23,
                        height = 2,
                        bg = "gray",
                        fg = "black",
                        command=handle_deposit)
    deposit.place(x=200, y = 250)

#this button will be used to log out the user from their account
    logOut = tk.Button(menu,
                       text="Log out user",
                       width = 23,
                       height = 2,
                       bg = "gray",
                       fg = "black",
                       command = handle_logout)
    logOut.place(x=200, y =300)

    



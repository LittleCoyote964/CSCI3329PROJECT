import tkinter as tk
import tkinter.font as tkFont

#will work on menu for action user picks
#menu for whenever the user is able to log in, will be imported to the Project_main.py

def handle_accountdetails():
    print("Testing, will have to add account detail")

def handle_withdrawal():
    print("Testing, this button is to withdraw money")

def handle_deposit():
    print("Testing, this is for depositing money")

def handle_logout():
    print("Testing, this is for logging the user out")

#continuing from the root window. 
def open_menu(root):
    menu = tk.TopLevel(root)
    menu.title("User menu")
    menu.configure(bg = "Maroon")
    menu.geometry("600x600")

    #fontStyle = tkFont.Font(family = "Times New Roman", size=18)

    #this is the header for the user menu window
    menuHeader = tk.Label(text="User Menu",
                          font = ("Times New Roman", 20) , 
                          bg = "maroon",
                          fg = "white")
    menuHeader.place(x = 175, y = 50)


#this button will be used to get the account details such as the balance
    detailOpt = tk.Button(text="Check Balance", 
                      width =23, 
                      height = 2, 
                      bg="gray", 
                      fg = "black", 
                      command=handle_accountdetails) # will have to edit this to where we are able to display the detail on the GUI
    detailOpt.place(x = 200, y = 100)


#these buttons will be used to withdraw and deposit fund
    withdrawal = tk.Button(text="Withdraw",
                           width = 23,
                           height = 2,
                           bg = "gray",
                           fg = "black",
                           command=handle_withdrawal)
    withdrawal.place(x=200, y = 150)

    deposit = tk.Button(text = "Deposit",
                        width = 23,
                        height = 2,
                        bg = "gray",
                        fg = "black",
                        command=handle_deposit)
    deposit.place(x=200, y = 200)

#this button will be used to log out the user from their account
    logOut = tk.Button(text="Log out user",
                       width = 23,
                       height = 2,
                       bg = "gray",
                       fg = "black",
                       command = handle_logout)
    logOut.place(x=200, y =250)



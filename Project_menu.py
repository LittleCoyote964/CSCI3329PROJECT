import tkinter as tk
import tkinter.font as tkFont

#will work on menu for action user picks
#menu for whenever the user is able to log in, will be imported to the Project_main.py

#continuing from the root window. 
def open_menu(root):
    menu = tk.TopLevel(root)
    menu.title("User menu")
    menu.configure(bg = "Maroon")
    menu.geometry("600x600")

    fontStyle = tkFont.Font(family = "Times New Roman", size=18)

    menuHeader = tk.Label(text="User Menu",
                          font = "Times New Roman", size=20 )



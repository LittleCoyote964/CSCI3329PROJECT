import tkinter as tk
import tkinter.font as tkFont

#will have to add action from when the customer signs in
def handle_click():
    print("Test, still need to add action.")

w = tk.Tk() #init Tkinter framework
w.title("Bank Account Login")
w.configure(bg = "Maroon")
w.geometry("600x600")

#font style / we can change the font 
fontStyle = tkFont.Font(family="Times New Roman", size=20)

#header label
headerLabel = tk.Label(text="(Bank Name)", font=("Time New Romman", 30))
headerLabel.place(x=175, y = 50)

#label to have the user enter their username
userLabel = tk.Label(text="Username: ", font=fontStyle)
userLabel.place(x = 100, y = 150)

#user entry
userEntry = tk.Entry(fg="Maroon", width=10, font=("Times New Roman", 20))
userEntry.place(x=340,y=150)

#label to have the user enter their password
passLabel = tk.Label(text="Password:", font=fontStyle)
passLabel.place(x=100,y=250)

#user entry for their password
passEntry = tk.Entry(fg="Maroon", width=10, font=("Times New Roman", 20))
passEntry.place(x=340,y=250)

#log in button
logButton = tk.Button(text="Login", width =23, height = 2, bg="white", fg = "black", command=handle_click)
logButton.place(x=200, y = 350)
w.mainloop()
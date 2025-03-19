import tkinter as tk
import tkinter.font as tkFont

#will have to add action from when the customer signs in
def handle_login():
    print("Test, this is the login button.")

def handle_forgot():
    print("Test, this is for forgot password.")

def handle_newuser():
    print("Test, this is to create a new user.")

w = tk.Tk()
w.title("Bank Account Login")
w.configure(bg="Maroon")

win_width = 600
win_height = 600
w.geometry(f"{win_width}x{win_height}")

screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()

x_position = (screen_width // 2) - (win_width // 2)
y_position = (screen_height // 2) - (win_height // 2)

# Set the position
w.geometry(f"{win_width}x{win_height}+{x_position}+{y_position}")

#font style / we can change the font 
fontStyle = tkFont.Font(family="Times New Roman", size=20)

#header label
headerLabel = tk.Label(text="Bank of Project", #change name whenever
                       font=("Times New Romman", 30), 
                       bg="maroon",
                       fg="white")
headerLabel.place(x=175, y = 50)

#label to have the user enter their username
userLabel = tk.Label(text="Username: ", 
                     font=fontStyle,
                     bg="maroon",
                     fg="white")
userLabel.place(x = 100, y = 150)

#user entry
userEntry = tk.Entry(fg="White", width=10, font=("Times New Roman", 20))
userEntry.place(x=340,y=150)

#label to have the user enter their password
passLabel = tk.Label(text="Password:",
                      font=fontStyle,
                      bg="maroon",
                      fg="white")
passLabel.place(x=100,y=250)

#user entry for their password
passEntry = tk.Entry(fg="White", 
                     width=10, 
                     font=("Times New Roman", 20),
                     show="*")#Hides the user input
passEntry.place(x=340,y=250)

#log in button
logButton = tk.Button(text="Login", 
                      width =23, 
                      height = 2, 
                      bg="gray", 
                      fg = "black", 
                      command=handle_login)
logButton.place(x=200, y = 350)

#forgot password button
forpassButt = tk.Button(text="Forgot Password?",
                        width=23, 
                        height=2, 
                        bg="gray",
                        fg="black",
                        command = handle_forgot)
forpassButt.place(x=200, y=400)

#create new user
newButton = tk.Button(text="Create new user",
                      width = 23,
                      height = 2,
                      bg = "gray",
                      fg = "black",
                      command = handle_newuser)
newButton.place(x = 200,y=450)
w.mainloop()
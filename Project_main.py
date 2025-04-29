import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import Project_menu
from forgot_password import forgot_password_window
from new_user import new_user_window

#will have to add action from when the customer signs in
def main(): 
    def handle_login():
        print("Test, this is the login button.")     
        id = userEntry.get()
        pssw = passEntry.get()
        f = open("user.txt", "r")
        idlist = f.readlines()#list
        idexist = False
        for b in range(len(idlist)):
            if idlist[b] == str(f"{id}\n"):
                idexist = True 
        f.close()
        f = open("pass.txt", "r")
        psswlist = f.readlines()
        f.close()
        psswexist = False
        for b in range(len(psswlist)):
            if psswlist[b] == str(f"{pssw}\n"):
                psswexist = True 
        if idexist and psswexist:
                w.destroy()
                Project_menu.open_menu() # this is to connect the use menu

        else:
            print("ID or Password is incorrect!") # need to make this part of the GUI
            fontS = tkFont.Font(family="Times New Roman", size=8)

            incorrectLabel = tk.Label(text="Password or Username is incorrect. Please try again.", 
                        font=fontS,
                        bg="white",
                        fg="red")
            incorrectLabel.place(x=10,y=327)

    def handle_forgot():
        print("Test, this is for forgot password.")

    def handle_newuser():
        print("Test, this is to create a new user.")

    w = tk.Tk()
    w.title("Bank Account Login")
    w.configure(bg="white")

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
    fontStyle = tkFont.Font(family="", size=18)


    # Load the image
    logo_image = Image.open("logo.png")  
    logo_image = logo_image.resize((250, 120))  # Resize as needed
    logo_photo = ImageTk.PhotoImage(logo_image)

    # Create label with image
    headerLabel = tk.Label(w, image=logo_photo, bg="white")
    headerLabel.image = logo_photo  # Keep a reference to avoid garbage collection
    headerLabel.place(x=25, y=20)

 # filler3 label
    filler3Label = tk.Label(
    text="Bank of America deposit products:\nUTRGV UTRGV-insured - Backed by the full faith and credit of the RGV community",
    font=("Times New Roman", 10),
    bg="light grey",
    fg="grey",
    padx=10,
    anchor="center",      # <--- center text inside label
    justify="center"      # <--- if multiline, center each line
)
    filler3Label.pack(fill='x', pady=(0, 0))  # <--- removes any space at the top

    # filler1 label
    filler1Label = tk.Label(w, text="Log In to Online Banking", font=("Times New Roman", 20), bg="red",fg="white",anchor='w',padx=10)      # <-- little padding from the left edge
    filler1Label.pack(fill='x', pady=(70, 0))

    # filler2 label
    filler2Label = tk.Label(text="Log In", font=("Times New Roman", 15), bg="white",fg="grey")      # <-- little padding from the left edge
    filler2Label.place(x =300, y=70)

 

    # Load the image for filler3
    filler_image = Image.open("Screenshot (283).png")  
    filler_image = filler_image.resize((350, 250))  # Resize as needed
    filler_photo = ImageTk.PhotoImage(filler_image)

    # Create label with image
    fillerLabel = tk.Label(w, image=filler_photo, bg="white")
    fillerLabel.image = logo_photo  # Keep a reference to avoid garbage collection
    fillerLabel.place(x=255, y=150)



    #label to have the user enter their username
    userLabel = tk.Label(text="User ID ", 
                        font=fontStyle,
                        bg="white",
                        fg="black")
    userLabel.place(x = 10, y = 160)

    #user entry
    userEntry = tk.Entry(fg="maroon", bg="white",width=20, font=("Times New Roman", 15))
    userEntry.place(x=10,y=200)

    #label to have the user enter their password
    passLabel = tk.Label(text="Password",
                        font=fontStyle,
                        bg="white",
                        fg="black")
    passLabel.place(x=10,y=260)

    #user entry for their password
    passEntry = tk.Entry(fg="maroon", 
                        width=20, 
                        font=("Times New Roman", 15),
                        show="*")#Hides the user input
    passEntry.place(x=10,y=300)



    #log in button
    logButton = tk.Button(text="Login", 
                        width =23, 
                        height = 2, 
                        bg="dark blue", 
                        fg = "white", 
                        command=handle_login)
    logButton.place(x=10, y = 400)

    #forgot password button
    forpassButt = tk.Button(w, text="Forgot your Password?",
                            width=23, 
                            height=1, 
                            bg="white",
                            fg="dark blue",
                            borderwidth=0,
                            relief="flat",
                            anchor='w',
                            command = lambda: forgot_password_window(w))
    forpassButt.place(x=10, y=350)

    #create new user
    newButton = tk.Button(text="Create new user",
                        width = 23,
                        height = 2,
                        bg = "dark blue",
                        fg = "white",
                        command = lambda: new_user_window(w))
    newButton.place(x = 10,y=450)
    w.mainloop()

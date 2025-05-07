import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from new_user import NewUserDialog
from forgot_password import ForgotPasswordDialog
from user_manager import UserManager


class BankApp:
    def __init__(self, master):
        self.master = master
        self.incorrect_label = None
        self.user_manager = UserManager()
        self.master.title("Bank Account Login")
        self.master.configure(bg="white")
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
    #font style / we can change the font 
        fontStyle = tkFont.Font(family="", size=18)


        # Load the image
        logo_image = Image.open("logo1.png")  
        logo_image = logo_image.resize((80, 80))  # Resize as needed
        logo_photo = ImageTk.PhotoImage(logo_image)

        # Create label with image
        headerLabel = tk.Label(image=logo_photo, bg="white")
        headerLabel.image = logo_photo  # Keep a reference to avoid garbage collection
        headerLabel.place(x=10, y=30)

        tk.Label(text="Bank of Project", font=("Times New Roman", 20), bg="white",fg="grey").place(x =100, y=50)

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
        filler1Label = tk.Label( text="Log In to Online Banking", font=("Times New Roman", 20), bg="red",fg="white",anchor='w',padx=10)      # <-- little padding from the left edge
        filler1Label.pack(fill='x', pady=(70, 0))

        # filler2 label
        filler2Label = tk.Label(text="Log In", font=("Times New Roman", 15), bg="white",fg="grey")      # <-- little padding from the left edge
        filler2Label.place(x =300, y=55)

    

        # Load the image for filler3
        filler_image = Image.open("filler.png")  
        filler_image = filler_image.resize((350, 350))  # Resize as needed
        filler_photo = ImageTk.PhotoImage(filler_image)

        # Create label with image
        fillerLabel = tk.Label( image=filler_photo, bg="white")
        fillerLabel.image = filler_photo  # Keep a reference to avoid garbage collection
        fillerLabel.place(x=245, y=150)



        #label to have the user enter their username
        userLabel = tk.Label(text="User ID ", 
                            font=fontStyle,
                            bg="white",
                            fg="black")
        userLabel.place(x = 10, y = 160)

        #user entry
        self.user_entry = tk.Entry(fg="black", bg="white",width=20, font=("Times New Roman", 15))
        self.user_entry.place(x=10,y=200)

        #label to have the user enter their password
        passLabel = tk.Label(text="Password",
                            font=fontStyle,
                            bg="white",
                            fg="black")
        passLabel.place(x=10,y=260)

        #user entry for their password
        self.pass_entry = tk.Entry(fg="black",
                            bg="white", 
                            width=20, 
                            font=("Times New Roman", 15),
                            show="*")#Hides the user input
        self.pass_entry.place(x=10,y=300)




        
        # buttons
        tk.Button(self.master, text="Login", width=23, height=2, bg="dark blue", fg="white",
                  command=self._handle_login).place(x=10, y=400)

        tk.Button(self.master, text="Forgot Password?", width=23, height=2, bg="white", fg="dark blue", relief="flat", borderwidth=0,anchor='w',
                  command=lambda: ForgotPasswordDialog(self.master)).place(x=10, y=350)

        tk.Button(self.master, text="Create New User", width=23, height=2, bg="dark blue", fg="white",
                  command=lambda: NewUserDialog(self.master)).place(x=10, y=450)

    def _handle_login(self):
        # reload users before checking credentials
        self.user_manager.reload_users()

        username = self.user_entry.get().strip()
        password = self.pass_entry.get().strip()

        print(f"Login attempt for: {username}")  # debug
        print(f"Existing users: {self.user_manager._users.keys()}")  # debug

        if self.incorrect_label:
            self.incorrect_label.destroy()
            self.incorrect_label = None

        if self.user_manager.authenticate(username, password):
            print("Authentication successful")  # debug
            balances = self.user_manager.get_balances(username)
            if balances:
                self.master.withdraw()
                from Project_menu import UserMenu
                UserMenu(self.master, username, balances, self._show_login)
        else:
            print("ID or Password is incorrect!") # need to make this part of the GUI
            fontS = tkFont.Font(family="Times New Roman", size=8)

            self.incorrect_label = tk.Label(text="Password or Username is incorrect. Please try again.", 
                        font=fontS,
                        bg="white",
                        fg="red")
            self.incorrect_label.place(x=10,y=327)
    def _show_login(self):
        self.user_entry.delete(0, tk.END)
        self.pass_entry.delete(0, tk.END)
        self.master.deiconify()

        if self.incorrect_label:
            self.incorrect_label.destroy()
            self.incorrect_label = None



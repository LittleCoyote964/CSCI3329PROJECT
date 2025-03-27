import tkinter as tk
import tkinter.font as tkFont
from forgot_password import forgot_password_window
from new_user import new_user_window

class BankApp:
    def __init__(self, master): #using master to have the "parent window"
        self.master = master # to keep the main window
        self.master.title("Bank account Login")
        self.master.configure(bg = "maroon")

        #window dimensions
        self.win_width = 600
        self.win_height = 600
        self.master.geometry(f"{self.win_width}x{self.win_height}")
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x_position = (screen_width // 2) - (self.win_width // 2)
        y_position = (screen_height // 2) - (self.win_height // 2)
        self.master.geometry(f"{self.win_width}x{self.win_height}+{x_position}+{y_position}")

        self.fontStyle = tkFont.Font(family="Times New Roman", size=20)

        self.setup_login() # to start the set up for the UI

    def setup_login(self):
        #for header label**
        self.headerLabel = tk.Label(text="Bank of Project", #change name whenever
                            font=("Times New Roman", 30), 
                            bg="maroon",
                            fg="white")
        self.headerLabel.place(x=175, y = 50)

        #username label**
        self.userLabel = tk.Label(text="Username: ", 
                            font=("Times New Roman", 20),
                            bg="maroon",
                            fg="white")
        self.userLabel.place(x = 100, y = 150)

        #username entry**
        self.userEntry = tk.Entry(fg="maroon",
                                bg="white",
                                width=10,
                                font=("Times New Roman", 20))
        self.userEntry.place(x=340,y=150)

        #password label**
        self.passLabel = tk.Label(text="Password:",
                            font=("Times New Roman", 20),
                            bg="maroon",
                            fg="white")
        self.passLabel.place(x=100,y=250)

        #password entry
        self.passEntry = tk.Entry(fg="maroon", 
                            width=10, 
                            font=("Times New Roman", 20),
                            show="*")#Hides the user input
        self.passEntry.place(x=340,y=250)

        #log in button
        self.logButton = tk.Button(text="Login", 
                            width =23, 
                            height = 2, 
                            bg="gray", 
                            fg = "black", 
                            command=self.handle_login)
        self.logButton.place(x=200, y = 350)

        #forgot password button
        self.forpassButt = tk.Button(text="Forgot Password?",
                                width=23, 
                                height=2, 
                                bg="gray",
                                fg="black",
                                command = lambda: forgot_password_window(self.master))
        self.forpassButt.place(x=200, y=400)

        #create new user
        self.newButton = tk.Button(text="Create new user",
                            width = 23,
                            height = 2,
                            bg = "gray",
                            fg = "black",
                            command = lambda: new_user_window(self.master))
        self.newButton.place(x = 200,y=450)

    def handle_login(self):
        print("Testing login button.")
        print("Test, this is the login button.") 

        user_id = self.userEntry.get()
        pssw = self.passEntry.get()

        f = open("user.txt", "r")
        idlist = f.readlines()#list
        idexist = False
        for b in range(len(idlist)):
            if idlist[b] == str(f"{user_id}\n"):
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
                self.master.withdraw()
                import Project_menu
                Project_menu.open_menu(self.master, user_id, balance= 0.00) # this is to connect the use menu
        else:
            print("ID or Password is incorrect!") # need to make this part of the GUI
            fontS = tkFont.Font(family="Times New Roman", size=10)

            self.incorrectLabel = tk.Label(text="Password or Username is incorrect. Please try again.", 
                        font=fontS,
                        bg="maroon",
                        fg="red")
            self.incorrectLabel.pack(pady=290)

    def show_login(self):
        self.master.deiconify() # so the window redisplays. 

if __name__ == "__main__":
    root = tk.Tk()     
    app = BankApp(root)
    root.mainloop()
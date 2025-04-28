import tkinter as tk

def new_user_window(parent_window):
    new_user = tk.Toplevel(parent_window)
    new_user.title("Create New User")
    new_user.geometry("400x300")
    new_user.configure(bg="gray")
    
    tk.Label(new_user, text="Create Username and Password", font=("Times New Roman", 20), bg="gray", fg="white").pack(pady=10)

    tk.Label(new_user, text="Enter username: ", font=("Times New Roman", 14), bg="gray", fg="white").pack()

    user_entry = tk.Entry(new_user, width=30)
    user_entry.pack(pady=5)

    tk.Label(new_user, text="Enter password: ", font=("Times New Roman", 14), bg="gray", fg="white").pack()

    pass_entry = tk.Entry(new_user, width=30, show='*')
    pass_entry.pack(pady=5)

    def submit_user():
        username = user_entry.get().strip() 
        password = pass_entry.get().strip()
        
        if not username or not password:
            print("Please enter a valid username and password.")
            return
        
        with open("user.txt", "r") as user_file:
            existing_users = [line.strip() for line in user_file.readlines()]
        
        if username in existing_users:
            print(f"Username '{username}' already exists. Please choose a different username.")
            return
        
        with open("user.txt", "a") as user_file:
            user_file.write(username + "\n")
        
        with open("pass.txt", "a") as pass_file:
            pass_file.write(password + "\n")

        with open("user_balance.txt", "a+") as balance_file:
            balance_file.seek(0, 2)  # move to the end of the file
            if balance_file.tell() > 0:
                balance_file.write("\n")
            balance_file.write(f"{username}, 0.00, 0.00")

        print(f"New user '{username}' created successfully!")
        new_user.destroy()

    submit_button = tk.Button(new_user, text="Submit", command=submit_user, bg="white", fg="black", width=15)
    submit_button.pack(pady=20)


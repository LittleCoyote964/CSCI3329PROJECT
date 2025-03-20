import tkinter as tk

def forgot_password_window(parent_window):
    forgot_window = tk.Toplevel(parent_window)
    forgot_window.title("Forgot Password")
    forgot_window.geometry("400x300")
    forgot_window.configure(bg="gray")

    tk.Label(forgot_window, text="Reset Password", font=("Times New Roman", 20), bg="gray", fg="white").pack(pady=10)

    tk.Label(forgot_window, text = "Enter your username: ", font=("Times New Roman", 14), bg="gray", fg="white").pack()

    user_entry = tk.Entry(forgot_window, width=30)
    user_entry.pack(pady=5)

    def reset_password():
        username = user_entry.get().strip()
        if username == "":
            print("Please enter a valid username.")
            return
        
        print(f"Password reset sent to {username}")
        forgot_window.destroy()

    reset_button = tk.Button(forgot_window, text="Submit", command=reset_password, bg="white", fg="black", width=15)
    reset_button.pack(pady=20)
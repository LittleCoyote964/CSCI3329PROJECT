import tkinter as tk
from Project_BankApp import BankApp

def start_app():
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()

if __name__ == "__main__":
    start_app()
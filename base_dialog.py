import tkinter as tk

class BaseDialog(tk.Toplevel):
    def __init__(self, parent, title, width=400, height=300, bg_color="gray"):
        super().__init__(parent)
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.configure(bg=bg_color)
        self.resizable(False, False)
        self._center_window()
        self._setup_ui()

    def _center_window(self):
        # center the window on the screen
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (self.winfo_width() // 2)
        y = (screen_height // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")

    def _setup_ui(self):
        # override this in child classes to add widgets
        pass
from tkinter import *

class BaseGUI:
    def __init__(self, parent: Tk, width: float, height: float):
        self.parent = parent
        self.center_window(width, height)  
        
    def center_window(self, width: float, height: float):
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.parent.geometry(f"{width}x{height}+{x}+{y}")

    def run(self):
        self.parent.mainloop()

    def destroy(self):
        self.parent.destroy()
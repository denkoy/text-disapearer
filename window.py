from tkinter import *
from buttons import Buttons
class Window:
    def __init__(self):
        self.window = Tk()
        self.window.title("Disappearing text")
        self.window.geometry("500x600")
        self.window.config(bg="white")

        self.button=Buttons()
        self.window.mainloop()

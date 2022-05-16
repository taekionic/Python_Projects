from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox
import shutil
import os
import time

import programcontrol
import programgui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(675, 500)
        self.master.maxsize(675, 500)

        programcontrol.center_window(self, 550, 400)
        self.master.title("File Checker")
        self.master.configure(bg="lightgray")
        self.master.protocol("WM_DELETE_WINDOW", lambda: programcontrol.ask_quit(self))
        arg = self.master

        programgui.startprogram(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
    
    

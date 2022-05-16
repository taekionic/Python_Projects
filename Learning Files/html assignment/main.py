from tkinter import *
import tkinter as tk
from tkinter import messagebox

import pagecontrol
import page_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(550, 400)
        self.master.maxsize(550,400)

        pagecontrol.center_window(self, 550, 400)
        self.master.title("Page Creator")
        self.master.configure(bg="lightgray")
        self.master.protocol("WM_DELETE_WINDOW", lambda: pagecontrol.ask_quit(self))
        arg = self.master

        page_gui.startprogram(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

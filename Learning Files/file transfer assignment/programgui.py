import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import shutil
import os
import time

import main
import programcontrol


def startprogram(self):
    self.lbl_welcome = tk.Label(self.master, text = "Directory Updater")
    self.lbl_welcome.grid(row = 0, column = 1, padx=(0,140), pady = (50,0))

    self.btn_source = tk.Button(self.master, text="Source Directory", command=lambda: programcontrol.sourcedirectory(self), width=17)
    self.btn_source.grid(row = 1, column = 0, sticky = N, padx = (30,30), pady = (30,0))

    self.sourcedir = tk.Entry(self.master, width = 75)
    self.sourcedir.grid(row = 1, column = 1, rowspan = 2, sticky = N+E, pady = (30,0))

    self.btn_Destination = tk.Button(self.master, text="Destination Directory", command=lambda: programcontrol.destdirectory(self), width=17)
    self.btn_Destination.grid( row = 2, column = 0, sticky = N, pady = (30,0))

    self.destdir = tk.Entry(self.master, width = 75)
    self.destdir.grid(row= 2, column = 1, rowspan = 2, sticky = N+E, pady = (30,0))

    self.dirlist = tk.Listbox(self.master, width = 92, selectmode="multiple")
    self.dirlist.grid(row = 3, column = 0, rowspan = 4, columnspan = 6, pady = (30,0), padx = (30,0))

    self.btn_Update = tk.Button(self.master, text = "Update Directory", width = 17, command=lambda: programcontrol.update(self))
    self.btn_Update.grid(row = 7, column = 1, sticky = E, pady = (30,0))

    self.btn_Check = tk.Button(self.master, text = "Check Directory", width = 17, command=lambda: programcontrol.check(self))
    self.btn_Check.grid(row = 7, column = 1, sticky = W, padx = (30,0), pady = (30,0))

    self.btn_movesel = tk.Button(self.master, text = "Move Selected Files", width = 17, command=lambda: programcontrol.move(self))
    self.btn_movesel.grid(row = 7, column = 1, sticky = W, padx = (175,0), pady = (30,0))








    


    







if __name__ == "__main__":
    pass
import shutil
import os
import time

from tkinter import *
import tkinter as tk
from tkinter import messagebox

import programgui
import main

Seconds_In_Day = 24 * 60 * 60
now = time.time()
before = now - Seconds_In_Day


def last_mod_time(files): #function to return modification time of file
    return os.path.getmtime(files)


def center_window(self, w, h): #centering window
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2)-(w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

#function to open directory search to allow user path selection for source and destination
def sourcedirectory(self): 
    self.sourcedir.delete(0,END)
    dir = tk.filedialog.askdirectory()
    self.sourcedir.insert(0, dir)


def destdirectory(self):
    self.destdir.delete(0,END)
    dir = tk.filedialog.askdirectory()
    self.destdir.insert(0, dir)

#function to retrieve files that have been modified in the last 24 hours and automatically move them to selected destination

def update(self):
    src = self.sourcedir.get()
    dst = self.destdir.get()
    for files in os.listdir(src):
        srcfiles = os.path.join(src, files)
        if last_mod_time(srcfiles) > before:
            self.dirlist.insert(0, files)
            dstfiles = os.path.join(dst, files)
            shutil.move(srcfiles, dstfiles)

#function to check for modified files in the list directory and print the output to the listbox

def check(self):
    src = self.sourcedir.get()
    for files in os.listdir(src):
        srcfiles = os.path.join(src, files)
        if last_mod_time(srcfiles) > before:
            self.dirlist.insert(0, files)

#function to move items selected in listbox and move them to the destination folder. NOT FUNCTIONAL YET.

def move(self):
    src = self.sourcedir.get()
    dst = self.destdir.get()
    sel = self.dirlist.curselection()
    for files in os.listdir(src):
        srcfiles = os.path.join(src, files)
        for i in sel:
            dstfiles = os.path.join(dst, sel)
            shutil.move(srcfiles,dstfiles)
    
    

    


def ask_quit(self):
    if messagebox.askokcancel("Exit program","Are you sure you would like to exit?"):
        self.master.destroy()
        os._exit(0)







if __name__ == "__main__":
    pass
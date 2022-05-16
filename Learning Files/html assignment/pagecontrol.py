import webbrowser
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os

def html(self):
    var_pagetext = str(self.txt_create.get())
    var_title = str(self.txt_title.get())
    with open("project.html", "w") as f:
        f.write("\
            <html>\
                <head>\
                    <title>"f"{var_title}" "</title>\
                </head>\
                <body>\
                    <h1>"\
                    + f"{var_pagetext}" \
                    "</h1>\
                </body>\
            </html>")
    webbrowser.open_new('project.html')



def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2)-(w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program","Are you sure you would like to exit?"):
        self.master.destroy()
        os._exit(0)





if __name__ == "__main__":
    pass

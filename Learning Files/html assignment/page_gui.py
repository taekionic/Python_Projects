from tkinter import *
import tkinter as tk


import pagecontrol
import main




def startprogram(self):
    """self.position1 = tk.Label(self.master, text='', bg='lightgray')
    self.position1.grid(row=0,column=0)"""
    #thank you message
    self.lbl_welcome = tk.Label(self.master, text="Thanks for using my program!")
    self.lbl_welcome.grid(row=0, column=1, pady=(25,0))
    #page title label and entry
    self.lbl_title = tk.Label(self.master, text="Enter Page Title")
    self.lbl_title.grid(row=1, column = 1, pady=(25,0))
    self.txt_title = tk.Entry(self.master, text='')
    self.txt_title.grid(row=1, column = 1, rowspan=2, pady=(10,0))

    self.lbl_color = tk.Label(self.master, text="Please select background color")
    self.lbl_color.grid(row=2, column = 1, pady=(50,0))
    self.lbl_color1 = tk.Label(self.master, text="Feature coming soon!")
    self.lbl_color1.grid(row=3, column=1)
    #page text
    self.lbl_create = tk.Label(self.master, text = "Enter page text")
    self.lbl_create.grid(row=4, column=1, pady=(25,0))
    self.txt_create = tk.Entry(self.master, text='', width=25)
    self.txt_create.grid(row=4, column=1, pady=(25,0))

    self.btn_submit = tk.Button(self.master, width=15, height=1,text="submit", command=lambda: pagecontrol.html(self))
    self.btn_submit.grid(row=5, column=1, pady=(25,0))
    
    """self.position1 = tk.Label(self.master, text='', bg='lightgray')
    self.position1.grid(row=3,column=2)"""



if __name__ == "__main__":
    pass
    

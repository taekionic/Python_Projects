import tkinter
from tkinter import *



class ParentWindow(Frame): 
    def __init__(self,master):
        Frame.__init__(self)


        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry(f'{700}x{400}')
        self.master.title('Learning TKinter')
        self.master.config(bg='darkgray')

        self.varfName = StringVar()
        self.varlName = StringVar()

        self.lblfName = Label(self.master,text='First Name: ', font=("Helvetica", 16), fg='black', bg='darkgray')
        self.lblfName.grid(row=0,column=0, padx=(30,0), pady=(30,0))

        self.lbllName = Label(self.master,text='Last Name: ', font=("Helvetica", 16), fg='black', bg='darkgray')
        self.lbllName.grid(row=1,column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='darkgray')
        self.lblDisplay.grid(row=3,column=1, padx=(30,0), pady=(30,0))

        self.txtfName = Entry(self.master, text=self.varfName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtfName.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.txtlName = Entry(self.master, text=self.varlName, font=("Helvetica", 16), fg='black', bg='lightblue' )
        self.txtlName.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, command=self.submit)
        self.btnSubmit.grid(row=2,column=1,padx=(0,0),pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, command=self.cancel )
        self.btnCancel.grid(row=2,column=1,padx=(0,90),pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varfName.get()
        ln = self.varlName.get()
        self.lblDisplay.config(text=f"Hello {fn} {ln}!")

    def cancel(self):
        self.master.destroy()





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

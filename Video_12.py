from tkinter import *
from tkinter.messagebox import *

class Window:
    def __init__(self, root):
        self.b1 = Button(root, text="Info", font=20, command=lambda:showinfo("ShowInfo", "Informacia"))
        self.b1.grid(row=0, column=0, sticky=W+E)
        self.b2 = Button(root, text="Warning", font=20, command=lambda:showwarning("ShowWarning", "Zgushaceq"))
        self.b2.grid(row=1, column=0, sticky=W+E)
        self.b3 = Button(root, text="Error", font=20, command=lambda:showerror("ShowError", "Sxalmunq"))
        self.b3.grid(row=2, column=0, sticky=W+E)


root = Tk()
obj = Window(root)
root.mainloop()
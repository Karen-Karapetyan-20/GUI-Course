from tkinter import *


class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("grid")
        self.l1 = Label(self.root, text="Login")
        self.l2 = Label(self.root, text="Password")
        self.e1 = Entry(self.root)
        self.e2 = Entry(self.root)
        self.l1.grid(row=0, column=0, sticky=E)
        self.l2.grid(row=1, column=0)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.c = Checkbutton(self.root, text="Mnal hamakargum")
        self.c.grid(columnspan=2)


root = Tk()
obj = Window(root)
root.mainloop()

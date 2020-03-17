from tkinter import *


class Window:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="black")
        self.f1 = Frame(self.root, width=250, height=125, bg="white")
        self.f2 = Frame(self.root, width=250, height=125, bg="white")
        self.f3 = Frame(self.root, width=250, height=125, bg="white")

        self.f1.grid(row=0, column=0)
        self.f2.grid(row=0, column=1, padx=1)
        self.f3.grid(row=0, column=2)
        self.root.bind("<Button-1>", self.left_click)
        self.root.bind("<Button-2>", self.middle_click)
        self.root.bind("<Button-3>", self.right_click)

    def left_click(self, event):
        self.f1.configure(bg="red")
        self.f2.configure(bg="white")
        self.f3.configure(bg="white")

    def middle_click(self, event):
        self.f1.configure(bg="white")
        self.f2.configure(bg="red")
        self.f3.configure(bg="white")

    def right_click(self, event):
        self.f1.configure(bg="white")
        self.f2.configure(bg="white")
        self.f3.configure(bg="red")


root = Tk()
obj = Window(root)
root.mainloop()

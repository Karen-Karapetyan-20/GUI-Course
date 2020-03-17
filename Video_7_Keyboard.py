from tkinter import *


class Window:
    def __init__(self, root):
        self.root = root
        self.l1 = Label(root, width=12, font=("Ubuntu", 100))
        self.l1.pack()

        self.l1.bind("a", self.print_char)

        self.root.bind("Shift-Up", self.print_su)
        self.root.bind("Control-Down", self.print_cd)

        for i in range(65, 123):
            self.root.bind(chr(i), self.print_char)

    def print_char(self, event):
        self.l1.configure(text=event.char)

    def print_su(self, event):
        self.l1.configure(text="Shift Up")

    def print_cd(self, event):
        self.l1.configure(text="Control Down")


root = Tk()
obj = Window(root)
root.mainloop()

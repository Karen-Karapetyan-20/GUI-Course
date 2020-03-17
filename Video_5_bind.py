from tkinter import *


class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Qani tarekan es ???")
        self.e = Entry(self.root, width=5, font=15)
        self.b = Button(self.root, text="Stugel")
        self.l = Label(self.root, width=27, font=15)
        self.e.grid(row=0, column=0)
        self.b.grid(row=1, column=0)
        self.l.grid(row=2, column=0)
        self.b.bind("<Button-1>", self.output)

    def output(self, event):
        self.txt = self.e.get()
        try:
            if int(self.txt) < 18:
                self.l["text"] = "It's early"
            else:
                self.l["text"] = "Welcome"
        except Exception:
            self.l["text"] = "Error !!!"


root = Tk()
obj = Window(root)
root.mainloop()

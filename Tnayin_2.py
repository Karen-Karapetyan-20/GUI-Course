from tkinter import *


class Tnayin_2:
    def __init__(self, root):
        self.root = root
        self.root.config(bg="black")
        self.root.geometry("700x500")
        self.d = {
            "կարմիր": "red",
            "կապույտ": "blue",
            "կանաչ": "green",
            "դեղին": "yellow",
            "մանուշակագույն": "purple"
        }
        self.t = Text(self.root, width="20", height="5", font="30")
        self.l1 = Label(self.root, text="Label_1", bg="white", fg="black", width="10", height="5")
        self.l2 = Label(self.root, text="Label_2", bg="white", fg="black", width="10", height="5")
        self.l3 = Label(self.root, text="Label_3", bg="white", fg="black", width="10", height="5")
        self.l4 = Label(self.root, text="Label_4", bg="white", fg="black", width="10", height="5")
        self.y = StringVar()
        self.b = Button(self.root, text="Sexmel", bg="white", fg="black", width="10", height="5", command=self.fun)
        self.t.pack()
        self.b.pack()
        self.l1.pack()
        self.l2.pack()
        self.l3.pack()
        self.l4.pack()

    def fun(self):
        self.x = self.t.get()
        self.x = self.x.split(", ")
        if self.x[0] == "l1":
            self.l1.config(bg=self.d[self.x[1]])
        elif self.x[0] == "l2":
            self.l2.config(bg=self.d[self.x[1]])
        elif self.x[0] == "l3":
            self.l3.config(bg=self.d[self.x[1]])
        elif self.x[0] == "l4":
            self.l4.config(bg=self.d[self.x[1]])
        elif self.x[1] not in self.d.keys():
            self.y.set("Tenc guyn chka dict_i mej")


root = Tk()
obj = Tnayin_2(root)
mainloop()

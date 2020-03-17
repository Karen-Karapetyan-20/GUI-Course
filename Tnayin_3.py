from tkinter import *


class Tnayin_3:
    def __init__(self, root):
        self.root = root
        self.root.title("Tnayin_3")
        self.root.geometry("600x400")
        self.f = Frame(root, width=300, height=150)
        self.e = Entry(self.f, width=20)
        self.t = Text(self.f, width=50, height=25)
        self.scroll = Scrollbar(self.f, command=self.t.yview)
        self.t.configure(yscrollcommand=self.scroll.set)
        self.var1 = BooleanVar()
        self.var1.set(1)
        self.rb1 = Radiobutton(self.f, variabl=self.var1, value=0, text="black", width=5, height=2)
        self.rb2 = Radiobutton(self.f, variabl=self.var1, value=1, text="white", width=5, height=2)
        self.rb3 = Radiobutton(self.f, variabl=self.var1, value=0, text="red", width=5, height=2)
        self.rb4 = Radiobutton(self.f, variabl=self.var1, value=1, text="green", width=5, height=2)
        self.rb5 = Radiobutton(self.f, variabl=self.var1, value=0, text="yellow", width=5, height=2)
        self.rb6 = Radiobutton(self.f, variabl=self.var1, value=1, text="purple", width=5, height=2)
        self.f_bg = Button(self.f, text="Change", width=6, height=2, font=5, command=self.R_BG)
        self.b1 = Button(self.f, text="Save", width=6, height=2, font=15, command=self.Save)
        self.b2 = Button(self.f, text="Open", width=6, height=2, font=15, command=self.Open)
        self.f.pack(side=LEFT)
        self.e.pack(anchor=NW, fill=X)
        self.t.pack(side=LEFT)
        self.scroll.pack(side=LEFT, fill=Y)
        self.b1.pack(anchor=NW)
        self.b2.pack(anchor=SW)
        self.rb1.pack(side=BOTTOM)
        self.rb2.pack(side=BOTTOM)
        self.rb3.pack(side=BOTTOM)
        self.rb4.pack(side=BOTTOM)
        self.rb5.pack(side=BOTTOM)
        self.rb6.pack(side=BOTTOM)
        self.f_bg.pack(side=BOTTOM)

    def Open(self):
        o = open(self.e.get())
        self.t.insert(1.0, o.read())

    def Save(self):
        j = open(self.e.get(), "w")
        j.write(self.t.get(1.0, END))
        j.close()

    def R_BG(self):
        if self.var1.get() == 0:
            self.root.configure(bg="black")
            self.e.configure(bg="red")
            self.t.configure(bg="yellow", fg="purple")
        else:
            self.root.configure(bg="white")
            self.e.configure(bg="green")
            self.t.configure(bg="purple", fg="yellow")


root = Tk()
obj = Tnayin_3(root)
root.mainloop()
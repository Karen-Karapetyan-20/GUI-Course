from tkinter import *


class Tnayin_5:
    def __init__(self, root):
        self.root = root
        self.root.title("Tnayin 5")
        self.root.geometry("610x650")
        self.mainmenu = Menu(root)
        self.root.configure(menu=self.mainmenu)
        self.close = Menu(self.mainmenu)
        self.change = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="New")
        self.mainmenu.add_cascade(label="Save")
        self.mainmenu.add_cascade(label="Open")
        self.mainmenu.add_cascade(label="Settings", menu=self.change)
        self.mainmenu.add_cascade(label="Exit", menu=self.close)
        self.l1 = Label(self.root, width=5, height=2, bg="black")
        self.l2 = Label(self.root, width=5, height=2, bg="white")
        self.close.add_command(label="Close window", command=exit)
        self.change.add_command(label="Change colors", command=self.label_change)

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    Label(width=10, height=5, bg="white").grid(row=i, column=j)
                else:
                    Label(width=10, height=5, bg="black").grid(row=i, column=j)

    def label_change(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    Label(width=10, height=5, bg="black").grid(row=i, column=j)
                else:
                    Label(width=10, height=5, bg="white").grid(row=i, column=j)


root = Tk()
obj = Tnayin_5(root)
root.mainloop()

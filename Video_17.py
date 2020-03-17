from math import sin, cos
from tkinter import *


class Window:
    x = 0

    def __init__(self, root):
        root.geometry("600x200+350+200")
        self.c = Canvas(root, width=600, height=200, bg="white")
        self.c.pack()
        self.c.create_line((10, 0), (10, 200), width=2, arrow=BOTH, fill="grey")
        self.c.create_line((10, 100), (600, 100), width=2, arrow=LAST, fill="grey")
        self.Print_dot()

    def Print_dot(self):
        y1 = sin(self.x)
        y2 = cos(self.x)
        self.c.create_oval((25 * self.x + 10, 25 * y1 + 100), (25 * self.x + 10, 25 * y1 + 100), width=1, outline="red")
        self.c.create_oval((25 * self.x + 10, 25 * y2 + 100), (25 * self.x + 10, 25 * y2 + 100), width=1,
                           outline="blue")

        self.x += 0.03
        root.after(5, self.Print_dot)


root = Tk()
obj = Window(root)
root.mainloop()

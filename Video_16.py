from tkinter import *


class Window:
    def __init__(self, root):
        self.c = Canvas(root, width=400, height=400, bg="white")
        self.c.pack()

        self.oval_1 = self.c.create_oval((10, 10), (90, 90), width=0, fill="red", tag="ovals")
        self.oval_2 = self.c.create_oval((310, 10), (390, 90), width=0, fill="blue", tag="ovals")
        self.triangle = self.c.create_polygon((200, 200), (10, 390), (390, 390), fill="green")
        self.c.tag_bind(self.oval_1, "<Button-1>", self.create_outline)
        self.c.tag_bind(self.oval_2, "<Button-1>", self.change_fill)
        self.c.tag_bind(self.triangle, "<Button-1>", self.move_ovals)
        root.bind("<Button-3>", self.clear_canvas)

    def create_outline(self, event):
        self.c.itemconfigure(self.oval_1, outline="blue", width=3)

    def change_fill(self, event):
        self.c.itemconfigure(self.oval_2, fill="orange")
        self.c.coords(self.oval_2, 250, 10, 390, 90)

    def move_ovals(self, event):
        self.c.move("ovals", 0, 260)

    def clear_canvas(self, event):
        self.c.delete("all")


root = Tk()
obj = Window(root)
root.mainloop()

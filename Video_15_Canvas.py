from tkinter import *


class Window:
    def __init__(self, root):
        self.c = Canvas(root, width=500, height=500, cursor="pencil", bg="white")
        self.c.pack()
        self.c.create_line((250, 0), (250, 500), width=3, fill="red", arrow=LAST)
        self.c.create_line((0, 250), (500, 250), width=3, fill="blue", arrow=BOTH)
        self.c.create_rectangle((10, 10), (240, 240), fill="green", outline="red")
        self.c.create_polygon((260, 10), (490, 10), (400, 125), (490, 240), (260, 240), (350, 125), fill="orange",
                              smooth=1)
        self.c.create_oval((10, 260), (240, 340), fill="yellow", outline="red", width=3)
        self.c.create_arc((10, 350), (90, 430), start=0, extent=270, fill="blue")
        self.c.create_arc((10, 350), (90, 430), start=0, extent=270, fill="blue")
        self.c.create_arc((80, 410), (160, 490), start=0, extent=270, style=ARC, outline="orange", width=3)
        self.c.create_text((275, 330), text="Tkinter \nthis is a program \nwith window's interface", font="Verdana 12",
                           anchor=W, justify=CENTER, fill="orange")


root = Tk()
obj = Window(root)
root.mainloop()

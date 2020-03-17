from tkinter import *


class Tnayin_6:
    f = True

    def __init__(self, root):
        root.title("Tnayin_6")
        root.geometry("900x500")
        root.configure(bg="green")
        self.l = Label(root, text="Label", bg="black", fg="white")
        self.b = Button(root, text="Pause", bg="black", fg="white", command=self.button)
        self.x1 = 0.5
        self.y1 = 0.5
        self.z1 = 0.1
        self.b.place(relx=0, rely=0, relwidth=0.2, relheight=0.1)
        self.l.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.1, anchor=CENTER)
        root.bind("<Left>", self.Left_Click)
        root.bind("<Up>", self.Up_Click)
        root.bind("<Right>", self.Right_Click)
        root.bind("<Down>", self.Down_Click)

    def button(self):
        if self.f == True:
            self.f = False
            self.b.configure(text="Play")
        else:
            self.f = True
            self.b.configure(text="Pause")

    def Left_Click(self, event):
        if self.f:
            self.l.place(relx=self.x1, rely=self.y1, anchor=CENTER)
            self.x1 -= self.z1
            if self.x1 < 0 and self.y1 == 0.5:
                self.x1 = 1.2
                self.x1 -= self.z1
            root.after(100, lambda: self.Left_Click(event))

    def Up_Click(self, event):
        if self.f:
            self.l.place(relx=self.x1, rely=self.y1, anchor=CENTER)
            self.y1 -= self.z1
            if self.y1 < 0 and self.x1 == 0.5:
                self.y1 = 1.2
                self.y1 -= self.z1
            root.after(100, lambda: self.Up_Click(event))

    def Right_Click(self, event):
        if self.f:
            self.l.place(relx=self.x1, rely=self.y1, anchor=CENTER)
            self.x1 += self.z1
            if self.x1 > 1 and self.y1 == 0.5:
                self.x1 = 0
                self.x1 += self.z1
            root.after(100, lambda: self.Right_Click(event))

    def Down_Click(self, event):
        if self.f:
            self.l.place(relx=self.x1, rely=self.y1, anchor=CENTER)
            self.y1 += self.z1
            if self.y1 > 1 and self.x1 == 0.5:
                self.y1 = -0.2
                self.y1 += self.z1
            root.after(100, lambda: self.Down_Click(event))


root = Tk()
obj = Tnayin_6(root)
root.mainloop()

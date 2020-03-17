from tkinter import *
from tkinter.messagebox import *


class Window:
    def __init__(self, root):
        self.b1 = Button(root, text="askquestion", font=20, width=12)
        self.b1.grid(row=0, column=0, sticky=E + W)
        self.l1 = Label(root, font=20, width=12)
        self.l1.grid(row=0, column=1, sticky=E + W)
        self.b1.bind("<Button-1>", self.asq_question)

        self.b2 = Button(root, text="askokcancel", font=20, width=12)
        self.b2.grid(row=1, column=0, sticky=E + W)
        self.l2 = Label(root, font=20, width=12)
        self.l2.grid(row=1, column=1, sticky=E + W)
        self.b2.bind("<Button-1>", self.asq_ok_cancel)

        self.b3 = Button(root, text="askyesno", font=20, width=12)
        self.b3.grid(row=2, column=0, sticky=E + W)
        self.l3 = Label(root, font=20, width=12)
        self.l3.grid(row=2, column=1, sticky=E + W)
        self.b3.bind("<Button-1>", self.asq_yes_no)

        self.b4 = Button(root, text="askyesno", font=20, width=12)
        self.b4.grid(row=3, column=0, sticky=E + W)
        self.l4 = Label(root, font=20, width=12)
        self.l4.grid(row=3, column=1, sticky=E + W)
        self.b4.bind("<Button-1>", self.asq_retry_cancel)

    def asq_question(self, event):
        answer = askquestion("AskQuestion", "Harc hamar 1")
        self.l1.configure(text=answer)

    def asq_ok_cancel(self, event):
        answer = askokcancel("AskOkCancel", "Harc hamar 2")
        self.l2.configure(text=answer)

    def asq_yes_no(self, event):
        answer = askyesno("AskYesNo", "Harc hamar 3")
        self.l3.configure(text=answer)

    def asq_retry_cancel(self, event):
        answer = askyesno("AskRetryCancel", "Harc hamar 4")
        self.l4.configure(text=answer)


root = Tk()
obj = Window(root)
root.mainloop()

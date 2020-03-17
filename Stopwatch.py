from tkinter import *
from datetime import datetime


class Stopwatch:
    temp = 0
    after_id = ""

    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.l = Label(self.root, text="00:00", width=5, font=("Ubuntu", 100))
        self.b1 = Button(self.root, text="Start", font=("Ubuntu", 30), command=self.start_sw)
        self.b2 = Button(self.root, text="Stop", font=("Ubuntu", 30), command=self.stop_sw)
        self.b3 = Button(self.root, text="Continue", font=("Ubuntu", 30), command=self.continue_sw)
        self.b4 = Button(self.root, text="Reset", font=("Ubuntu", 30), command=self.reset_sw)

        self.l.grid(row=0, columnspan=2)
        self.b1.grid(row=1, columnspan=2, sticky=E + W)

    def start_sw(self):
        self.b1.grid_forget()
        self.b2.grid(row=1, columnspan=2, sticky=E + W)
        self.tick()

    def tick(self):
        self.after_id = self.root.after(1000, self.tick)
        f_temp = datetime.fromtimestamp(self.temp).strftime("%M:%S")
        self.temp += 1
        self.l.configure(text=str(f_temp))

    def stop_sw(self):
        self.b2.grid_forget()
        self.b3.grid(row=1, column=0, sticky=E + W)
        self.b4.grid(row=1, column=1, sticky=E + W)
        self.root.after_cancel(self.after_id)

    def continue_sw(self):
        self.b3.grid_forget()
        self.b4.grid_forget()
        self.b2.grid(row=1, columnspan=2, sticky=E + W)
        self.tick()

    def reset_sw(self):
        self.temp = 0
        self.l.configure(text="00:00")
        self.b3.grid_forget()
        self.b4.grid_forget()
        self.b1.grid(row=1, columnspan=2, sticky=E + W)


root = Tk()
obj = Stopwatch(root)
root.mainloop()

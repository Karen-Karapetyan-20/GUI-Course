from tkinter.filedialog import *
from tkinter import *


class Window:
    def __init__(self, root):
        self.main_menu = Menu(root)
        root.configure(menu=self.main_menu)

        self.first_item = Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="File", menu=self.first_item)

        self.first_item.add_command(label="Open", command=self.open_file)
        self.first_item.add_command(label="Save", command=self.save_file)
        self.first_item.add_command(label="Exit", command=self.exit_file)

        self.t = Text(root, width=40, height=15, font=12)
        self.t.pack(expand=YES, fill=BOTH)

    def open_file(self):
        of = askopenfilename()
        file = open(of, "r")
        self.t.insert(END, file.read())
        file.close()

    def save_file(self):
        sf = asksaveasfilename()
        final_text = self.t.get(1.0, END)
        file = open(sf, "w")
        file.write(final_text)
        file.close()

    def exit_file(self):
        root.quit()


root = Tk()
obj = Window(root)
root.mainloop()

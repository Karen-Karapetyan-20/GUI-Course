from tkinter import *


class Menu_Video:
    def __init__(self, root):
        self.main_menu = Menu(root)
        root.configure(menu=self.main_menu)
        self.first_item = Menu(self.main_menu)
        self.main_menu.add_cascade(label="File", menu=self.first_item)
        self.first_item.add_command(label="New", command=self.new_win)
        self.first_item.add_command(label="Exit", command=self.exit_app)
        self.second_item = Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Edit", menu=self.second_item)
        self.second_item.add_command(label="Item 1")
        self.second_item.add_command(label="Item 2")
        self.second_item.add_command(label="Item 3")
        self.second_item.add_separator()
        self.second_item.add_command(label="Item 4")

        self.tool_bar = Frame(root, bg="black")
        self.tool_bar.pack(side=TOP, fill=X)

        self.b1 = Button(self.tool_bar, text="Cut", bg="white", fg="black")
        self.b1.grid(row=0, column=0, padx=2, pady=2)

        self.b2 = Button(self.tool_bar, text="Copy", bg="white", fg="black")
        self.b2.grid(row=0, column=1, padx=2, pady=2)

        self.b3 = Button(self.tool_bar, text="Paste", bg="white", fg="black")
        self.b3.grid(row=0, column=2, padx=2, pady=2)

        self.status_bar = Label(root, relief=SUNKEN, anchor=W, text="Mission complete !")
        self.status_bar.pack(side=BOTTOM, fill=X)


    def new_win(self):
        win = Toplevel(root)
        label1 = Label(win, text="Bardzr makardaki patuhani text", font=20)
        label1.pack()

    def exit_app(self):
        root.destroy()




root = Tk()
obj = Menu_Video(root)
root.mainloop()

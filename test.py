from tkinter import *

master = Tk()

v = IntVar()
v.set(1)
Radiobutton(master, text="One", variable=v, value=1).pack(anchor=W)
Radiobutton(master, text="Two", variable=v, value=2).pack(anchor=W)

mainloop()
sadfasfd
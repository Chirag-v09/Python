from tkinter import *

root = Tk()


def leftclick(event):
    print("Left")


def rightclick(event):
    print('Right')


def midleclick(event):
    print("Midle")


frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftclick)
frame.bind('<Button-2>', midleclick)
frame.bind("<Button-3>", rightclick)
frame.pack()

root.mainloop()

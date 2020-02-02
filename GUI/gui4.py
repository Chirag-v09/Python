from tkinter import *

root = Tk()


def printname():
    print("Hello my name is Chirag Verma")


button_1 = Button(root, text='Print my Name', command=printname)
button_1.pack()

root.mainloop()

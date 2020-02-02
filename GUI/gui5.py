from tkinter import *
import tkinter.ttk

root = Tk()


def printname(event):
    print('Hello my name is Chirag Verma')


button_1 = Button(root, text='Print my Name')
button_1.bind("<Button-1>", printname)
button_1.grid(row=0, column=1)
tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=0, row=1, rowspan=1, sticky='ns')

root.mainloop()
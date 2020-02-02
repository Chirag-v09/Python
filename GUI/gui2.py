from tkinter import *

root = Tk()

one = Label(root, text='One', bg='red', fg='white')
one.pack()
Two = Label(root, text='Two', bg='green', fg='black')
Two.pack(fill=X)
three = Label(root, text='Three', bg='purple', fg='yellow')
three.pack(side=LEFT, fill=Y)

root.mainloop()

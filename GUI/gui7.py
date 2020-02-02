from tkinter import *
import tkinter.messagebox

class ChiragButton:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printbutton = Button(frame, text='Print message', command=self.printmessage)
        self.printbutton.pack(side=LEFT)

        self.quitbutton = Button(frame, text='Quit', command=frame.quit)
        self.quitbutton.pack(side=LEFT)

    def printmessage(self):
        x = 'hello'
        tkinter.messagebox.showinfo('Window Title', x)
        print("Wow! It's worked...")


root = Tk()
c = ChiragButton(root)

root.mainloop()

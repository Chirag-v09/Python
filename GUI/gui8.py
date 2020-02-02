from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title', 'Monkeys love bananas')

answer = tkinter.messagebox.askquestion('Questions', 'Do you like pizza with sweet cron toppings on it?')

if answer == 'yes':
    print("()")

root.mainloop()

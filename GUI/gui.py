from tkinter import *

root = Tk()

# theLabel = Label(root, text='hello world')
# theLabel.pack()

topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

button1 = Button(topframe, text='Button 1', fg='red')
button2 = Button(topframe, text='Button 2', fg='green')
button3 = Button(topframe, text='Button 3', fg='blue')
button4 = Button(bottomframe, text='Button 4', fg='black')

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)

root.geometry('300x300+500+200')
root.mainloop()

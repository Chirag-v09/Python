# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:20:50 2019

@author: Chirag
"""

from tkinter import *
def func1():
    global top
    top=Toplevel()
def func2():
    global top
    top.destroy()

root=Tk()
root.geometry("300x300")
btn=Button(root,text="Create",command=func1)
btn.pack()
btn1=Button(root,text="Destroy",command=func2)
btn1.pack()

root.mainloop()

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:25:55 2024

@author: hema
"""
# data type error

from tkinter import*
from tkinter import messagebox

root=Tk()
root.geometry("900x600")
root.title("opps implementation")

input_box=Entry(root)
input_box.pack()

def addition():
    number =7
    get_input=input_box.get()
    try:
        print(number+get_input)
    except TypeError:
        messagebox.showinfo("error", "Cant add 2 different datatypes")
        
button=Button(root,text="addition",command=addition)
button.pack()
root.mainloop()
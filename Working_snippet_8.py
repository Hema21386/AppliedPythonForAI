# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 16:39:38 2024

@author: hema
"""
#Try to implement the scroll bar functionality in the parent window

from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import random

root = Tk()
root.geometry("900x600")
root.title("Oops implementation")

guielements=["Label", "Button", "Dropdown"]

dropdown=ttk.Combobox(root,state="readonly",values=guielements)
dropdown.pack()

class CreateElements:
    def __init__(self):
        print ("This is create element class")
    
        
    def createlabel(self):
        randomno=random.randint(1,20)
        label=Label(root, text="New label is created with random number " +str(randomno), fg="teal")
        label.pack()
        
    def createbutton(self):
        classbtn=Button(root,text="Button", command=self.message)
        classbtn.pack(padx=20, pady=10)
        
    def createdropdown(self):
        value=[1,2,3,4]
        classdropdown=ttk.Combobox(root,state="readonly",values=value)
        classdropdown.pack()
        
    def choose(self):
        # calling the variable which is outside the scope of a class
        global dropdown
        element=dropdown.get()
        if(element=="Label"):
            self.createlabel()
        elif(element=="Button"):
            self.createbutton()
        elif(element=="Dropdown"):
            self.createdropdown()
            
    def message(self):
        messagebox.showinfo("Show Info","You clicked the button created using class")
            
object1=CreateElements()
btn=Button(root,text="CreateElement", command=object1.choose)
btn.pack(padx=20, pady=10)

root.mainloop()
            

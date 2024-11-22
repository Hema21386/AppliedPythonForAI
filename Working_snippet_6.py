# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:12:56 2024

@author: Hema
"""

# Write a program to create password generator using 3d arrays

"""
Created on Tue Sep 24 16:47:52 2024

@author: Hema
"""

#Creating a random password generator

from tkinter import *
import random

root=Tk()
root.title("Password generator")
root.geometry("400x400")

label=Label(root)
array_3d=[[['1','2','3','4','5','6','7','8','0'],["happy","power","kind"],["A","B","C","D","E"]]]

def newpassword():
    random1=random.randint(0,8)
    random2=random.randint(0,2)
    random3=random.randint(0,4)
    
    letter1=array_3d[0][0][random1]
    letter2=array_3d[0][1][random2]
    letter3=array_3d[0][2][random3]
    
    label["text"] = letter1+letter2+letter3
    
btn=Button(root,text="Generate password", command=newpassword)
btn.place(relx=0.3,rely=0.3, anchor=CENTER)
label.place(relx=0.5,rely=0.5, anchor=CENTER)
    
root.mainloop()

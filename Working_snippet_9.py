# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:00:24 2024

@author: Hema
"""

#Fibonacci Series... 0 1 1 2 3 5....

from tkinter import*
root=Tk()

root.title("Fibonacci Series")
root.geometry("500x500")

enter_no=Entry(root)
label=Label(root,text="Fibonacci Series")
label1=Label(root,text="Sum of Fibonacci Series")

def Fibonacci():
    input_no= int(enter_no.get())
    first_no=0
    second_no=1
    sum=0
    sum1=0
    counter=1
    
    while(counter<= input_no):
        label["text"] += str(sum)+ " "
        label1["text"] = str(sum1)+ ""
        counter=counter+1
        first_no=second_no
        second_no=sum
        sum=first_no+second_no
        sum1=sum1+sum
        
enter_no.pack()
btn=Button(root, text="Fibonacci Series", command=Fibonacci, fg="purple", bg="blue")
btn.pack()

label.pack()
label1.pack()
root.mainloop()
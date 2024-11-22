# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:19:55 2024

@author: Hema
"""

# Create the logs of books and their details using object oriented programming

class logofbooks:
    def __init__(self,name,author,startdate,enddate):
        self.book_name=name
        self.author=author
        self.startdate=startdate
        self.enddate=enddate
        
    def add_book(self):
        print("Book Name:" +self.book_name)
        print("Author:" +self.author)
        print("Start Date:" +self.startdate)
        print("End Date:" +self.enddate)
        
Book1=logofbooks("The Monk Who Sold His Ferrari", "Robin Sharma", "03-Jan-2024", "20-Jan-2024")
Book1.add_book()

Book2=logofbooks("2 States", "Chetan Bhagat", "15-Feb-2024", "21-Feb-2024")
Book2.add_book()

Book3=logofbooks("The power of positive thinking", "Norman Vincent Peale", "20-Sep-2024", "xx-xx-xxxx")
Book3.add_book()

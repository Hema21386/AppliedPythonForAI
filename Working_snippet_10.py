# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:40:34 2024

@author: hema
"""

#inheritance

"""
Inheritance is a concept in oops which allows you to define a class that inherits all/some of the methods and properties of a class

base class/ parent class-- the class whose methods and attributes are being inherited
derived class/ child class-- the class which inherits methods and attributes from parent class/another class

"""
#base class/ parent class
class Doctor():
    def __init__(self):
        print("This is class doctor")
        
    def BMI(weight, height):
        bmi=weight/(height*height)
        print("Your BMI is " +str(bmi))
        
    def heart_rate(heartrate):
        if (heartrate>=60 and heartrate<100):
            print("Your heart rate is normal")
        else:
            print("Your hear rate is not normal")
            
#Used for multiple inheritance
class Surgeon:
    def operation(self):
        print("Operation")
            
class Patient(Doctor,Surgeon):
    def __init__(self,name,weight,height,heartrate):
        self.patientname=name
        self.patientweight=weight
        self.patientheight=height
        self.patientheartrate=heartrate
        
    def healthcheck(self):
        print("Name of the patient: ", self.patientname)
        Doctor.BMI(self.patientweight,self.patientheight)
        Doctor.heart_rate(self.patientheartrate)
        
patient1=Patient("Hema",53,54.3,80)
patient1.healthcheck()
patient1.operation()
patient2=Patient("Kajal",70,54.3,75)
patient2.healthcheck()

#multiple inheritance syntax and usage
#class Patient(Doctor,Surgeon):

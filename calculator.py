# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:38:25 2021

@author: Anagha
"""

# CREATE A CALCULATOR

def add():
    a=int(input("enter a value"))
    b=int(input("enter a value"))
    print(a+b)

def subtract():
    x=int(input("enter a value"))
    y=int(input("enter a value"))
    print(x-y)


def multiply():
    d=int(input("enter a value"))
    e=int(input("enter a value"))
    print(d*e)


def divide():
    g=int(input("enter a value"))
    h=int(input("enter a value"))
    print(g/h)


def cal():
    print("Calculator")
    print("1.Add")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    c=input("Enter a choice")
    if(c=="1"):
        add()
    elif(c=="2"):
         subtract()
    elif(c=="3"):
         multiply()
    elif(c=="4"):
         divide()
    else:
        print("Exit the Calculator")  
    t=input("Do you want to continue,Enter your choice Y/N")
    if(t=="Y"):
        cal()
    else:
        print("End of calculator")
    
        
    
    
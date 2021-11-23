# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 14:09:27 2021

@author: Anagha
"""

# Nested if-else syntax 1

def func():
    var=int(input("enter a value"))
    if var < 200:
       print("Expression value is less than 200")
       if var == 150:
          print("The Expression is equal to 150")
       elif var == 100:
            print("The expression is 100")
       elif var == 50:
            print("The expression is equal to 50")
       elif var < 50:
            print("The expression is less than 50")
    else:
        print("Could not find true expression")
        
        print("Goodbye")
        



    

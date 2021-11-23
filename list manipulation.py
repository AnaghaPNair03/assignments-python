# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 14:45:14 2021

@author: Anagha
"""

# List and String Methods

def due():
    L1=[1,"six",2,3,"apple"]
    print(L1)
    L2=[1,2,3,4,"five",3]
    print(L2)
    L3=[6,4,2,0,"two","lie",8,"True"]
    print(len(L3))
    L4=[10,20,30,"true","abc",40]
    print(type(L4))
    L5=list(("apple","banana","cherry","blueberry"))
    print(L5)
    L6=[1,2,3,4,5,6,7,12]
    L6.append(13)
    print(L6)
    L7=["a","b","c","d","e"]
    L8=["f","g","h","i"]
    L7.append(L8)
    print(L7)
    
def rue():
    L1=[1,2,3,4,5]
    L1.clear()
    print(L1)
    L2=["a","b","c","d","e"]
    y=L2.copy()
    print(y)
    L3=[1,2,3,4,5,2,6,7,2]
    x=L3.count(2)
    print(x)
    L4=["apple","cherry","banana","blueberry","kiwi"]
    L4.extend(["lichi"])
    print(L4)
    L5=["apple","cherry","banana","blueberry","kiwi"]
    L6=('1','2','3','4')
    L5.extend(L6)
    print(L5)
    L7=[1,2,3,4,5,"apple","car","six",6,8,10]
    a=L7.index("car")
    print(a)
    L8=[1,2,3,4,5,"apple","car","six",6,8,10]
    L8.insert(6,"banana")
    print(L8)
    
def view():
    L1=[1,2,3,4,5,6]
    x=L1.pop(3)
    print(x)
    L2=["abc",23,45,89,36,10]    
    L2.remove(36)
    print(L2)
    L3=[34,54,67,87,9,12]
    L3.reverse()
    print(L3)
    L4=["abc","def","ghi","jkl","mno"]
    L4.sort(reverse=False)
    print(L4)
    L5=["abc","def","ghi","jkl","mno"]
    L5.sort(reverse=True)
    print(L5)
    L6=["apple","cherry","banana","blueberry","kiwi"]
    print(L6[2:4])
    L7=[1,2,3,4,5,"apple","car","six",6,8,10]
    print(L7[-6:-2])
    
    
    

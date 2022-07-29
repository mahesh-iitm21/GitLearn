# -*- coding: utf-8 -*-
"""
Created on Wed May 18 14:58:48 2022

@author: mahes
"""
print(34)
l="Monkeys write"
m="New York times"
a=""
for i in l:
    if i.isalpha()==True:
        i=i.lower()
        a=a+i
print(a)  
A=[]
for i in range(len(a)):
    A.append(a[i])
b=""
for j in m:
    if j.isalpha()==True:
        j=j.lower()
        b=b+j
print(b)  
B=[]
for i in b:
    B.append(i)
print(A)
print(B)
A.sort()
B.sort()
if A==B:
    print("Hurray")

      
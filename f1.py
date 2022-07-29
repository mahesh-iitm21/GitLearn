# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:39:38 2022

@author: mahes
"""
k=[4,5,5,1,2,7]
l=[4,5,5,1,2,7]
l.sort()
print(l)

for i in range (len(k)):
    for j in range (len(k)):
        if k[i]==l[j]:
            print(j+1)
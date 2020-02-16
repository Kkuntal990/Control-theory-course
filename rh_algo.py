#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:56:51 2020

@author: kuntal
"""
import numpy as np
import matplotlib.pyplot as plt


def column(matrix, i):
    return [row[i] for row in matrix]

def check(order, coeff):
    m = int(order/2) +1
    n = order+1
    routh = np.zeros((n, m))
    coeff1 = coeff[::2]
    coeff2 = coeff[1::2]
    
    if len(coeff1) > len(coeff2):
        coeff2.append(0)
        
    routh[0] = coeff1
    routh[1] = coeff2
#    print(coeff1)
#    print(coeff2)
    flag = True
    for i in range(2,n):
        for j in range(m-1):
            routh[i][j] = (-1/routh[i-1][0])*(routh[i-2][0]*routh[i-1][j+1] - routh[i-1][0]*routh[i-2][j+1])
    #print(routh)
    col = column(routh,0)
    #print(col)
    for element in coeff:
        if element == 0:
            flag =  False
    
    if min(coeff) < 0 < max(coeff):
        flag =  False
     
    sign = 1
    count = 0
    for element in col:
        temp = element/abs(element)
        if (sign != temp):
            count +=1
            sign = temp
            flag = False
            
    return flag, count
    
     
coeff =  [6,1,2,4,3]
       
    
f, c = check(4,coeff )

def poly(x):
    return 6*x**4 + x**3 + 2*x**2 + 4*x + 3

x = np.linspace(-0.8,0, 2000)
fig, ax = plt.subplots()
ax.plot(x, poly(x))
ax.grid(True, which='both')
plt.show()

print("Number of roots in right half of the plane: ", c)
if f:
    print("System is stable")
else:
    print("System unstable")

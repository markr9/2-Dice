# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 17:32:25 2019

@author: MR
"""

from random import random
import matplotlib.pyplot as plt

a=[]
rolls=1e7
i=0
while i<rolls:
    a.append(int(random()*6+1)+int(random()*6+1))
    i+=1
    
y=[]
x=[]
z=[]
w=[]
j=1
while j<12:
    y.append(a.count(float(j+1)))
    x.append(j+1)
    if j!=1:
        z.append(z[j-2]+y[j-1])
    else:
        z.append(y[j-2])
    #print(z)
    j+=1

k=0   
while k<len(z):
    z[k]/=(rolls/100)
    y[k]/=(rolls/100)
    w.append(12-k)
    k+=1
    
x2=[6,5,4,3,2,1]
y2=[1/6*100,2/6*100,3/6*100,4/6*100,5/6*100,100]
    
plt.plot(x,y)
plt.xlabel('Roll sum')
plt.ylabel('Frequency')
plt.grid('on')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.show()
#print(x,y,w,z,x2,y2)
plt.plot(w,z,x2,y2)
plt.xlabel('Roll')
plt.ylabel('Chance')
plt.grid('on')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
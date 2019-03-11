#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:02:25 2019

@author: Mate
"""

import numpy as np
import praktikum_addons.bib as bib
import matplotlib.pyplot as plt

l = 632.8
e_s = 0.01/np.sqrt(12)
e_m = 0.1
file = open("../Rohdaten/kalib.dat")
data = []
for line in file:
    d = np.array(line.split(" "))
    data.append(d.astype(np.float))

A = []
B = []

def f1():
    i = len(data)-2
    x = np.arange(0, (len(data[i]))*10, 10)
    y = np.array(data[i])
    ey = np.ones(len(data[i]))*e_s
    ex = np.ones(len(data[i]))*e_m
    ax1, ax2, a,ea,b,eb,chiq,corr = bib.pltmitres(x,data[i],ey, ex=ex,yeinheit="mm", xl="m", yl="s", regData=True)
    A = a
    B = b
    
    deltas = []
    for j in range(len(x)-1):
        deltas.append((y[j+1]-y[j]))
    deltas = np.array(deltas)
    
    #1. Fall: Nehme +0.07 als 10 an
    ax1, ax2, a,ea,b,eb,chiq,corr = bib.pltmitres(x[:-1],deltas,ey[:-1],yeinheit="mm", xl="m", yl="δ", regData=True)
    korrektur = np.round((deltas-0.07)/0.01)
    korrektur = np.append(np.zeros(1), korrektur)
    
    x2=np.array(x)
    
    for j in range(len(korrektur)):
        for k in range(j,len(x2)):
            x2[k] = x2[k]+korrektur[j]
    
    ax1, ax2, a,ea,b,eb,chiq,corr=bib.pltmitres(x2,y,ey,yeinheit="mm", xl="m", yl="s", regData=True)
#-------------------------------------------------
def f2():
    i = len(data)-1
    x = np.arange(0, (len(data[i]))*10, 10)
    y = np.array(data[i])
    ey = np.ones(len(data[i]))*e_s
    ex = np.ones(len(data[i]))*e_m
    ax1, ax2, a,ea,b,eb,chiq,corr = bib.pltmitres(x,data[i],ey, ex=ex,yeinheit="mm", xl="m", yl="s", regData=True)
    A = a
    B = b
    
    deltas = []
    for j in range(len(x)-1):
        deltas.append((y[j+1]-y[j]))
    deltas = np.array(deltas)
    
    #1. Fall: Nehme +0.07 als 10 an
    ax1, ax2, a,ea,b,eb,chiq,corr = bib.pltmitres(x[:-1],deltas,ey[:-1],yeinheit="mm", xl="m", yl="δ", regData=True)
    korrektur = np.round((deltas-0.07)/0.01)
    korrektur = np.append(np.zeros(1), korrektur)
    
    x2=np.array(x)
    
    for j in range(len(korrektur)):
        for k in range(j,len(x2)):
            x2[k] = x2[k]+korrektur[j]
    
    ax1, ax2, a,ea,b,eb,chiq,corr=bib.pltmitres(x2,y,ey,yeinheit="mm", xl="m", yl="s", regData=True)
    print(a)
    print(x2)
    
def f3():
    i = len(data)-3
    x = np.arange(0, (len(data[i]))*10, 10)
    y = np.array(data[i])
    ey = np.ones(len(data[i]))*e_s
    ex = np.ones(len(data[i]))*e_m
    ax1, ax2, a,ea,b,eb,chiq,corr = bib.pltmitres(x,data[i],ey, ex=ex,yeinheit="mm", xl="m", yl="s", regData=True)
    A = a
    B = b
    
    deltas = []
    for j in range(len(x)-1):
        deltas.append((y[j+1]-y[j]))
    deltas = np.array(deltas)
    
    #1. Fall: Nehme +0.07 als 10 an
    ax1, ax2, a,ea,b,eb,chiq,corr = bib.pltmitres(x[:-1],deltas,ey[:-1],yeinheit="mm", xl="m", yl="δ", regData=True)
    korrektur = np.round((deltas-0.07)/0.01)
    korrektur = np.append(np.zeros(1), korrektur)
    
    x2=np.array(x)
    
    for j in range(len(korrektur)):
        for k in range(j,len(x2)):
            x2[k] = x2[k]+korrektur[j]
    
    ax1, ax2, a,ea,b,eb,chiq,corr=bib.pltmitres(x2,y,ey,yeinheit="mm", xl="m", yl="s", regData=True)
    print(a)
f1()
f2()
f3()
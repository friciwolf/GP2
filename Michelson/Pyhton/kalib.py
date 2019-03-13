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


def f1(korr=False):
    i = len(data)-1
    x = np.arange(0, (0+len(data[i][0:]))*10, 10)#12
    y = np.array(data[i][0:])#12
    ey = np.ones(len(x))*e_s
    ex = np.ones(len(x))*e_m
    ax1, ax2, a,ea,b,eb,chiq,corr = bib.pltmitres(x,y,ey, ex=ex,yeinheit="mm", xl="m", yl="s", regData=True, title="kalib1")

    if korr:
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
    print("a=", a)
    k=l/(2*a)
    k*=10**-9 * 10**3
    ek = l*0.5*ea/a**2 * 10**-9 * 10**3
    print("k=", k)
    print("ek=", ek)
    print("ek/k", ek/k)
    return k, ek

def f2(korr=False):
    i = len(data)-2
    x = np.arange(0, (0+len(data[i][0:]))*10, 10)#12
    y = np.array(data[i][0:])#12
    ey = np.ones(len(x))*e_s
    ex = np.ones(len(x))*e_m
    ax1, ax2, a,ea,b,eb,chiq,corr = bib.pltmitres(x,y,ey, ex=ex,yeinheit="mm", xl="m", yl="s", regData=True, title="kalib2")
    
    #Korrektur?
    if korr:
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
    print("a=", a)
    k=l/(2*a)
    k*=10**-9 * 10**3
    ek = l*0.5*ea/a**2*10**-9 * 10**3
    print("k=", k)
    print("ek=", ek)
    print("ek/k", ek/k)
    return k, ek
    
def f3(korr=False):
    i = len(data)-3
    x = np.arange(0, (len(data[i]))*10, 10)
    y = np.array(data[i])
    ey = np.ones(len(x))*e_s
    ex = np.ones(len(x))*e_m
    ax1, ax2, a,ea,b,eb,chiq,corr = bib.pltmitres(x,y,ey, ex=ex,yeinheit="mm", xl="m", yl="s", regData=True, title="kalib3")
    
    #Korrektur?
    if korr:
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
    print("a=", a)
    k=l/(2*a)
    k*=10**-9 * 10**3
    ek = l*0.5*ea/a**2 * 10**-9 * 10**3
    print("k=", k)
    print("ek=", ek)
    print("ek/k", ek/k)
    return k, ek

def k(korr=False):
    k1 = []
    k1.append(f1(korr))
    k1.append(f2(korr))
    k1.append(f3(korr))
    ek = np.std(k1)
    return k1, ek
print(k(False))
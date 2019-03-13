#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:02:25 2019

@author: Mate
"""

import numpy as np
import praktikum_addons.bib as bib
import matplotlib.pyplot as plt
import praktikum.analyse as anal

l = 632.8
e_s = 0.01/np.sqrt(12)
e_m = 0.1
file = open("../Rohdaten/kalib.dat")
data = []
for line in file:
    d = np.array(line.split(" "))
    data.append(d.astype(np.float))


def f12(korr=False):
    i = len(data)-1
    #N=20
    N=0
    x = np.arange(10*N, (N+len(data[i][N:]))*10, 10)#12
    y1 = np.array(data[i][N:])#12
    
    i = len(data)-2
    y2 = np.array(data[i][N:])#12
    y = 0.5*(y1+y2)
    ey = np.ones(len(y))*e_s
    ex = np.ones(len(y))*e_m
    
    ax1, ax2, a,ea,b,eb,chiq,corr = bib.pltmitres(x,y,ey, ex=ex,yeinheit="mm", xl="m", yl="s", regData=True, title="kalib12")

    print("a=", a)
    k=l/(2*a)
    k*=10**-9 * 10**3
    ek = l*0.5*ea/a**2 * 10**-9 * 10**3
    print("k=", k)
    print("ek=", ek)
    print("ek/k", ek/k)
    return k, ek

def f1(korr=False):
    i = len(data)-1
    x = np.arange(0, (0+len(data[i][0:]))*10, 10)#12
    y = np.array(data[i][0:])#12
    ey = np.ones(len(x))*e_s
    ex = np.ones(len(x))*e_m
    ax1, ax2, a,ea,b,eb,chiq,corr = bib.pltmitres(x,y,ey, ex=ex,yeinheit="mm", xl="m", yl="s", regData=True, title="kalib1")
    
    print("a=", a)
    k=l/(2*a)
    k*=10**-9 * 10**3
    ek = l*0.5*ea/a**2*10**-9 * 10**3
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
    
    print("a=", a)
    k=l/(2*a)
    k*=10**-9 * 10**3
    ek = l*0.5*ea/a**2 * 10**-9 * 10**3
    print("k=", k)
    print("ek=", ek)
    print("ek/k", ek/k)
    return k, ek

def kalib_1():
    i = len(data)-1
    intervalle = [0,60, 100, 200, 300]
    
    K = []
    eK = []
    for I in range(len(intervalle)-1):
        j = int(intervalle[I]/10)
        k = int(intervalle[I+1]/10)
        x = np.arange(intervalle[I], (j+len(data[i][j:k]))*10, 10)#12
        y = np.array(data[i][j:k])#12
        ey = np.ones(len(x))*e_s
        ex = np.ones(len(x))*e_m
        
        ax1, ax2, a,ea,b,eb,chiq,corr = bib.pltmitres(x,y,ey, ex=ex,yeinheit="mm", xl="m", yl="s", regData=True, title="kalib1")
    
        print("a=", a)
        k=l/(2*a)
        k*=10**-9 * 10**3
        ek = l*0.5*ea/a**2 * 10**-9 * 10**3
        print("k=", k)
        print("ek=", ek)
        print("ek/k", ek/k)
        K.append(k)
        eK.append(ek)
    return np.array(K), np.array(eK)

def kalib_2():
    i = len(data)-2
    intervalle = [0,60, 100, 200, 300]
    
    K = []
    eK = []
    for I in range(len(intervalle)-1):
        j = int(intervalle[I]/10)
        k = int(intervalle[I+1]/10)
        x = np.arange(intervalle[I], (j+len(data[i][j:k]))*10, 10)#12
        y = np.array(data[i][j:k])#12
        ey = np.ones(len(x))*e_s
        ex = np.ones(len(x))*e_m
        
        ax1, ax2, a,ea,b,eb,chiq,corr = bib.pltmitres(x,y,ey, ex=ex,yeinheit="mm", xl="m", yl="s", regData=True, title="kalib2")
    
        print("a=", a)
        k=l/(2*a)
        k*=10**-9 * 10**3
        ek = l*0.5*ea/a**2 * 10**-9 * 10**3
        print("k=", k)
        print("ek=", ek)
        print("ek/k", ek/k)
        K.append(k)
        eK.append(ek)
    return np.array(K), np.array(eK)

def k(korr=False):
    k1 = []
    k1.append(f12(korr))
    k1.append(f3(korr))
    ek = np.std(k1)
    return k1, ek
#print(k(False))
#k1 = []
#k1.append(f1(False))
#k1.append(f2(False))
#k1.append(f3(False))
#ek = np.std(k1)
#print(k1, ek)
k1, ek1 = kalib_1()
k2, ek2 = kalib_2()
for i in range(len(k1)):
    print(anal.gewichtetes_mittel(np.array([k1[i], k2[i]]), np.array([ek1[i],ek2[i]])))
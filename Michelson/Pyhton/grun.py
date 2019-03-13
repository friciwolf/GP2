#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:32:05 2019

@author: Mate
"""

import numpy as np
import praktikum_addons.bib as bib
import matplotlib.pyplot as plt
import kalib
import praktikum.analyse as anal

#k=kalib.f1(korr=True)

def stodelta(s, es):
#    k2 = 0.047661464215564706
#    ek2 = 3.8514953450756394e-05
#    ek = 4.303966797175662e-05
#    k = 0.04785297947657103 # Aus f12
#    ek3 = 4.0002020841550235689
#    k3 = 0.047578845216741605 # Aus f12 -Beschränkt auf 200:
    k1=[0.047758860737034836, 0.000166221353675446]#bis 100
    k2=[0.0471787618568906, 0.00016238177613276726]#100-200
    k3=[0.04758680292242013, 0.0001650610018844606]#ab 200
    k = []
    ek_stat = []
    ek = []
    for i in range(len(s)):
        S=s[i]
        if S<=7.65:
            k.append(k1[0]*s[i])
            ek_stat.append(k1[0]*es[i])
            ek.append(k1[1]*s[i])
        elif S>7.65 and S<=8.31:
            k.append(k2[0]*s[i])
            ek_stat.append(k2[0]*es[i])
            ek.append(k2[1]*s[i])
        elif S>8.31:
            k.append(k3[0]*s[i])
            ek_stat.append(k3[0]*es[i])
            ek.append(k3[1]*s[i])
    return np.array(k), np.array(ek), np.array(ek_stat)

l = 532.0
e_s = 0.01/np.sqrt(12)
e_m = 0.1
file = open("../Rohdaten/grun.dat")
data = []
for line in file:
    d = np.array(line.split(" "))
    data.append(d.astype(np.float))
data = np.array(data)

for i in range(1, len(data)):    
    if i!=2:
        s = data[i][:]#13:
        m = np.arange(0, len(s)*10, 10)#13
        delta, edelta_sys,edelta = stodelta(s,np.ones(len(s))*e_s)
        em = np.ones(len(delta))*e_m
        ax1, ax2, a, ea, b, eb, chiq, corr = bib.pltmitres(m,delta,edelta, ex=em, xl="m", yl="mm", regData=True, title="grun"+str(i))
        print("lambda", i,"=",2*a*10**6)
        print("e_lambda", i,"=",2*ea*10**6)
        #Verschiebemethode
        ap, eap, bp, ebp, chiq, corr = anal.lineare_regression_xy(m+e_m,delta+edelta_sys,em,edelta)
        am, eam, bm, ebm, chiq, corr = anal.lineare_regression_xy(m-e_m,delta-edelta_sys,em,edelta)
        e_l_sys = np.max((np.abs(a-ap),np.abs(a-am)))*2*10**6
        print("e_lambda_sys", i , "=", e_l_sys)


    else:
        
        s = data[i][24:29]#13:
        m = np.arange(240, 240+len(s)*10, 10)#13
        delta, edelta_sys, edelta = stodelta(s,np.ones(len(s))*e_s)
        em = np.ones(len(delta))*e_m
        ax1, ax2, a, ea, b, eb, chiq, corr = bib.pltmitres(m,delta,edelta, ex=em, xl="m", yl="mm", regData=True, title="grun"+str(i))
        print("lambda", i,"=",2*a*10**6)
        print("e_lambda", i,"=",2*ea*10**6)
        #Verschiebemethode
        ap, eap, bp, ebp, chiq, corr = anal.lineare_regression_xy(m+e_m,delta+edelta_sys,em,edelta)
        am, eam, bm, ebm, chiq, corr = anal.lineare_regression_xy(m-e_m,delta-edelta_sys,em,edelta)
        e_l_sys = np.max((np.abs(a-ap),np.abs(a-am)))*2*10**6
        print("e_lambda_sys", i , "=", e_l_sys)
        
        s = data[i][30:]#13:
        m = np.arange(300, 300+len(s)*10, 10)#13
        delta, edelta_sys, edelta = stodelta(s,np.ones(len(s))*e_s)
        em = np.ones(len(delta))*e_m
        ax1, ax2, a, ea, b, eb, chiq, corr = bib.pltmitres(m,delta,edelta, ex=em, xl="m", yl="mm", regData=True, title="grun"+str(i))
        print("lambda", i+0.5,"=",2*a*10**6)
        print("e_lambda", i+0.5,"=",2*ea*10**6)
        #Verschiebemethode
        ap, eap, bp, ebp, chiq, corr = anal.lineare_regression_xy(m+e_m,delta+edelta_sys,em,edelta)
        am, eam, bm, ebm, chiq, corr = anal.lineare_regression_xy(m-e_m,delta-edelta_sys,em,edelta)
        e_l_sys = np.max((np.abs(a-ap),np.abs(a-am)))*2*10**6
        print("e_lambda_sys", i+0.5 , "=", e_l_sys)
print("---"*20)
intervalle = [0, 100, 200, 360]
i=2
for j in range(len(intervalle)-1):
    s = data[i][int(intervalle[j]/10):int(intervalle[j+1]/10)]#13:
    m = np.arange(intervalle[j], intervalle[j]+len(s)*10, 10)#13
    delta, edelta_sys,edelta = stodelta(s,np.ones(len(s))*e_s)
    em = np.ones(len(delta))*e_m
    ax1, ax2, a, ea, b, eb, chiq, corr = bib.pltmitres(m,delta,edelta, ex=em, xl="m", yl="mm", regData=True, title="Grun"+str(i))
    print("lambda", i,"=",2*a*10**6)
    print("e_lambda", i,"=",2*ea*10**6)
    #Verschiebemethode
    ap, eap, bp, ebp, chiq, corr = anal.lineare_regression_xy(m+e_m,delta+edelta_sys,em,edelta)
    am, eam, bm, ebm, chiq, corr = anal.lineare_regression_xy(m-e_m,delta-edelta_sys,em,edelta)
    e_l_sys = np.max((np.abs(a-ap),np.abs(a-am)))*2*10**6
    print("e_lambda_sys", i , "=", e_l_sys)
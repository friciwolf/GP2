#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:24:06 2019

@author: Mate
"""
import praktikum_addons.bib as bib
import numpy as np
from pylab import *


e = 60
lambdas = np.array([643.85,546.07,508.58,479.99, 435.83, 404.66])
rot1 =26.5+np.array([27, 26, 25,35,23,21,19,22,25,21])/60
grun1 = 25.5+np.array([5,5,3])/60
blaugrun1 = 24.5+np.array([12,13,14])/60
blau1 = 24.5 + np.array([16,15,15])/60
violett1 = 24 + np.array([16,17,13])/60
dviolett1 = 20.5 + np.array([5,6,6])/60
ZnBlau1 = 24 + np.array([4,0,0])/60

rot2 = 144.5+np.array([21,20,20])/60
grun2 = 146+np.array([15,15,16])/60
blaugrun2 = 147+np.array([4,5,5])/60
blau2 = 147.5 +np.array([23,21,22])/60
violett2 = 149.5+np.array([3,2,1])/60
dviolett2 = 151 +np.array([13,14,14])/60
ZnBlau2 = 147.5+np.array([22,20,22])/60

prisma2 = [rot2, grun2, blaugrun2, blau2, violett2, dviolett2]
prisma1 = [rot1, grun1, blaugrun1, blau1, violett1, dviolett1]
ZnBlau = [ZnBlau1, ZnBlau2]

dmin = []
for i in range(len(prisma1)):
    dmin.append(-np.average(prisma1[i])+np.average(prisma2[i])*0.5)

sigma_winkel = np.std(prisma1[0])
    
dmin = np.array(dmin)
n = np.sin(bib.DegToRad(dmin+e)*0.5)/np.sin(bib.DegToRad(e/2))
bib.pltmitres(lambdas**-2,n,0,)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:24:06 2019

@author: Mate
"""
import praktikum_addons.bib as bib
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sympy import *

###################################
#HgCd
###################################

def lton(x,a,b,c):
    return a+b*x+c*x**2

e = 60
lambdas = np.array([643.85,546.07,508.58, 435.83, 404.66])*10**-9 #479.99,
rot1 =26.5+np.array([27, 26, 25,35,23,21,19,22,25,21])/60
grun1 = 25.5+np.array([5,5,3])/60
blaugrun1 = 24.5+np.array([12,13,14])/60
#blau1 = 24.5 + np.array([16,15,15])/60
violett1 = 24 + np.array([16,17,13])/60
violett1 = violett1-2
dviolett1 = 20.5 + np.array([5,6,6])/60
ZnBlau1 = 24 + np.array([4,0,0])/60

rot2 = 144.5+np.array([21,20,20])/60
grun2 = 146+np.array([15,15,16])/60
blaugrun2 = 147+np.array([4,5,5])/60
#blau2 = 147.5 +np.array([23,21,22])/60
violett2 = 149.5+np.array([3,2,1])/60
violett2 = violett2+0
dviolett2 = 151 +np.array([13,14,14])/60
ZnBlau2 = 147.5+np.array([22,20,22])/60

prisma2 = [rot2, grun2, blaugrun2, violett2, dviolett2]#blau2,
prisma1 = [rot1, grun1, blaugrun1, violett1, dviolett1]#blau1,
ZnBlau = [ZnBlau1, ZnBlau2]

dmin = []
sigma_winkel0 = np.std(prisma1[0])*np.sqrt(len(prisma1[0]))/np.sqrt(len(prisma1[0])-1)
sigma_winkel1 = []
sigma_winkel2 = []

for i in range(len(prisma1)):
    dmin.append((-np.average(prisma1[i])+np.average(prisma2[i]))*0.5)
    sigma_winkel1.append(sigma_winkel0/np.sqrt(len(prisma1[i])))
    sigma_winkel2.append(sigma_winkel0/np.sqrt(len(prisma2[i])))

sigma_winkel1 = np.array(sigma_winkel1)
sigma_winkel2 = np.array(sigma_winkel2)
sigma_winkel = np.array(np.sqrt(sigma_winkel1**2+sigma_winkel2**2))

dmin = np.array(dmin)
e_dmin = sigma_winkel/2

n = np.sin(bib.DegToRad(dmin+e)*0.5)/np.sin(bib.DegToRad(e/2))
e_n = (np.cos(bib.DegToRad(dmin+e)*0.5)/np.sin(bib.DegToRad(e/2)))*0.5*bib.DegToRad(e_dmin)

ax1, ax2, c,ec,d,ed,chiq,corr = bib.pltmitres(lambdas**-2,n,e_n, yl="n", xl="$\lambda$", xeinheit="$nm^{-2}$", ratios=[4,1], regData=True, markersize=10)
ax1.set_ylim(top=1.9)
p, cov = curve_fit(lton,lambdas**-2,n,sigma=e_n)
a = np.arange(min(lambdas**-2)*0.95,max(lambdas**-2)*1.05,max(lambdas**-2)*0.01)
b = lton(a,*p)
#ax1.plot(a,b, color="b", label="fit")
#ax2.plot(a,b-c*a-d, color="b")
plt.show()
plt.close()
plt.errorbar(lambdas**-2, n-lton(lambdas**-2,*p),e_n, color="b", label="Residum-plot", marker="x", linestyle="None", capsize=5)
plt.legend(title="$\chi^2 /NDF={:.4f}$".format(bib.chiq(n,lton(lambdas**-2,*p),e_n)/(len(lambdas)-3)))
plt.axhline(0)
plt.show()

###################################
#Zn-Lampe
###################################
def ntol(n,a,b,c):
    return ((-b+np.sqrt(b**2-4*(a-n)*c))/(2*(c)))**(-0.5)

def gauss_ntol(n_eval,e_n, p1, p2, p3):
    n,a,b,c = symbols("n a b c")
    return diff(((-b+sqrt(b**2-4*(a-n)*c))/(2*(c)))**(-0.5),n).subs([(n,n_eval),(a,p1),(b,p2),(c,p3)])*e_n

d = 0.5*(-np.average(ZnBlau1)+np.average(ZnBlau2))
s_d = 0.5*np.sqrt(2)*sigma_winkel0/np.sqrt(3)
n_Zn = np.sin(bib.DegToRad(d+e)*0.5)/np.sin(bib.DegToRad(e/2))
e_n_Zn = np.cos(bib.DegToRad(d+e)*0.5)/np.sin(bib.DegToRad(e/2))*bib.DegToRad(s_d)*0.5
print("Die Wellenlänge beträgt damit",ntol(n_Zn,*p))
print("oberere Grenze", ntol(n_Zn+e_n_Zn,*p))
print("untere Grenze", ntol(n_Zn-e_n_Zn,*p))
print("Gauss:", gauss_ntol(n_Zn,e_n_Zn, *p))
###################################
#Auflösungsvermögen
###################################

def d_lton(l, a, b, c):
    return -2*b*l**-3-4*c*l**-5

a1=1.5*10**-3
l1 = 579.07*10**-9
l2 = 576.96*10**-9
A_theo1 = l2/(l1-l2)
A_theo2 = l1/(l1-l2)
n_l1 = lton(l1**-2,*p)
n_l2 = lton(l2**-2, *p)
print(A_theo1)
print(A_theo2)
A1 = (d_lton(l1, *p))*2*a1*np.sin(bib.DegToRad(e/2))/np.sqrt(1-(n_l1*np.sin(bib.DegToRad(e/2)))**2)
A2 = (d_lton(l2, *p))*2*a1*np.sin(bib.DegToRad(e/2))/np.sqrt(1-(n_l2*np.sin(bib.DegToRad(e/2)))**2)
print(A1)
print(A2)

a2=10**-3
A3 = (d_lton(l1, *p))*2*a2*np.sin(bib.DegToRad(e/2))/np.sqrt(1-(n_l1*np.sin(bib.DegToRad(e/2)))**2)
A4 = (d_lton(l2, *p))*2*a2*np.sin(bib.DegToRad(e/2))/np.sqrt(1-(n_l2*np.sin(bib.DegToRad(e/2)))**2)
print(A3)
print(A4)
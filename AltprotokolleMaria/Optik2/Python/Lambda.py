# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 01:18:35 2018

@author: Apoca1yptica
"""

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *

Rohdaten=np.genfromtxt("Rohdatenl.txt")
print(len(Rohdaten))
serr=0.01/np.sqrt(12)*np.ones(28)*10**-3
merr=1./np.sqrt(12)*np.ones(28)
m=np.array([])
s=np.array([])
for i in range(28):
    s=np.append(s, Rohdaten[i])
    m=np.append(m, (i)*10)
s=s*10**-3
#k=0.04685502878801657
#kerr=7.165372679836135e-05
k=0.04713889034
kerr=0.00046389398
yerr1=(2*k*serr)
yerr2=(2*(k-kerr)*serr)
yerr3=(2*(k+kerr)*serr)
print(yerr1)

a1,ea1,b1,eb1,chiq1,corr1 = analyse.lineare_regression_xy(m,s*2*k,merr,yerr1)
print(a1,ea1,b1,eb1,chiq1,corr1)
print(chiq1/26)

a2,ea2,b2,eb2,chiq2,corr2 = analyse.lineare_regression_xy(m,s*2*(k-kerr),merr,yerr2)
print(a2,ea2,b2,eb2,chiq2,corr2)
print(chiq2/26)

a3,ea3,b3,eb3,chiq3,corr3 = analyse.lineare_regression_xy(m,s*2*(k+kerr),merr,yerr3)
print(a3,ea3,b3,eb3,chiq3,corr3)
print(chiq3/26)

print(a1-a2)
print(a3-a1)

xwerte=m
ywerte=s*2*k
eywerte=yerr1
exwerte=merr

ywerte2=s*2*(k-kerr)
eywerte2=yerr2

ywerte3=s*2*(k+kerr)
eywerte3=yerr3

def anpassung1(x):
    return a1*(x)+b1
name="Lambdagruen"

figure()
#title('Lineare Regression des Übersetzungsfaktors')
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, anpassung1(xwerte), '-')
xlabel('m')
ylabel('$2s\\cdot k  [m]$')
legend(title='Fit \n$f(x)=ax+b$,  $x=m$ \n$a=${:.5e} $m$ $\pm$ {:.2e} $m$ \n$b=${:.5e} $m$ $\pm$ {:.2e} $m$ \n$n=28$'.format(a1,ea1,b1,eb1))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
#title('Residuenplot des Übersetzungsfaktors')
errorbar(x=xwerte, y=ywerte-anpassung1(xwerte), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte,0.*ywerte, zorder=2) # Linie bei Null 
ylabel('$2s\\cdot k-fit  [m]$')
xlabel('m')
legend(title='Residuenplot \n $\chi^2/n_{{df}}$ = {:.2f}'.format(chiq1/(len(xwerte)-2)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()

def anpassung2(x):
    return a2*(x)+b2


figure()
#title('Lineare Regression des Übersetzungsfaktors')
errorbar(x=xwerte, y=ywerte2, yerr=eywerte2, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, anpassung2(xwerte), '-')
xlabel('m')
ylabel('$2s\\cdot k  [m]$')
legend(title='Fit \n$f(x)=ax+b$,  $x=m$ \n$a=${:.5e} $m$ $\pm$ {:.2e} $m$ \n$b=${:.5e} $m$ $\pm$ {:.2e} $m$ \n$n=28$'.format(a2,ea2,b2,eb2))
savefig('{}_LinReg2.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
#title('Residuenplot des Übersetzungsfaktors')
errorbar(x=xwerte, y=ywerte2-anpassung2(xwerte), yerr=eywerte2, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte,0.*ywerte, zorder=2) # Linie bei Null 
ylabel('$2s\\cdot k-fit  [m]$')
xlabel('m')
legend(title='Residuenplot \n $\chi^2/n_{{df}}$ = {:.2f}'.format(chiq2/(len(xwerte)-2)))
savefig('{}_Residuen2.pdf'.format(name), bbox_inches = 'tight')

show()

def anpassung3(x):
    return a3*(x)+b3

figure()
#title('Lineare Regression des Übersetzungsfaktors')
errorbar(x=xwerte, y=ywerte3, yerr=eywerte3, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, anpassung3(xwerte), '-')
xlabel('m')
ylabel('$2s\\cdot k  [m]$')
legend(title='Fit \n$f(x)=ax+b$,  $x=m$ \n$a=${:.5e} $m$ $\pm$ {:.2e} $m$ \n$b=${:.5e} $m$ $\pm$ {:.2e} $m$ \n$n=28$'.format(a3,ea3,b3,eb3))
savefig('{}_LinReg3.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
#title('Residuenplot des Übersetzungsfaktors')
errorbar(x=xwerte, y=ywerte3-anpassung3(xwerte), yerr=eywerte3, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte,0.*ywerte, zorder=2) # Linie bei Null 
ylabel('$2s\\cdot k-fit  [m]$')
xlabel('m')
legend(title='Residuenplot \n $\chi^2/n_{{df}}$ = {:.2f}'.format(chiq3/(len(xwerte)-2)))
savefig('{}_Residuen3.pdf'.format(name), bbox_inches = 'tight')

show()

figure()
#title('Lineare Regression des Übersetzungsfaktors')
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1, color="black")
errorbar(x=xwerte, y=ywerte2, yerr=eywerte2, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1, color="red")
errorbar(x=xwerte, y=ywerte3, yerr=eywerte3, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1, color="green")
plot(xwerte, anpassung1(xwerte), '-', label="Anpassung mit k", color="black")
plot(xwerte, anpassung2(xwerte), '-', label="Anpassung mit k-$\sigma_k$", color="red")
plot(xwerte, anpassung3(xwerte), '-', label="Anpassung mit k+$\sigma_k$", color="green")
xlabel('m')
ylabel('$2s\\cdot k  [m]$')
legend()
savefig('{}_LinReg4.pdf'.format(name), bbox_inches = 'tight')
show()
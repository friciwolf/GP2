#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:02:08 2019

@author: Mate
"""

import numpy as np
import matplotlib.pyplot as plt
import praktikum_addons.bib as bib

#Q aus Messgrößen

R_1 = np.array([0, 1/99.15, 1/46.60]) #R**-1
eR_1 = np.array([0, 0.0025/99.15, 0.0025/46.60])
R_o = np.array([99.15, 46.60])
eR_o = 0.25*10**-2*R_o
R_L = 3.749
eR_L = 0.0025*R_L
L = 4.831*10**-3 #H
eL = 0.0025*L
C = 4.717*10**-6 #F
eC = 0.0025*C
Q = []
Q.append(R_L**-1 * np.sqrt(L/C))

def Q_p(R):
    Q_1 = (R**-1)*np.sqrt(L/C)+R_L*np.sqrt(C/L)
    return Q_1**-1

def eQ_p_1(R, eR): #Fehler auf Q_p**-1
    eQ_1 = np.sqrt(eR**2*L/(C*R**4)+eR_L**2*C/L+(((R*np.sqrt(L*C))**-1-R_L*np.sqrt(C/L)/L)**2)*eL**2/4+((R_L/np.sqrt(L*C)-np.sqrt(L/C)/(R*C))**2)*eC**2/4)
    return eQ_1

x = R_1 #R**-1
ex = eR_1
y = np.array([R_L*np.sqrt(C/L)]) #Q**-1
y = np.append(y,Q_p(R_1[1:]**-1)**-1)
ey = np.array([y[0]*np.sqrt((eR_L/R_L)**2+0.25*(eC/C)**2+0.25*(eL/L)**2)])
ey = np.append(ey,eQ_p_1(R_o, eR_o))
ax1, ax2, a,ea,b,eb,chiq, corr = bib.pltmitres(x,y,ey,ex, regData=True, xl="$R^{-1} [\Omega^{-1}]$", yl="$Q^{-1}$")
ax1.legend(title="Lineare Regression\n{} = ({:.6f} ± {:.6f}){} $\cdot$ {}+({:.6f}±{:.6f}){}".format("$Q^{-1}$",a,ea, "/$\Omega^{-1}$","$R^{-1}$",b, eb, "", loc=1))
ax1.set_ylim(top=1.5)
plt.show()
plt.close()
print("Aus den Messgrößen erhält man:")
for i in range(len(x)):
    print("Q=",y[i]**-1, "+-", ey[i]*y[i]**-2, "für R^-1=", R_1[i])
    
#Plot der LSG:
#47,100,inf
#R=47
s = ["47", "100", "inf"]
Q = np.array([1.244, 1.22 , 1.23])
eQstat = np.array([0.0, 0.04 , 0.01])
eQsys = np.array([0.003, 0.01 , 0.03])

e = np.sqrt(eQstat**2+eQsys**2)
x = ["Erwartung", "Stromminimum", "Stromüberhöhung"]
plt.errorbar(x,Q,e, linestyle="None", marker="o")
i=0
plt.savefig("P"+s[i]+"_Fazit.pdf")
plt.show()
#R=100
Q = np.array([2.273, 2.12 , 2.17])
eQstat = np.array([0.0, 0.09 , 0.02])
eQsys = np.array([0.005, 0.05 , 0.08])
e = np.sqrt(eQstat**2+eQsys**2)
x = ["Erwartung", "Stromminimum", "Stromüberhöhung"]
plt.errorbar(x,Q,e, linestyle="None", marker="o")
i=1
plt.savefig("P"+s[i]+"_Fazit.pdf")
plt.show()

#R=inf
Q = np.array([8.536, 5.18 , 5.76])
eQstat = np.array([0.0, 0.35 , 0.46])
eQsys = np.array([0.026, 0.12 , 0.32])
e = np.sqrt(eQstat**2+eQsys**2)
x = ["Erwartung", "Stromminimum", "Stromüberhöhung"]
plt.errorbar(x,Q,e, linestyle="None", marker="o")
i=2
plt.savefig("P"+s[i]+"_Fazit.pdf")
plt.show()
#R = 47Ω
#R = 100Ω
#R=∞
#Erwartung/Messbrücke Stromminimum Stromüberhöhung
#1.244 ± 0.003(sys.) 1.22 ± 0.04 ± 0.01 1.23 ± 0.01 ± 0.03
#2.273 ± 0.005(sys.) 2.12 ± 0.09 ± 0.05 2.17 ± 0.02 ± 0.08
#8.536 ± 0.026(sys.) 5.18 ± 0.35 ± 0.12 5.76 ± 0.46 ± 0.32

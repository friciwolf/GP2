#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:00:39 2019

@author: Mate
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
import praktikum.analyse as anal
import praktikum.cassy1 as cassy1

def pltmitres(x,y,ex,ey, xl, yl, xeinheit, yeinheit, titel):
    """
    Zum Erstellen eines Plots mit dazugehörigem Residumplot
    
    Parameter:
        x, y, ex, ey - Daten mit Fehler
        xl, yl : Titel der Achsen
        xeinheit, yeinheit : Einheit der Werte als String
        titel : titel des Plots
    Verwendung:
        x = np.arange(0.1,1,0.1)
        y = np.sin(x)
        ex = np.ones(len(x))*0.5
        ey = np.ones(len(y))*0.2
        pltmitres(x,y, ex, ey, "x", "y", "m/s", "s", "titel")
        plt.show()
    """
    x = np.array(x)
    y = np.array(y)
    ex = np.array(ex)
    ey = np.array(ey)
    a,ea,b,eb,chiq,corr = anal.lineare_regression(x,y,ey)
    
    gs1 = GridSpec(3, 5)
    
    plt.subplot(gs1[:-1,:-1])
    plt.title(titel)
    plt.errorbar(x,y, ey, ex, marker="x", linestyle="None", capsize=5)
    l = max(x)-min(x)
    x2 = np.arange(min(x)-l*0.1, max(x)+l*0.1, l/1000)
    y2 = a*x2+b
    plt.plot(x2, y2, color="orange")
    plt.ylabel(yl+" [{}]".format(xeinheit))
    plt.ylim(top=15)
    plt.legend(title="Lineare Regression\n{} = ({:.4f} ± {:.4f}){}/{} $\cdot$ {}+({:.4f}±{:.4f}){}\n$\chi^2 /NDF={:.2f}$".format(yl,a,ea, xeinheit, yeinheit,xl,b, eb, xeinheit, chiq/(len(x)-2)), loc=1)
    
    plt.subplot(gs1[2, :-1])
    plt.errorbar(x,y-a*x-b, np.sqrt(ex**2*a**2+ey**2), marker="x", linestyle="None", capsize=5)
    plt.axhline(0, color="orange")
    plt.xlabel(xl+" [{}]".format(yeinheit))
    
    plt.tight_layout()
    return a, ea, b, eb, chiq

data = cassy1.lese_lab_datei("../Winkelkal.lab")
R = data[:,3]
phi = data[:,5]

eR = np.ones(len(R))*0.005 #nehme als statistische Fehler den Digitalisirungsfehler - chiq akzeptabel

a, ea, b, eb, chiq = pltmitres(phi, R, np.ones(len(R))*0, eR, "$\phi$", "R", "$k\Omega$", "°", "")
plt.savefig("../Images/Winkelkalib.pdf")
plt.show()
print("Lineare Regression\n{} = ({:.4f} ± {:.4f}){}/{} * {}+({:.4f}±{:.4f}){}\nchi^2 /NDF={:.2f}".format("R",a,ea, "kOhm", "°","phi",b, eb, "°", chiq/(len(R)-2)))
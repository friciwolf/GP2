#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:26:54 2019

@author: Mate
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

import praktikum.analyse as anal

def c_open(file):
    """
    Zum Einlesen der CASSY-Messungen
    Parameter: file - Messdatei
    returns: R, U
    """
    data = cassy.CassyDaten(file)
    R = data.messung(1).datenreihe("R_B1").werte
    U = data.messung(1).datenreihe("U_A1").werte
    return np.array(R), np.array(U)

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
    a,ea,b,eb,chiq,corr = anal.lineare_regression_xy(x,y,ex,ey)
    
    gs1 = GridSpec(3, 3)
    
    plt.subplot(gs1[:-1,:-1])
    plt.title(titel)
    plt.errorbar(x,y, ex, ey, marker="x", linestyle="None", capsize=5)
    l = max(x)-min(x)
    x2 = np.arange(min(x)-l*0.1, max(x)+l*0.1, l/1000)
    y2 = a*x2+b
    plt.plot(x2, y2, color="orange")
    plt.ylabel(yl+" [{}]".format(xeinheit))
    plt.legend(title="Lineare Regression\n{} = ({:.2f} ± {:.2f}){} $\cdot$ {}+({:.2f}±{:.2f}){}\n$\chi^2 /NDF={:.2f}$".format(yl,a,ea, xeinheit,xl,b, eb, yeinheit, chiq/(len(x)-2)), loc=1)
    
    plt.subplot(gs1[2, :-1])
    plt.errorbar(x,y-y, np.sqrt(ex**2*a+ey**2), marker="x", linestyle="None", capsize=5)
    plt.axhline(0, color="orange")
    plt.xlabel(xl+" [{}]".format(yeinheit))
    
    plt.tight_layout()
    
x = np.arange(0.1,1,0.1)
y = np.sin(x)
ex = np.ones(len(x))*0.5
ey = np.ones(len(y))*0.2
pltmitres(x,y, ex, ey, "x", "y", "m/s", "s", "titel")
plt.show()
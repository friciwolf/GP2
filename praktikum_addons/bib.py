#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:26:54 2019

@author: Mate
"""

import matplotlib.pyplot as plt
import numpy as np
import praktikum.analyse as anal
import praktikum.cassy as cassy

def c_open(file, symbols, messungsnr=1):
    """
    Zum Einlesen der CASSY-Messungen
    
    Parameter:
        :param file: Messdatei
        :param symbols: Bezeichnung der Datenreihen z.B. R_B1, U_A1 als string
        :param messungsnr: Nummer der Messung (default: 1)
        :rtype: Array der Messdaten, also output[0] <=> R_B1, output[1] <=> U_A1 
    Verwendung:
        import praktikum_addons.bib as bib
        x,y = bib.c_open("../doppel_1.lab", ["R_B1","U_A1"])
    """
    data = cassy.CassyDaten(file)
    N = len(data.messung(messungsnr).datenreihe(symbols[0]).werte)
    output = np.zeros((len(symbols),N))
    for i in range(len(symbols)):
        output[i] = data.messung(messungsnr).datenreihe(symbols[i]).werte
    return output

def index_element(x0, x):
    """
    Gibt den Index eines Elements x0 im Array x. Gibt -1 aus, falls nicht gefunden
    """
    for n in range(len(x)):
        if x0==x[n]: return n
    return -1

def DegToRad(x):
    """
    Rechnet Daten in Radian um
    """
    return x*np.pi/180

def chiq(fxi,yi, eyi):
    fxi = np.array(fxi)
    yi = np.array(yi)
    eyi = np.array(eyi)
    return np.sum(((yi-fxi)/eyi)**2)

def finde_Knoten(x, y, I=30):
    """
    Sucht nach Knotenpunkte(=Minima) im Intervall von I um jeden Wert. Bei Gleichheit, nehme den Linken
    
    Returns:
        :rtype: i_kn Indizes der Punkte
        :rtype: x_kn x-Werte der Punkte
    """
    x_kn = []
    i_kn = []
    for i in range(I, len(x)-I):
        minumum = True
        for i2 in range(i-I, i+I):
            if y[i2]<y[i]:
                minumum=False
        if (minumum and x[i] not in x_kn):
            x_kn.append(x[i])
            i_kn.append(i)
    return np.array(i_kn), np.array(x_kn)

def pltmitres(x,y,ey,ex=0, xl="x", yl="y", xeinheit="", yeinheit="", title="", ratios=[2,1], regData=False, capsize=5, markersize=5):
    """
    Erstellen eines Plots mit dazugehörigem Residumplot
    
    Parameter:
        :param x,y,ex,ey: Daten mit Fehler
        :param xl,yl: Titel der Achsen
        :param xeinheit,yeinheit: Einheit der Werte als String
        :param titel: Titel des Plots
        :param ratios: Flächenverhältnis zwischen Daten- und Residumplot
        :param regData: Falls wahr, a,ea,b,eb,chiq,corr der Regression werden auch zurückgegeben
    
    Returns:
        :rtype fig, ax1, ax2 - Figurenplot, Achsen des Datenplots bzw. Residumplots 
    Verwendung:
        import numpy as np
        import praktikum_addons.bib as bib
        import matplotlib.pyplot as plt
        
        x = np.arange(0.1,1.3,0.1)
        y = np.sin(x)
        ex = np.ones(len(x))*0.03
        ey = np.ones(len(y))*0.1
        fig,ax1, ax2 = bib.pltmitres(x,y, ex, ey, yeinheit = "s", xeinheit="m", ratios=[7,1])
        ax1.set_ylim(top=2)
        plt.show()
    """
    x = np.array(x)
    y = np.array(y)
    ex = np.array(ex)
    ey = np.array(ey)
    if ex==0: a,ea,b,eb,chiq,corr = anal.lineare_regression(x,y,ey)
    else: a,ea,b,eb,chiq,corr = anal.lineare_regression_xy(x,y,ex,ey)
    
    fig, (ax1,ax2) = plt.subplots(2, 1,gridspec_kw = {'height_ratios':ratios})
    
    plt.title(title)
    ax1.errorbar(x,y, ey, np.ones(len(x))*ex, marker="x", linestyle="None", capsize=capsize, markersize=markersize)
    l = max(x)-min(x)
    x2 = np.arange(min(x)-l*0.1, max(x)+l*0.1, l/1000)
    y2 = a*x2+b
    ax1.plot(x2, y2, color="orange")
    if yeinheit!="": ax1.set_ylabel(yl+" [{}]".format(yeinheit))
    else: ax1.set_ylabel(yl)
    ax1.legend(title="Lineare Regression\n{} = ({:.2f} ± {:.2f}){} $\cdot$ {}+({:.2f}±{:.2f}){}\n$\chi^2 /NDF={:.4f}$".format(yl,a,ea, yeinheit+"/"+xeinheit,xl,b, eb, yeinheit, chiq/(len(x)-2)), loc=1)
    
    ax2.errorbar(x,y-a*x-b, np.sqrt(ex**2*a**2+ey**2), marker="x", linestyle="None", capsize=capsize, markersize=markersize)
    ax2.axhline(0, color="orange")
    if xeinheit!="": plt.xlabel(xl+" [{}]".format(xeinheit))
    else: plt.xlabel(xl)

    plt.tight_layout()
    if regData: return ax1, ax2, a,ea,b,eb,chiq,corr
    else: return ax1, ax2
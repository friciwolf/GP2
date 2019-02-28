#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:43:49 2019

@author: Mate
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
import praktikum.cassy1 as cassy1
from scipy.signal import find_peaks
import praktikum.analyse as anal

l = 0.9736 #in cm
pi = np.pi
a = 1.56
maxima = []
maxima_theo = []
einzelspalt_breite = []
doppelspalt_breite = []
doppelspalt_abstand = []
e_maxima = np.round(0.05/0.0263,2) #Ungefähr auf 0.05 Ohm Genauigkeit-diese kommt aber auf den Punkt an!
e_b = 0.1/np.sqrt(12)

def UtoI(U, a):
    return U**(2/a)

def RtoDeg(R, eR):
    return (R-6.872058823529412)/0.0263, eR/0.0263

def sinxdx2(x):
    return (np.sin(x)/x)**2

def sinNxdsinx2(x, N):
    return (np.sin(N*x)/np.sin(x))**2

def I(alpha, I0, b, d, N):
    """
    b, d in cm
    """
    if N==1:
        return I0 * sinxdx2(b*pi*np.sin(alpha)/l)
    else:
        return I0 * sinxdx2(b*pi*np.sin(alpha)/l) * sinNxdsinx2(d*pi*np.sin(alpha)/l,N)

def index_element(x0, x):
    for n in range(len(x)):
        if x0==x[n]: return n

def zentriere(phi, U):
    delta = 0
    i_peaks, _ = find_peaks(U, distance=12, width=11)
    max_phi = []
    max_U = []
    for i in i_peaks:
        max_phi.append(phi[i])
        max_U.append(U[i])
    null = np.min(np.abs(max_phi))
    i_null = index_element(null,np.abs(max_phi))
    delta = (max_phi[i_null+1]+max_phi[i_null-1])*0.5
    return phi-delta, delta, np.array(max_phi)-delta, np.array(max_U)

def Einzelspalt(file, b, debug):
    N = 1
    d = 0
    data = cassy1.lese_lab_datei(file)
    U = np.array(data[:,2])
    R = np.array(data[:,3])
    eR = np.ones(len(R))*0.005
    phi, ephi = RtoDeg(R, eR)
    
    #Plot der Rohdaten
    plt.plot(phi, U, label="Rohdaten")
    plt.xlabel("$\phi [°]$")
    plt.ylabel("U [V]")
    plt.legend(title="N=1, b="+str(b)+" cm")
    plt.savefig("../Images/einzelspalt_roh_"+str(b)+"_"+file[-5]+".pdf")
    plt.show()
    plt.close()
    
    phi, delta,peaks,U_p  = zentriere(phi,U)
    Intens = UtoI(U, a)
    
    #Maxima abspeichern
    null = np.min(np.abs(peaks))
    i_null = index_element(null,np.abs(peaks))
    peak_1_theo = np.arcsin(4.49341/pi*l/b)*180/pi
    maxima.append(np.round(peaks[i_null], 2))
    maxima.append(np.round(peaks[i_null+1], 2))
    maxima.append(np.round(peaks[i_null-1], 2))
    maxima_theo.append(0)
    if np.round(peaks[i_null+1])<0:
        maxima_theo.append(-np.round(peak_1_theo,2))
        maxima_theo.append(np.round(peak_1_theo,2))
    else:
        maxima_theo.append(np.round(peak_1_theo,2))
        maxima_theo.append(-np.round(peak_1_theo,2))
    einzelspalt_breite.append(b)
    einzelspalt_breite.append(b)
    einzelspalt_breite.append(b)
    
    plt.plot(peaks, UtoI(U_p,a), linestyle="None", marker="x")
    
    if debug: #Zeige die Maxima und den nicht verschobenen Plot an
        plt.axvline(delta)
        phi2, ephi2 = RtoDeg(R, eR)
        plt.plot(phi2, Intens, label = "$I_0$")

    plt.xlabel("$\phi [°]$")
    plt.ylabel("Relative Intensität")
    plt.plot(phi, Intens, label = "I")
    plt.plot(phi, I(phi*pi/180, max(Intens),b,d,N), label = "$I_{theo}$")
    plt.legend(title="N=1, b="+str(b)+" cm")
    plt.savefig("../Images/einzelspalt_"+str(b)+"_"+file[-5]+".pdf")
    plt.show()
    plt.close()
    
def Doppelspalt(file, b, d, debug):
    N = 2
    data = cassy1.lese_lab_datei(file)
    U = np.array(data[:,2])
    R = np.array(data[:,3])
    eR = np.ones(len(R))*0.005
    phi, ephi = RtoDeg(R, eR)
    
    #Plot der Rohdaten
    plt.plot(phi, U, label="Rohdaten")
    plt.xlabel("$\phi [°]$")
    plt.ylabel("U [V]")
    plt.legend(title="N=2, b="+str(b)+" cm, d="+str(d)+ " cm")
    plt.savefig("../Images/doppelspalt_roh_"+file[-5]+".pdf")
    plt.show()
    plt.close()

    phi, delta,peaks,U_p = zentriere(phi,U)    
    Intens = UtoI(U, a)
    
    #Maxima abspeichern
    null = np.min(np.abs(peaks))
    i_null = index_element(null,np.abs(peaks))
    peak_1_theo = np.arcsin(l/d)*180/pi
    maxima.append(np.round(peaks[i_null], 2))
    maxima.append(np.round(peaks[i_null+1], 2))
    maxima.append(np.round(peaks[i_null-1], 2))
    maxima_theo.append(0)
    if np.round(peaks[i_null+1])<0:
        maxima_theo.append(-np.round(peak_1_theo,2))
        maxima_theo.append(np.round(peak_1_theo,2))
    else:
        maxima_theo.append(np.round(peak_1_theo,2))
        maxima_theo.append(-np.round(peak_1_theo,2))
    doppelspalt_breite.append(b)
    doppelspalt_breite.append(b)
    doppelspalt_breite.append(b)
    doppelspalt_abstand.append(d)
    doppelspalt_abstand.append(d)
    doppelspalt_abstand.append(d)
    
    plt.plot(peaks, UtoI(U_p,a), linestyle="None", marker="x", markersize=5)
        
    if debug: #Zeige die Maxima und den nicht verschobenen Plot an
        plt.axvline(delta)
        phi2, ephi2 = RtoDeg(R, eR)
        plt.plot(phi2, Intens, label = "$I_0$")

    plt.xlabel("$\phi [°]$")
    plt.ylabel("Relative Intensität")
    plt.plot(phi, Intens, label = "I")
    plt.plot(phi, I(phi*pi/180, max(Intens)/(N**2),b,d,N), label = "$I_{theo}$")
    plt.legend(title="N=2, b="+str(b)+" cm, d="+str(d)+ " cm")
    plt.savefig("../Images/doppelspalt_"+file[-5]+".pdf")
    plt.show()
    plt.close()

################################################
#Plot der Messungen
################################################
Einzelspalt("../einzel3cm_1.lab",3,False)
Einzelspalt("../einzel3cm_2.lab",3,False)
Einzelspalt("../einzel3cm_3.lab",3,False)
Einzelspalt("../einzel3cm_4.lab",3,False)

Einzelspalt("../einzel4cm_1.lab",4,False)
Einzelspalt("../einzel4cm_2.lab",4,False)
Einzelspalt("../einzel4cm_3.lab",4,False)
Einzelspalt("../einzel4cm_4.lab",4,False)

Doppelspalt("../doppel_1.lab",2.4,4.9,False)
Doppelspalt("../doppel_2.lab",2.4,4.9,False)
Doppelspalt("../doppel_3.lab",1.8,4.3,False)

print("Die gefundenen Maxima liegen bei:")
for i in range(len(maxima)):
    if (i)%3==0 and i<8*3:
        print("b=",einzelspalt_breite[i], "cm:")
        print("{:16} | {:5}".format("max_gem", "max_theo"))
    elif (i)%3==0 and i>=8*3:
        print("b=",doppelspalt_breite[i-24], "cm:")
        print("d=",doppelspalt_abstand[i-24], "cm:")
        print("{:16} | {:5}".format("max_gem", "max_theo"))
    print("{:6} +- {:6} | {:5}".format(maxima[i], e_maxima, maxima_theo[i]))
wellenlaenge = []
e_wellenlaenge = []
for i in range(len(maxima)):
    if (i)%3!=0 and i<8*3:
        wellenlaenge.append(einzelspalt_breite[i]*np.sin(maxima[i]*pi/180)*pi/4.49341)
        e_wellenlaenge.append(pi/4.49341*np.sqrt((einzelspalt_breite[i]*np.cos(maxima[i]*pi/180)*e_maxima*(pi/180))**2+(np.sin(maxima[i]*pi/180)*e_b)**2))
    elif (i)%3!=0 and i>=8*3:
        wellenlaenge.append(doppelspalt_abstand[i-24]*np.sin(maxima[i]*pi/180))
        e_wellenlaenge.append(np.sqrt((doppelspalt_abstand[i-24]*np.cos(maxima[i]*pi/180)*e_maxima*pi/180)**2+(np.sin(maxima[i]*pi/180)*e_b)**2))
print(np.abs(wellenlaenge))
print(np.average(np.abs(wellenlaenge)))
print(e_wellenlaenge) #TODO: Fehler besser abschätzen?
print(anal.gewichtetes_mittel(np.array(np.abs(wellenlaenge)), np.array(e_wellenlaenge)))



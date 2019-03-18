#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:12:02 2019

@author: maria
"""
from __future__ import print_function

from praktikum import cassy1
from praktikum import cassy
import praktikum.analyse as anal
import numpy as np
from pylab import *


f, UC, U0, UR= np.genfromtxt('../Daten/50HzFourier.txt', skip_header=5, usecols=(1,7,8,9), unpack=True)



f=f*1000


C = 4.717e-6
R47 = 46.60

figure(figsize=((13,6)))
plot(f,U0, color='blue', label='$FFT(U_0)$')
plot(f,UC, color='orange', label='$FFT(U_C)$')
legend()
xlim(0,7000)
#ylim(0,3)
ylabel('F(U) [V]')
xlabel('f [Hz]')
savefig('Fourier_UC_Rohdaten.pdf', bbox_inches = 'tight')
show()


figure(figsize=((13,6)))
plot(f,U0, color='blue', label='$FFT(U_0)$')
plot(f,UR, color='lightgreen', label='$FFT(U_R)$')
legend()
xlim(0,7000)
#ylim(0,0.5)
ylabel('F(U) [V]')
xlabel('f [Hz]')
savefig('Fourier_UR_Rohdaten.pdf', bbox_inches = 'tight')
show()


k=np.array(range(50))
fF=(2*k+1)*50
Koef=4/(np.pi*(2*k+1))
KoefC=Koef/np.sqrt(1+(fF*R47*C*2*np.pi)**2)
KoefR=Koef/np.sqrt(1+(1/(fF*R47*C*2*np.pi))**2)

figure(figsize=((12,6)))
plot(f,U0, color='blue', label='$FFT(U_0)$')
plot(f,UC, color='orange', label='$FFT(U_C)$')
scatter(fF,Koef, color='darkblue',label='Erwartung $F(U_0)$')
scatter(fF,KoefC, color='red', label='Erwartung $F(U_C)$')
legend()
xlim(0,2000)
ylim(0,0.5)
ylabel('F(U) [V]')
xlabel('f [Hz]')
savefig('Fourier_UC_Erwartung.pdf', bbox_inches = 'tight')
show()


figure(figsize=((12,6)))
plot(f,U0, color='blue', label='$FFT(U_0)$')
plot(f,UR, color='lightgreen', label='$FFT(U_R)$')
scatter(fF,Koef, color='darkblue',label='Erwartung $F(U_0)$')
scatter(fF,KoefR, color='green', label='Erwartung $F(U_R)$')
legend()
xlim(0,2000)
ylim(0,0.5)
ylabel('F(U) [V]')
xlabel('f [Hz]')
savefig('Fourier_UR_Erwartung.pdf', bbox_inches = 'tight')
show()
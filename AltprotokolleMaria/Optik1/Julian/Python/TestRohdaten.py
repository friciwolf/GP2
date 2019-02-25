from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *



Rohrohdaten = np.genfromtxt('Rohrohdaten.txt', skip_header=3)

print(Rohrohdaten)


CdHg_roh = np.array([[]])
for i in range(7):
    for j in range(3):
        CdHg_roh = np.append(CdHg_roh, [Rohrohdaten[i,0], Rohrohdaten[i,1]+Rohrohdaten[i,j+2]/60, Rohrohdaten[i,5]+Rohrohdaten[i,j+6]/60])
CdHg_roh=np.reshape(CdHg_roh, (7,3,3))

Zn_roh = np.array([[]])
for i in range(7,11):
    for j in range(3):
        Zn_roh = np.append(Zn_roh, [Rohrohdaten[i,0], Rohrohdaten[i,1]+Rohrohdaten[i,j+2]/60, Rohrohdaten[i,5]+Rohrohdaten[i,j+6]/60])
Zn_roh=np.reshape(Zn_roh, (4,3,3))

 




Rohrohdaten = np.genfromtxt('Rohrohdaten.txt', skip_header=2, max_rows=1)
print(Rohdaten0)
CdHg0 = np.array([[]])

for j in range(3):
    CdHg0 = np.append(CdHg0, [Rohrohdaten[0], Rohrohdaten[1]+Rohrohdaten[j+2]/60, Rohrohdaten[12]+Rohrohdaten[j+13]/60])
for j in range(3,10):
    CdHg0 = np.append(CdHg0, [Rohrohdaten[0], Rohrohdaten[1]+Rohrohdaten[j+2]/60, nan])
CdHg0=np.reshape(CdHg0, (1,10,3))

print(CdHg0)

CdHg01mean,std=analyse.mittelwert_stdabw(CdHg0[0,:,1])
print(CdHg01mean, std)






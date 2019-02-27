from __future__ import print_function

from praktikum import cassy1
from praktikum import cassy
import praktikum.analyse as anal
import numpy as np
from pylab import *

K,eK=np.genfromtxt('K.txt', unpack=True, usecols=(0,1))

wellenlaenge = []
ewellenlaenge = []
esyswellenlaenge = []


#stehwel1------------------------------------------------------------------------------------

data = cassy1.lese_lab_datei('../Rohdaten/stehwel1.lab')

startpoint=23
endpoint=1226

R = data[:,3]
U = data[:,2]
R_lim=R[startpoint:endpoint]
U_lim=U[startpoint:endpoint]


NKnoten = 75 #erster wird nicht mitgezählt
DeltaR = 2.961 - 0.678
eR = 0.003 # Ungenauigkeit der Knotenbestimmung                       3/4096/np.sqrt(12)=0.0002

eDeltaR = np.sqrt(2)*eR

figure(figsize=((10,3)))
plot(R,U, color='grey')
plot(R_lim, U_lim, color='black')
text(1.0, 0.85, "{} Knoten".format(NKnoten))
xlabel('R / $\\Omega$')
ylabel('U / V')
savefig('stehwel1.pdf', bbox_inches = 'tight')
show()


Wellenlaenge = DeltaR*K*2/NKnoten

eWellenlaenge = eDeltaR*K*2/NKnoten
esysWellenlaenge = DeltaR*eK*2/NKnoten


print("Wellenlänge1 = {:.4f} ± {:.4f}(stat) ± {:.4f}(sys) cm".format(Wellenlaenge, eWellenlaenge, esysWellenlaenge))

wellenlaenge.append(Wellenlaenge)
ewellenlaenge.append(eWellenlaenge)
esyswellenlaenge.append(esysWellenlaenge)



#stehwel2------------------------------------------------------------------------------------

data = cassy1.lese_lab_datei('../Rohdaten/stehwel2.lab')

startpoint=6
endpoint=592

R = data[:,3]
U = data[:,2]
R_lim=R[startpoint:endpoint]
U_lim=U[startpoint:endpoint]


NKnoten = 81 #erster wird nicht mitgezählt
DeltaR = 2.961 - 0.501
eR = 0.003 # Ungenauigkeit der Knotenbestimmung                       3/4096/np.sqrt(12)=0.0002

eDeltaR = np.sqrt(2)*eR

figure(figsize=((10,3)))
plot(R,U, color='grey')
plot(R_lim, U_lim, color='black')
text(1.0, 0.8, "{} Knoten".format(NKnoten))
text(1.0, 1.3, "Als Knoten mitgezählt", color="red")
plot(1.0665, 1.1265, "x", color="red")
xlabel('R / $\\Omega$')
ylabel('U / V')
savefig('stehwel2.pdf', bbox_inches = 'tight')
show()


Wellenlaenge = DeltaR*K*2/NKnoten

eWellenlaenge = eDeltaR*K*2/NKnoten
esysWellenlaenge = DeltaR*eK*2/NKnoten


print("Wellenlänge2 = {:.4f} ± {:.4f}(stat) ± {:.4f}(sys) cm".format(Wellenlaenge, eWellenlaenge, esysWellenlaenge))

wellenlaenge.append(Wellenlaenge)
ewellenlaenge.append(eWellenlaenge)
esyswellenlaenge.append(esysWellenlaenge)


#stehwel3------------------------------------------------------------------------------------

data = cassy1.lese_lab_datei('../Rohdaten/stehwel3.lab')

startpoint=7
endpoint=235

R = data[:,3]
U = data[:,2]
R_lim=R[startpoint:endpoint]
U_lim=U[startpoint:endpoint]


NKnoten = 30 #erster wird nicht mitgezählt
DeltaR = 2.9565 - 2.046
eR = 0.003 # Ungenauigkeit der Knotenbestimmung                       3/4096/np.sqrt(12)=0.0002

eDeltaR = np.sqrt(2)*eR

figure(figsize=((10,3)))
plot(R,U, color='grey')
plot(R_lim, U_lim, color='black')
text(1.0, 0.8, "{} Knoten".format(NKnoten))
xlabel('R / $\\Omega$')
ylabel('U / V')
savefig('stehwel3.pdf', bbox_inches = 'tight')
show()


Wellenlaenge = DeltaR*K*2/NKnoten

eWellenlaenge = eDeltaR*K*2/NKnoten
esysWellenlaenge = DeltaR*eK*2/NKnoten


print("Wellenlänge1 = {:.4f} ± {:.4f}(stat) ± {:.4f}(sys) cm".format(Wellenlaenge, eWellenlaenge, esysWellenlaenge))

wellenlaenge.append(Wellenlaenge)
ewellenlaenge.append(eWellenlaenge)
esyswellenlaenge.append(esysWellenlaenge)



#stehwel4------------------------------------------------------------------------------------

data = cassy1.lese_lab_datei('../Rohdaten/stehwel3.lab')

startpoint=246
endpoint=399

R = data[:,3]
U = data[:,2]
R_lim=R[startpoint:endpoint]
U_lim=U[startpoint:endpoint]


NKnoten = 19 #erster wird nicht mitgezählt
DeltaR = 1.9215 - 1.347
eR = 0.003 # Ungenauigkeit der Knotenbestimmung                       3/4096/np.sqrt(12)=0.0002

eDeltaR = np.sqrt(2)*eR

figure(figsize=((10,3)))
plot(R,U, color='grey')
plot(R_lim, U_lim, color='black')
text(1.0, 0.8, "{} Knoten".format(NKnoten))
xlabel('R / $\\Omega$')
ylabel('U / V')
savefig('stehwel4.pdf', bbox_inches = 'tight')
show()


Wellenlaenge = DeltaR*K*2/NKnoten

eWellenlaenge = eDeltaR*K*2/NKnoten
esysWellenlaenge = DeltaR*eK*2/NKnoten


print("Wellenlänge1 = {:.4f} ± {:.4f}(stat) ± {:.4f}(sys) cm".format(Wellenlaenge, eWellenlaenge, esysWellenlaenge))

wellenlaenge.append(Wellenlaenge)
ewellenlaenge.append(eWellenlaenge)
esyswellenlaenge.append(esysWellenlaenge)
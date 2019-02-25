from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *


a_kalib, ea_kalib=np.genfromtxt('a.txt', unpack=True)
ea_kalib=0.01

K,eK=np.genfromtxt('K.txt', unpack=True, usecols=(0,1))


data = cassy1.lese_lab_datei('Rohdaten/Polarisation.lab')


U = data[:,2]
phi = data[:,6]

phi=phi*np.pi/180


figure()
plot(phi*180/np.pi, U)
xlabel('$\\phi$ / Grad')
ylabel('U / V')
savefig('Polarisation_Rohdaten.pdf', bbox_inches = 'tight')
legend(title='Rohdaten')
show()
print('---------------- \n Die Kurven sind symmetrisch um 90 Grad, also ist keine Anpassung der phi-Nullage noetig \n --------------')

Umin=np.min(U)
I=(U-Umin)**(-2/a_kalib)
I_rel=(I/np.max(I))

figure()
plot(phi*180/np.pi, I_rel)
xlabel('$\\phi$ / Grad')
ylabel('I / $I_0$')
legend(title='Umwandlung von Spannung auf Intensität')
savefig('Polarisation_Intensitaet.pdf', bbox_inches = 'tight')
show()


I_rel0=np.delete(I_rel, [0,9,18,27,36])
phi0=np.delete(phi, [0,9,18,27,36])
U0=np.delete(U, [0,9,18,27,36])
print('phi0=',phi0)
logI0 = np.log(I_rel0)
logcosphi0=np.log(np.absolute(np.cos(phi0)))

ephi0=1/np.sqrt(12)*np.pi/180*np.ones(len(phi0)) # in radiant
eU0=0.0005*np.ones(len(U0))  #    0.6/4096/np.sqrt(12)*np.ones(len(U0))   #0.001

print('angenommenen Unsicherheiten: eU={}, ephi={}Grad'.format(eU0[0], ephi0[0]*180/np.pi))
print('Fehler auf U diesmal kleiner, weil Empfaenger und Sender recht dicht beieinander standen, fest installiert waren und dadurch das Rauschen einen geringeren Einfluss hat.')

elogI0=np.sqrt(((2/(a_kalib)**2)*np.log(U0-Umin)*ea_kalib)**2 + (2*eU0/(a_kalib*(U0-Umin)))**2)
elogcosphi0=np.absolute(np.sin(phi0)/np.cos(phi0))*ephi0
print('berechnete Fehler: elogI={}, elogcosphi={}'.format(elogI0, elogcosphi0))


x,ex,b,eb,chiq,corr = analyse.lineare_regression_xy(logcosphi0, logI0, elogcosphi0, elogI0)

print('Ergebnis: x=%f+-%f, b=%f+-%f, chi2=%f, corr=%f' % (x,ex,b,eb,chiq,corr))


figure()
#title('Lin. Reg. zum Gesetz von Malus')
errorbar(logcosphi0, logI0, xerr=elogcosphi0, yerr=elogI0, linestyle='none', marker='o', markersize=2, elinewidth=1, zorder=1)
plot(logcosphi0, x*logcosphi0+b,'-', zorder=2)
xlabel('$log(|cos(\\phi)|)$')
ylabel('$log(I/I_0)$')
legend(title='Lineare Regression \nSteigung: ${:.2f}\\pm{:.2f}$ \ny-Achsenabschnitt: ${:.3f}\\pm{:.3f}$ \nDatenpunkte: {}'.format(x, ex, b, eb, len(logcosphi0)))
savefig('Polarisation_LinReg.pdf', bbox_inches = 'tight')
show()


figure()
#title('Residuenplot Gesetz von Malus')
errorbar(logcosphi0, logI0-(logcosphi0*x+b), xerr=elogcosphi0, yerr=elogI0, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(logcosphi0, 0.*logcosphi0, zorder=2) # Linie bei Null 
xlabel('$log(|cos(\\phi)|)$')
ylabel('$log(I/I_0)$ - Fitgerade')
legend(title='Residuenplot \n $X^2/n$ = {:.2f}'.format(chiq/(len(logcosphi0)-2)))
savefig('Polarisation_Residuen.pdf', bbox_inches = 'tight')

show()


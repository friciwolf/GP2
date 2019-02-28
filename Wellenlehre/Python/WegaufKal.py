#Ultraschall

from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *


data = cassy1.lese_lab_datei('../Rohdaten/WegaufKal3.lab')

R = data[:,3]
d = data[:,5]



#------------------------------Rohdaten-Plot-----------------------------------

figure()
#title('Abstandskalibrierung Wegaufnehmer: Rohdaten')
plot(R, d, marker="o")
xlabel('R / k$\\Omega$')
ylabel('S / cm')
legend(title='Abstandskalibrierung Rohdaten')
savefig('WegaufKal_Rohdaten.pdf', bbox_inches = 'tight')

show()
close()





#-----------------------------Lineare Regresion----------------------------------

eR=3/4096/sqrt(12)*np.ones(len(R))                     #Binningfehler auf Widerstand in kOhm
ed=0.03*np.ones(len(d))#/sqrt(12)*np.ones(len(d))      #Ablesefehler Maßband in cm
d_mean=np.mean(d)
R_mean=np.mean(R)

a,ea,b,eb,chiq,corr = analyse.lineare_regression_xy(R-R_mean,d-d_mean,eR,ed)

print('Ergebnis: a=%f+-%f, b=%f+-%f, chi2=%f, corr=%f' % (a,ea,b,eb,chiq,corr))


def AbstandausW(Omega):
    return a*(Omega-R_mean)+b+d_mean

figure()
#title('Lineare Regression der Abstandskalibrierung')
errorbar(R, d, xerr=eR, yerr=ed, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(R, AbstandausW(R),'-', zorder=2)
xlabel('R / $k\\Omega$')
ylabel('S / cm')
legend(title='Lineare Regression \nSteigung [cm/k$\\Omega$]: ${:.3f}\\pm{:.3f}$ \ny-Achsenabschnitt[cm]: ${:.1f}\\pm{:.1f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(R-R_mean)))
savefig('WegaufKal_LinReg.pdf', bbox_inches = 'tight')
show()


figure()
#title('Residuenplot der Abstandskalibrierung')
errorbar(R, d-AbstandausW(R), yerr=np.sqrt((a*eR)**2+ed**2), linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(R, 0.*R, zorder=2) # Linie bei Null 
xlabel('R / $k\\Omega$')
ylabel('$(S-S_{fit})$ / cm')
legend(title='Residuenplot \n $X^2/n$ = {:.2f}'.format(chiq/(len(R-R_mean)-2)))
savefig('WegaufKal_Residuen.pdf', bbox_inches = 'tight')

show()

np.savetxt('K.txt', [[a, ea]], header='Kalibrierungsfaktor Wegaufnehmer in cm/kOhm, Fehler')
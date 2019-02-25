from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *


data = cassy1.lese_lab_datei('Rohdaten/Abstandskalibrierung.lab')

R = data[:,3]
d = data[:,5]


figure()
#title('Abstandskalibrierung Wegaufnehmer: Rohdaten')
plot(d,R, marker="o")
xlabel('R / k$\\Omega$')
ylabel('S / cm')
legend(title='Abstandskalibrierung Rohdaten')
savefig('Abstandskal_Rohdaten.pdf', bbox_inches = 'tight')

show()
close()


eR=10/4096/sqrt(12)*np.ones(len(R))                   #0.01
ed=0.1/sqrt(12)*np.ones(len(d))  #0.1
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
xlabel('R / $\\Omega$')
ylabel('S / cm')
legend(title='Lineare Regression \nSteigung: ${:.2f}\\pm{:.3f}$ \ny-Achsenabschnitt: ${:.2f}\\pm{:.3f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(R-R_mean)))
savefig('Abstandskal_LinReg.pdf', bbox_inches = 'tight')
show()


figure()
#title('Residuenplot der Abstandskalibrierung')
errorbar(R, d-AbstandausW(R), xerr=eR, yerr=ed, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(R, 0.*R, zorder=2) # Linie bei Null 
xlabel('R / $\\Omega$')
ylabel('$(S-S_{fit})$ / cm')
legend(title='Residuenplot \n $X^2/n$ = {:.2f}'.format(chiq/(len(R-R_mean)-2)))
savefig('Abstandskal_Residuen.pdf', bbox_inches = 'tight')

show()

np.savetxt('K.txt', [[a, ea, b, eb]])
from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *

data = cassy1.lese_lab_datei('Rohdaten/Winkelkalibration.lab')

R = data[:,3]
gamma = data[:,6]
gamma=gamma*np.pi/180

figure()
#title('Winkelaufnehmer: Rohdaten')
scatter(R,gamma, marker="o")
xlabel('R / k$\\Omega$')
ylabel('$\\gamma$ / Grad')
legend(title='Rohdaten Winkelkalibrierung')
savefig('Winkelkal_Rohdaten.pdf', bbox_inches = 'tight')

show()
close()


eR=10./4096./np.sqrt(12)*np.ones(len(R))
egamma=5/np.sqrt(12)*np.ones(len(gamma))*np.pi/180
gamma_mean=np.mean(gamma)
R_mean=np.mean(R)

K_winkel,eK_winkel,b,eb,chiq,corr = analyse.lineare_regression_xy(R-R_mean,gamma-gamma_mean,eR,egamma)

print('Ergebnis: a=%f+-%f, b=%f+-%f, chi2=%f, corr=%f' % (K_winkel,eK_winkel,b,eb,chiq,corr))


def AbstandausW(Omega):
    return K_winkel*(Omega-R_mean)+b+gamma_mean

figure()
#title('Lineare Regression der Winkelkalibrierung')
errorbar(R, gamma*180/np.pi, xerr=eR, yerr=egamma*180/np.pi, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(R, AbstandausW(R)*180/np.pi,'-', zorder=2)
xlabel('R / $\\Omega$')
ylabel('$\\gamma$ / Grad')
legend(title='Lineare Regression \nSteigung: ${:.2f}\\pm{:.3f}$ \ny-Achsenabschnitt: ${:.3f}\\pm{:.3f}$ \nDatenpunkte: {}'.format(K_winkel,eK_winkel, b, eb, len(R)))
savefig('Winkelkal_LinReg.pdf', bbox_inches = 'tight')
show()


figure()
#title('Residuenplot der Winkelkalibrierung')
errorbar(R, (gamma-AbstandausW(R))*180/np.pi, xerr=eR, yerr=egamma*180/np.pi, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(R, 0.*R, zorder=2) # Linie bei Null 
xlabel('R / $\\Omega$')
ylabel('$\\gamma-\\gamma_{fit}$ / Grad')
legend(title='Residuenplot \n $X^2/n$ = {:.2f}'.format(chiq/(len(R)-2)))
savefig('Winkelkal_Residuen.pdf', bbox_inches = 'tight')

show()



np.savetxt('winkelkalibrierung.txt', [[K_winkel, b, R_mean, gamma_mean, eK_winkel]], header='K_winkl, b, R_mean, gamma_mean')



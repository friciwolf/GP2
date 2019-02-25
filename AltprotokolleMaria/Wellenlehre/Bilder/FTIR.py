from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *

K_winkel, b, R_mean, gamma_mean, eK_winkel= np.genfromtxt('winkelkalibrierung.txt', unpack=True)
a, ea =np.genfromtxt('a.txt', unpack=True)

def GradausW(Omega):
    return (K_winkel*(Omega-R_mean)+b+gamma_mean)*180/np.pi


data01 = cassy1.lese_lab_datei('Rohdaten/FTIR1mm.lab')
data04 = cassy1.lese_lab_datei('Rohdaten/FTIR4mm.lab')
data10 = cassy1.lese_lab_datei('Rohdaten/FTIR10mm.2.lab')


g01 = data01[:,3]
U01 = data01[:,2]
g04 = data04[:,3]
U04 = data04[:,2]
g10 = data10[:,3]
U10 = data10[:,2]

I01=U01**(-2/a)
I04=U04**(-2/a)
I10=U10**(-2/a)

peakhightR=np.array([0.0075, 0.0204, 0.0285])**(-2/a)
peakposR=np.array([-63.5, -64.6, -66])
peakhightT=np.array([0.0275, 0.0132, 0.00315])**(-2/a)
peakposT=np.array([-0.2, 0, 1.04])


figure()
plot(g01, I01, label='D=1mm')
plot(g04, I04, label='D=4mm')
plot(g10, I10, label='D=10mm')

#text(peaks[i]+0.05, 0.011, '$\\gamma_{}$'.format(i))
ylabel('relative Intensität')
xlabel('$\\gamma$ / Grad')
legend()
savefig('FTIR_Rohdaten.pdf', bbox_inches = 'tight')
show()

Itot=peakhightR[0]+peakhightT[0]

logI=np.log((Itot-peakhightR)/Itot)
D=np.array([0.1,0.4,1.])

eD=0.1/sqrt(12)*np.ones(len(D))
eI=0.5*(np.max(peakhightR+peakhightT)-np.min(peakhightR+peakhightT))*np.ones(len(peakhightR))
elogI=np.ones(3)
for i in range(3):
    elogI[i]=peakhightR[i]*eI[i]/(Itot-peakhightR[i])*np.sqrt(1/(Itot)**2+1/(peakhightR[i])**2)


minusk,eminusk,b,eb,chiq,corr = analyse.lineare_regression_xy(D,logI,eD,elogI)

print('Ergebnis: a=%f+-%f, b=%f+-%f, chi2=%f, corr=%f' % (minusk,eminusk,b,eb,chiq,corr))


figure()
#title('Lin. Reg. zur Bestimmung zur FTIR')
errorbar(D,logI,xerr=eD,yerr=elogI, linestyle='none', marker='o', markersize=2, elinewidth=1, zorder=1)
plot(D, minusk*D+b,'-', zorder=2)
xlabel('D / cm')
ylabel('$log(I_T/I_{tot})$')
legend(title='Lineare Regression \nSteigung: ${:.1f}\\pm{:.1f}$ \ny-Achsenabschnitt: ${:.2f}\\pm{:.2f}$ \nDatenpunkte: {}'.format(minusk, eminusk, b, eb, len(D)))
savefig('FTIR_LinReg.pdf', bbox_inches = 'tight')
show()


figure()
#title('Residuenplot')
errorbar(D, logI-(D*minusk+b), xerr=eD, yerr=elogI, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(D, 0.*D, zorder=2) # Linie bei Null 
xlabel('D / cm')
ylabel('$log(I_T/I_{tot})$ - Fitgerade')
legend(title='Residuenplot \n $X^2/n$ = {:.2f}'.format(chiq/(len(D)-2)))
savefig('FTIR_Residuen.pdf', bbox_inches = 'tight')

show()

print(peakhightT)
print(peakhightR)

Wellenlaenge = - 2*np.pi / minusk
print(Wellenlaenge)


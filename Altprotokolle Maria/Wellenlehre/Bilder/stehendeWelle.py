from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *

K,eK=np.genfromtxt('K.txt', unpack=True, usecols=(0,1))

data = cassy1.lese_lab_datei('Rohdaten/Stehende Welle.lab')
startpoint=94
endpoint=562

R = data[:,3]
U = data[:,2]
R_lim=R[startpoint:endpoint]
U_lim=U[startpoint:endpoint]

Ri=np.array([5.904,6.313,6.713, 7.298,7.802, 8.398, 8.797, 9.187])
eRi=np.array([0.008,0.015,0.016, 0.018, 0.016,0.021, 0.011, 0.015])
indize=np.array([0,4, 8,14,19,25, 29, 33])



figure(figsize=((10,3)))
plot(R,U, color='grey')
plot(R_lim, U_lim, color='black')
for i in range(len(Ri)):
    axvline(x=Ri[i], color='red')
    text(Ri[i], 0.075, '$R_{{{}}}$={:.2f}'.format(indize[i], Ri[i]))
xlabel('R / $\\Omega$')
ylabel('U / V')
savefig('stehendeWelle.pdf', bbox_inches = 'tight')
show()


Wellenlaenge = (Ri[len(Ri)-1]-Ri[0])*K*2/33
print(Wellenlaenge)

print('1. Auswertung: gesamter Abstand=3.283 kOhm = 53.51cm ---- Wellenlaenge=3.24')






a,ea,b,eb,chiq,corr = analyse.lineare_regression(indize, Ri, eRi)
print('\n \n 2.Auswertung')
print('Ergebnis: a=%f+-%f, b=%f+-%f, chi2=%f, corr=%f' % (a,ea,b,eb,chiq,corr))


figure()
#title('Lin. Reg. der Widerstandpeaks bei stehenden Wellen')
errorbar(indize,Ri,yerr=eRi, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(indize, a*indize+b,'-', zorder=2)
xlabel('Peak Nummer i')
ylabel('R / $\\Omega$')
legend(title='Lineare Regression \nSteigung: ${:.4f}\\pm{:.4f}$ \ny-Achsenabschnitt: ${:.3f}\\pm{:.3f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(indize)))
savefig('stehendeWelle_LinReg.pdf', bbox_inches = 'tight')
show()


figure()
#title('Residuenplot stehende Wellen')
errorbar(indize, Ri-(indize*a+b), yerr=eRi, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(indize, 0.*indize, zorder=2) # Linie bei Null 
xlabel('Peak Nummer i')
ylabel('$(R-R_{fit})$ / $\\Omega$')
legend(title='Residuenplot \n $X^2/n$ = {:.2f}'.format(chiq/(len(indize)-2)))
savefig('stehendeWelle_Residuen.pdf', bbox_inches = 'tight')

show()

print(np.mean(eRi))


print('2.Auswertung: Pro Peak aendert sich der Widerstand um 0.0996, also ist die Wellenlaenge:')
print(a*2*K)



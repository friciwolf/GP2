from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *


data = cassy1.lese_lab_datei('Rohdaten/Abstandsmessung1.2.lab')

s_B1 = data[:,3]
U_A1 = data[:,2]

U_A1=U_A1[15:480]
s_B1=s_B1[15:480]



figure()
#title('Abstandsabhängigkeit der Spannung: Rohdaten')
scatter(s_B1, U_A1, s=1)
ylabel('U / V')
xlabel('s / cm')
ylim(0.01,0.1)
legend(title='Abstandsmessung Rohdaten')
savefig('Abstandsabh_Rohdaten.pdf', bbox_inches = 'tight')

show()
close()


ls_B1=np.log(s_B1)
lU_A1=np.log(U_A1)

es = 0.5/np.sqrt(12)*1/s_B1          #fehler durch schwieriges abmessen und schnelle Kalibration
eU = .002*1/(U_A1)       # 0.6 / 4096 / np.sqrt(12) * 1/(U_A1) 


a,ea,b,eb,chiq,corr = analyse.lineare_regression_xy(ls_B1,lU_A1,es,eU)

print('Ergebnis: a=%f+-%f, b=%f+-%f, chi2=%f, corr=%f' % (a,ea,b,eb,chiq,corr))

figure()
#title('Lineare Regression der Abstandsabhängigkeit')
errorbar(ls_B1, lU_A1, xerr=es, yerr=eU, linestyle='none', marker='o', markersize=2, elinewidth=1, zorder=1)
plot(ls_B1,a*ls_B1+b,'-', zorder=2)
xlabel('log(s/cm)')
ylabel('log(U/V)')
legend(title='Lineare Regression \nSteigung: ${:.2f}\\pm{:.2f}$ \ny-Achsenabschnitt: ${:.2f}\\pm{:.2f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(ls_B1)))
savefig('Abstandsabh_LinReg.pdf', bbox_inches = 'tight')
show()


figure()
#title('Residuenplot der Abstandsabhängigkeit')
errorbar(ls_B1,U_A1-np.exp((a*ls_B1+b)),xerr=es, yerr=eU*U_A1, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(ls_B1,0.*ls_B1, zorder=2) # Linie bei Null 
xlabel('log(s/cm)')
ylabel('$(U-U_{fit})$ / V')
legend(title='Residuenplot \n $X^2/n$ = {:.2f}'.format(chiq/(len(ls_B1)-2)))
savefig('Abstandsabh_Residuen.pdf', bbox_inches = 'tight')

show()

np.savetxt('a.txt', [[a,ea]])


'''
Auf die Strecke nehmen wir Unsicherheit von 0.5cm auf


'''

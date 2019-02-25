from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *

K_winkel, b, R_mean, gamma_mean, eK_winkel= np.genfromtxt('winkelkalibrierung.txt', unpack=True)
a, ea =np.genfromtxt('a.txt', unpack=True)

def GradausW(Omega):
    return (K_winkel*(Omega-R_mean)+b+gamma_mean)*180/np.pi

data00 = cassy1.lese_lab_datei('Rohdaten/Brechung0.lab')
data20 = cassy1.lese_lab_datei('Rohdaten/Brechung20.lab')
data40 = cassy1.lese_lab_datei('Rohdaten/Brechung40.lab')
data60 = cassy1.lese_lab_datei('Rohdaten/Brechung60.lab')


R00 = data00[:,3]
U00 = data00[:,2]
R20 = data20[:,3]
U20 = data20[:,2]
R40 = data40[:,3]
U40 = data40[:,2]
R60 = data60[:,3]
U60 = data60[:,2]

g00=GradausW(R00)
g20=GradausW(R20)
g40=GradausW(R40)
g60=GradausW(R60)

peaksW=np.array([7.789, 7.596, 7.387, 7.111])
epeaksW=np.array([0.219, 0.214, 0.210, 0.198])
peaks=GradausW(peaksW)
epeaks=K_winkel*epeaksW

figure()
plot(g00, U00, label='$\\alpha_1$=0°')
plot(g20, U20, label='$\\alpha_1$=20°')
plot(g40, U40, label='$\\alpha_1$=40°')
plot(g60, U60, label='$\\alpha_1$=60°')
for i in range(len(peaks)):
    axvline(x=peaks[i], color='black')
    text(peaks[i]+0.05, 0.011, '$\\gamma_{{1{}}}$'.format(i))
xlim(-40,60)
xlabel('$\\gamma_1$ / Grad')
ylabel('U / V')
legend()
savefig('Brechung_gamma.pdf', bbox_inches = 'tight')
show()
 
data2_40 = cassy1.lese_lab_datei('Rohdaten/Brechung40.2.lab')
#np.savetxt('test.txt', data2_40[:,2:4])



#--------------------------------------------------------------------------------------------------------


data2_00 = cassy1.lese_lab_datei('Rohdaten/Brechung0.2.lab')
data2_20 = cassy1.lese_lab_datei('Rohdaten/Brechung20.2.lab')
data2_40 = cassy1.lese_lab_datei('Rohdaten/Brechung40.2.lab')



R2_00 = data2_00[:,3]
U2_00 = data2_00[:,2]
R2_20 = data2_20[:,3]
U2_20 = data2_20[:,2]
R2_40 = data2_40[:,3]
U2_40 = data2_40[:,2]


g2_00=GradausW(R2_00)
g2_20=GradausW(R2_20)
g2_40=GradausW(R2_40)

peaksW2=np.array([7.825, 8.176, 8.65])
epeaksW2=np.array([0.087,0.118,0.5])
peaks2=GradausW(peaksW2)
epeaks2=K_winkel*epeaksW2

figure()
plot(g2_00, U2_00, label='$\\alpha_2$=0°')
plot(g2_20, U2_20, label='$\\alpha_2$=-20°')
plot(g2_40, U2_40, label='$\\alpha_2$=-40°')
for i in range(len(peaks2)):
    axvline(x=peaks2[i], color='black')
    text(peaks2[i]+0.05, 0.031, '$\\gamma_{{2{}}}$'.format(i))
xlabel('$\\gamma_2$ / Grad')
ylabel('U / V')
xlim(-60,30)
legend()

savefig('Brechung_gamma2.pdf', bbox_inches = 'tight')
show()
 


alpha=np.array([0,20,40,60])
beta=alpha-peaks
ealpha=5/np.sqrt(12)*np.ones(len(alpha))
esinalpha=np.absolute(np.cos(alpha*np.pi/180)*ealpha)
ebetasquare=ealpha**2+epeaks**2
ebeta=np.sqrt(ebetasquare)
esinbeta=np.absolute(np.cos(beta*np.pi/180)*ebeta)

'''
figure()
scatter(np.sin(beta*np.pi/180), np.sin(alpha*np.pi/180))
show()
'''


alpha2=np.array([0,-20,-40])
beta2=alpha2+peaks2
ealpha2=5/np.sqrt(12)*np.ones(len(alpha2))
esinalpha2=np.absolute(np.cos(alpha2*np.pi/180)*ealpha2)
ebeta2square=ealpha2**2+epeaks2**2
ebeta2=np.sqrt(ebeta2square)
esinbeta2=np.absolute(np.cos(beta2*np.pi/180)*ebeta2)








n,en,b,eb,chiq,corr = analyse.lineare_regression_xy(np.sin(beta*np.pi/180), np.sin(alpha*np.pi/180), esinbeta*np.pi/180, esinalpha*np.pi/180)

print('Ergebnis: a=%f+-%f, b=%f+-%f, chi2=%f, corr=%f' % (n,en,b,eb,chiq,corr))


figure()
#title('Lin. Reg. zur Bestimmung des Brechungsindexes')
errorbar(np.sin(beta*np.pi/180), np.sin(alpha*np.pi/180), xerr=esinbeta*np.pi/180, yerr=esinalpha*np.pi/180, linestyle='none', marker='o', markersize=2, elinewidth=1, zorder=1)
plot(np.sin(beta*np.pi/180), n*np.sin(beta*np.pi/180)+b,'-', zorder=2)
xlabel('$sin(\\beta_1)$')
ylabel('$sin(\\alpha_1)$')
legend(title='Lineare Regression \nSteigung: ${:.2f}\\pm{:.2f}$ \ny-Achsenabschnitt: ${:.2f}\\pm{:.2f}$ \nDatenpunkte: {}'.format(n, en, b, eb, len(np.sin(beta*np.pi/180))))
savefig('Brechung_LinReg.pdf', bbox_inches = 'tight')
show()


figure()
#title('Residuenplot')
errorbar(np.sin(beta*np.pi/180), np.sin(alpha*np.pi/180)-(np.sin(beta*np.pi/180)*n+b), xerr=esinbeta*np.pi/180, yerr=esinalpha*np.pi/180, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(np.sin(beta*np.pi/180), 0.*np.sin(beta*np.pi/180), zorder=2) # Linie bei Null 
xlabel('$sin(\\beta_1)$')
ylabel('$sin(\\alpha_1)$ - Fitgerade')
legend(title='Residuenplot \n $X^2/n$ = {:.3f}'.format(chiq/(len(np.sin(beta*np.pi/180))-2)))
savefig('Brechung_Residuen.pdf', bbox_inches = 'tight')

show()




n2,en2,b2,eb2,chiq2,corr2 = analyse.lineare_regression_xy(np.sin(alpha2*np.pi/180), np.sin(beta2*np.pi/180), esinalpha2*np.pi/180, esinbeta2*np.pi/180)

print('Ergebnis: a=%f+-%f, b=%f+-%f, chi2=%f, corr=%f' % (n2,en2,b2,eb2,chiq2,corr2))


figure()
#title('Lin. Reg. 2 zur Bestimmung des Brechungsindexes')
errorbar(np.sin(alpha2*np.pi/180), np.sin(beta2*np.pi/180), xerr=esinalpha2*np.pi/180, yerr=esinbeta2*np.pi/180, linestyle='none', marker='o', markersize=2, elinewidth=1, zorder=1)
plot(np.sin(alpha2*np.pi/180), n2*np.sin(alpha2*np.pi/180)+b2,'-', zorder=2)
ylabel('$sin(\\beta_2)$')
xlabel('$sin(\\alpha_2)$')
legend(title='Lineare Regression \nSteigung: ${:.2f}\\pm{:.2f}$ \ny-Achsenabschnitt: ${:.2f}\\pm{:.2f}$ \nDatenpunkte: {}'.format(n2, en2, b2, eb2, len(np.sin(alpha2*np.pi/180))))
savefig('Brechung_LinReg2.pdf', bbox_inches = 'tight')
show()


figure()
#title('Residuenplot')
errorbar(np.sin(alpha2*np.pi/180), np.sin(beta2*np.pi/180)-(np.sin(alpha2*np.pi/180)*n2+b2), esinalpha2*np.pi/180, esinbeta2*np.pi/180, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(np.sin(alpha2*np.pi/180), 0.*np.sin(alpha2*np.pi/180), zorder=2) # Linie bei Null 
ylabel('$sin(\\beta_2)$ - Fitgerade')
xlabel('$sin(\\alpha_2)$')
legend(title='Residuenplot \n $X^2/n$ = {:.2f}'.format(chiq2/(len(np.sin(alpha2*np.pi/180))-2)))
savefig('Brechung_Residuen2.pdf', bbox_inches = 'tight')

show()

print(peaks)
print(epeaks)
print(peaks2)
print(epeaks2)

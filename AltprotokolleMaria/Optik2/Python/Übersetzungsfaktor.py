# -*- coding: utf-8 -*-

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *



serr=0.01/np.sqrt(12)  # in mm
merr=1./np.sqrt(12)   # wir gehen davon aus, dass wir uns in 10Schritt maximal um eine ordnung verzaehlen, und das Ausmass der verzaehlung einer Gleicherteilung folgt


lambdaHeNe=632.8*10**-9
lambdaerr=0.1*10**-9

Rohdaten=np.genfromtxt("Rohdaten.txt")

s=Rohdaten #  in mm

#m=np.array([0,10,11,10,11,11,10,10,11,10,11,11,12,10,12,10,11,11,10,11,11,11,11,10,11])
#m=np.array([0,9,10,9,10,10,9,9,10,9,10,10,11,9,11,9,10,10,9,10,10,10,10,9,10])
#m=np.array([0,8.55,10,8.55,10,10,8.55,8.55,10,8.55,10,10,11.5,8.5,11.5,8.5,10,10,8.5,10,10,10,10,8.5,10])
m=np.array([0,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10])

for i in range(len(s)):
    if (i!=0): m[i]=m[i-1]+m[i]

ywerte=m
xwerte=s
exwerte=serr*np.ones(len(xwerte))
eywerte=merr*np.ones(len(ywerte))
name="Uebersetzungsfaktor"

a,ea,b,eb,chiq,corr = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(a,ea,b,eb,chiq,corr))
print('somit ist der Umrechnungsfaktor k={}+-{}'.format(a*1000*lambdaHeNe/2, ea*1000*lambdaHeNe/2))

def anpassung(x):
    return a*(x)+b

figure()
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, anpassung(xwerte), '-')
ylabel('m')
xlabel('s / mm')
legend(title='Lineare Regression \nSteigung[1/mm]: ${:.2f}\\pm{:.2f}$ \ny-Achsenabschnitt: ${:.0f}\\pm{:.0f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(xwerte)))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
errorbar(x=xwerte, y=ywerte-anpassung(xwerte), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte,0.*xwerte, zorder=2) # Linie bei Null 
xlabel('s / mm')
ylabel('$m-m_{fit}$')
legend(title='Residuenplot \n $X^2/n_{{df}}$ = {:.2f}'.format(chiq/(len(xwerte)-2)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()



#Aufteilen in drei Gruppen

aliste=[]

# Gruppe 1

ywerte=m[0:6]
xwerte=s[0:6]
exwerte=serr*np.ones(len(xwerte))
eywerte=merr*np.ones(len(ywerte))
name="Uebersetzungsfaktor1"

a,ea,b,eb,chiq,corr = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(a,ea,b,eb,chiq,corr))
print('somit ist der Umrechnungsfaktor k={}+-{}'.format(a*1000*lambdaHeNe/2, ea*1000*lambdaHeNe/2))

def anpassung(x):
    return a*(x)+b

figure()
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, anpassung(xwerte), '-')
ylabel('m')
xlabel('s / mm')
legend(title='Lineare Regression \nSteigung[1/mm]: ${:.2f}\\pm{:.2f}$ \ny-Achsenabschnitt: ${:.0f}\\pm{:.0f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(xwerte)))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
errorbar(x=xwerte, y=ywerte-anpassung(xwerte), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte,0.*xwerte, zorder=2) # Linie bei Null 
xlabel('s / mm')
ylabel('$m-m_{fit}$')
legend(title='Residuenplot \n $X^2/n_{{df}}$ = {:.2f}'.format(chiq/(len(xwerte)-2)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()


aliste.append(a)


#Gruppe 2

ywerte=m[6:12]
xwerte=s[6:12]
exwerte=serr*np.ones(len(xwerte))
eywerte=merr*np.ones(len(ywerte))
name="Uebersetzungsfaktor2"

a,ea,b,eb,chiq,corr = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(a,ea,b,eb,chiq,corr))
print('somit ist der Umrechnungsfaktor k={}+-{}'.format(a*1000*lambdaHeNe/2, ea*1000*lambdaHeNe/2))

def anpassung(x):
    return a*(x)+b

figure()
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, anpassung(xwerte), '-')
ylabel('m')
xlabel('s / mm')
legend(title='Lineare Regression \nSteigung[1/mm]: ${:.2f}\\pm{:.2f}$ \ny-Achsenabschnitt: ${:.0f}\\pm{:.0f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(xwerte)))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
errorbar(x=xwerte, y=ywerte-anpassung(xwerte), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte,0.*xwerte, zorder=2) # Linie bei Null 
xlabel('s / mm')
ylabel('$m-m_{fit}$')
legend(title='Residuenplot \n $X^2/n_{{df}}$ = {:.2f}'.format(chiq/(len(xwerte)-2)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()

aliste.append(a)



#Gruppe 3

ywerte=m[12:18]
xwerte=s[12:18]
exwerte=serr*np.ones(len(xwerte))
eywerte=merr*np.ones(len(ywerte))
name="Uebersetzungsfaktor3"

a,ea,b,eb,chiq,corr = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(a,ea,b,eb,chiq,corr))
print('somit ist der Umrechnungsfaktor k={}+-{}'.format(a*1000*lambdaHeNe/2, ea*1000*lambdaHeNe/2))

def anpassung(x):
    return a*(x)+b

figure()
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, anpassung(xwerte), '-')
ylabel('m')
xlabel('s / mm')
legend(title='Lineare Regression \nSteigung[1/mm]: ${:.2f}\\pm{:.2f}$ \ny-Achsenabschnitt: ${:.0f}\\pm{:.0f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(xwerte)))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
errorbar(x=xwerte, y=ywerte-anpassung(xwerte), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte,0.*xwerte, zorder=2) # Linie bei Null 
xlabel('s / mm')
ylabel('$m-m_{fit}$')
legend(title='Residuenplot \n $X^2/n_{{df}}$ = {:.2f}'.format(chiq/(len(xwerte)-2)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()

aliste.append(a)



#Gruppe 4

ywerte=m[18:25]
xwerte=s[18:25]
exwerte=serr*np.ones(len(xwerte))
eywerte=merr*np.ones(len(ywerte))
name="Uebersetzungsfaktor4"

a,ea,b,eb,chiq,corr = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(a,ea,b,eb,chiq,corr))
print('somit ist der Umrechnungsfaktor k={}+-{}'.format(a*1000*lambdaHeNe/2, ea*1000*lambdaHeNe/2))

def anpassung(x):
    return a*(x)+b

figure()
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, anpassung(xwerte), '-')
ylabel('m')
xlabel('s / mm')
legend(title='Lineare Regression \nSteigung[1/mm]: ${:.2f}\\pm{:.2f}$ \ny-Achsenabschnitt: ${:.0f}\\pm{:.0f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(xwerte)))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
errorbar(x=xwerte, y=ywerte-anpassung(xwerte), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte,0.*xwerte, zorder=2) # Linie bei Null 
xlabel('s / mm')
ylabel('$m-m_{fit}$')
legend(title='Residuenplot \n $X^2/n_{{df}}$ = {:.2f}'.format(chiq/(len(xwerte)-2)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()

aliste.append(a)




print(aliste)
print(np.mean(aliste), np.std(aliste, ddof=1)/np.sqrt(len(aliste)))
k=[np.mean(aliste)*1000*lambdaHeNe/2, np.std(aliste, ddof=1)/np.sqrt(len(aliste))*1000*lambdaHeNe/2, np.mean(aliste)*1000*lambdaerr/2]
print('gemittelter Umrechnungsfaktor k={} +- {}(stat) +- {:f}(sys)'.format(k[0],k[1],k[2]))


np.savetxt('kalibrierung.txt', k)

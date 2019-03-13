# -*- coding: utf-8 -*-

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *


Teilung=[8,16,23,31]
#Teilung=[11,21,31]
#Teilung=[16,31]

serr=0.01/np.sqrt(12)  # in mm
merr=0.1  # Maximum lässt sich nicht genau einstellen

lambdaHeNe=632.8*10**-9
lambdaerr=0.1*10**-9


file= open("../Rohdaten/kalib.dat")
data=[]
l=0
for line in file:
    d=np.array(line.split(" "))
    data.append(d.astype(np.float))

s=np.array(data[4]) #  in mm


#                                            9
m=np.array([0,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10])

for i in range(len(s)):
    if (i!=0): m[i]=m[i-1]+m[i]

xwerte=m
ywerte=s
exwerte=merr*np.ones(len(xwerte))
eywerte=serr*np.ones(len(ywerte))
name="Uebersetzungsfaktor1"

a,ea,b,eb,chiq,corr = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(a,ea,b,eb,chiq,corr))
print('somit ist der Umrechnungsfaktor k={}+-{}'.format(1000*lambdaHeNe/(2*a), 1000*ea*lambdaHeNe/(2*a**2)))

def anpassung(x):
    return a*(x)+b

figure()
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, anpassung(xwerte), '-')
xlabel('m')
ylabel('s / mm')
legend(title='Lineare Regression \nSteigung[mm]: ${:.4f}\\pm{:.4f}$ \ny-Achsenabschnitt: ${:.1f}\\pm{:.1f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(xwerte)))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
errorbar(x=xwerte, y=ywerte-anpassung(xwerte), yerr=np.sqrt((eywerte)**2+(exwerte*ea)**2), linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte,0.*xwerte, zorder=2) # Linie bei Null 
xlabel('m')
ylabel('$s-s_{fit} [mm]$')
legend(title='Residuenplot \n $X^2/n_{{df}}$ = {:.2f}'.format(chiq/(len(xwerte)-2)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()




#Aufteilen in vier  Gruppen
aliste=[]
erraliste=[]

aliste.append(a)
erraliste.append(ea)



for j in range(len(Teilung)):

    
    if j==0:
        xwerte=m[0:Teilung[j]]
        ywerte=s[0:Teilung[j]]
    else:
        xwerte=m[Teilung[j-1]:Teilung[j]]
        ywerte=s[Teilung[j-1]:Teilung[j]]
    exwerte=merr*np.ones(len(xwerte))
    eywerte=serr*np.ones(len(ywerte))
    name="Uebersetzungsfaktor1{}".format(j+1)

    a,ea,b,eb,chiq,corr = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
    print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(a,ea,b,eb,chiq,corr))
    print('somit ist der Umrechnungsfaktor k={}+-{}'.format(1000*lambdaHeNe/(2*a), 1000*ea*lambdaHeNe/(2*a**2)))
    
    def anpassung(x):
        return a*(x)+b
    
    figure()
    errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
    plot(xwerte, anpassung(xwerte), '-')
    xlabel('m')
    ylabel('s / mm')
    legend(title='Lineare Regression \nSteigung[mm]: ${:.4f}\\pm{:.4f}$ \ny-Achsenabschnitt: ${:.1f}\\pm{:.1f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(xwerte)))
    savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
    show()
    
    
    figure()
    errorbar(x=xwerte, y=ywerte-anpassung(xwerte), yerr=np.sqrt((eywerte)**2+(exwerte*ea)**2), linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
    plot(xwerte,0.*xwerte, zorder=2) # Linie bei Null 
    xlabel('m')
    ylabel('$s-s_{fit} [mm]$')
    legend(title='Residuenplot \n $X^2/n_{{df}}$ = {:.2f}'.format(chiq/(len(xwerte)-2)))
    savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')
    
    show()
    
    aliste.append(a)
    erraliste.append(ea)






print(aliste)

aliste=np.array(aliste)
erraliste=np.array(erraliste)

kalib1=1000*lambdaHeNe/2/aliste
ekalib1=1000*erraliste*lambdaHeNe/2/aliste**2

print(' Umrechnungsfaktor k Übersicht')
print(kalib1)
print(ekalib1)

np.savetxt('kalibrierung1.txt', [kalib1, ekalib1])

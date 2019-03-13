# -*- coding: utf-8 -*-

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *


Teilung=[8,16,23,31]
#Teilung=[11,21,31]
#Teilung=[16,31]

#---Kalibrierungsfaktor bestimmen

kalibfile1=np.genfromtxt('kalibrierung1.txt')
kalibfile1=kalibfile1[0,:]
kalibfile2=np.genfromtxt('kalibrierung2.txt')
kalibfile2=kalibfile2[0,:]

Kalib=[]
Errkalib=[]
for i in range(len(kalibfile1)):
    Kalib.append(np.mean([kalibfile1[i], kalibfile2[i]]))
    Errkalib.append(np.std([kalibfile1[i], kalibfile2[i]], ddof=1))    
Errkalib=np.mean(Errkalib)*np.ones(len(Errkalib))

print(Kalib, Errkalib)



#--------------------------------------------------


serr=0.01/np.sqrt(12)  # in mm
merr=0.1  # Maximum lässt sich nicht genau einstellen

kalib=0.048
errkalib=0.001


file= open("../Rohdaten/grun.dat")
data=[]
for line in file:
    d=np.array(line.split(" "))
    data.append(d.astype(np.float))

s=np.array(data[1]) #  in mm


#                                            
m=np.array([0,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10])

for i in range(len(s)):
    if (i!=0): m[i]=m[i-1]+m[i]

xwerte=m
ywerte=s
exwerte=merr*np.ones(len(xwerte))
eywerte=serr*np.ones(len(ywerte))
name="testlambda"

a,ea,b,eb,chiq,corr = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(a,ea,b,eb,chiq,corr))
print('somit ist die Wellenlaenge lambda={}+-{}'.format(a/1000*2*kalib, ea/1000*2*errkalib))

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
errkalib=Errkalib[0]

# Gruppe 1



for j in range(len(Teilung)):


    
    kalib=Kalib[j]
    
    if j==0:
        xwerte=m[0:Teilung[j]]
        ywerte=s[0:Teilung[j]]
    else:
        xwerte=m[Teilung[j-1]:Teilung[j]]
        ywerte=s[Teilung[j-1]:Teilung[j]]
    exwerte=merr*np.ones(len(xwerte))
    eywerte=serr*np.ones(len(ywerte))
    name="TestLambda{}".format(j)
    
    a,ea,b,eb,chiq,corr = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
    print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(a,ea,b,eb,chiq,corr))
    print('somit ist die Wellenlaenge lambda={}+-{}+-{}sys'.format(a/1000*2*kalib, ea/1000*2*kalib, a/1000*2*Errkalib[j]))
    
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





aliste=np.array(aliste)
erraliste=np.array(erraliste)

Lambda=aliste/1000*2*Kalib
elinreglambda=erraliste/1000*2*Kalib
elambda=aliste/1000*2*Errkalib[j]


for i in range(len(Lambda)):
    print("Teilung {}: Lambda={:.1f}nm +-{:.1f}sys nm+-{:.1f}linreg nm    für K={:.4f}+-{:.4f}".format(i,Lambda[i]*10e8,elambda[i]*10e8, elinreglambda[i]*10e8, Kalib[i], Errkalib[i]))

np.savetxt('testlambda.txt', [Lambda, elinreglambda, elambda])

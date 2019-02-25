
from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *

Rohdaten=np.genfromtxt("Rohdatenl.txt")



serr=0.01/np.sqrt(12)  #in mm
merr=1./np.sqrt(12)

k=np.genfromtxt('kalibrierung.txt')[0]
kerr=np.genfromtxt('kalibrierung.txt')[1]


s=Rohdaten   #in mm
m=np.array([0,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10])
for i in range(len(s)):
    if (i!=0): m[i]=m[i-1]+m[i]



ywerte=s
xwerte=m
exwerte=merr*np.ones(len(xwerte))
eywerte=serr*np.ones(len(ywerte))
name="Wellenlaenge"

a,ea,b,eb,chiq,corr = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(a,ea,b,eb,chiq,corr))
print('somit ist die Wellenlaenge lambda={}nm+-{}nm(stat)+-{}nm(sys)'.format(a*2*k*10**6, ea*2*k*10**6, a*2*kerr*10**6))

def anpassung(x):
    return a*(x)+b

figure()
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, anpassung(xwerte), '-')
ylabel('s / mm')
xlabel('m')
legend(title='Lineare Regression \nSteigung[mm]: ${:.5f}\\pm{:.5f}$ \ny-Achsenabschnitt[mm]: ${:.2f}\\pm{:.2f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(xwerte)))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
#title('Residuenplot des Übersetzungsfaktors')
errorbar(x=xwerte, y=ywerte-anpassung(xwerte), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte,0.*xwerte, zorder=2) # Linie bei Null 
xlabel('m')
ylabel('$s-s_{fit}$ / mm')
legend(title='Residuenplot \n $X^2/n$ = {:.2f}'.format(chiq/(len(xwerte)-2)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()




#Aufteilung in Gruppen


aliste=[]


#Gruppe 1

ywerte=s[0:9]
xwerte=m[0:9]
exwerte=merr*np.ones(len(xwerte))
eywerte=serr*np.ones(len(ywerte))
name="Wellenlaenge1"

a,ea,b,eb,chiq,corr = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(a,ea,b,eb,chiq,corr))
print('somit ist die Wellenlaenge lambda={}nm+-{}nm(stat)+-{}nm(sys)'.format(a*2*k*10**6, ea*2*k*10**6, a*2*kerr*10**6))

def anpassung(x):
    return a*(x)+b

figure()
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, anpassung(xwerte), '-')
ylabel('s / mm')
xlabel('m')
legend(title='Lineare Regression \nSteigung[mm]: ${:.5f}\\pm{:.5f}$ \ny-Achsenabschnitt[mm]: ${:.2f}\\pm{:.2f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(xwerte)))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
#title('Residuenplot des Übersetzungsfaktors')
errorbar(x=xwerte, y=ywerte-anpassung(xwerte), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte,0.*xwerte, zorder=2) # Linie bei Null 
xlabel('m')
ylabel('$s-s_{fit}$ / mm')
legend(title='Residuenplot \n $X^2/n$ = {:.2f}'.format(chiq/(len(xwerte)-2)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()

aliste.append(a)




#Gruppe 2

ywerte=s[9:18]
xwerte=m[9:18]
exwerte=merr*np.ones(len(xwerte))
eywerte=serr*np.ones(len(ywerte))
name="Wellenlaenge2"

a,ea,b,eb,chiq,corr = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(a,ea,b,eb,chiq,corr))
print('somit ist die Wellenlaenge lambda={}nm+-{}nm(stat)+-{}nm(sys)'.format(a*2*k*10**6, ea*2*k*10**6, a*2*kerr*10**6))

def anpassung(x):
    return a*(x)+b

figure()
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, anpassung(xwerte), '-')
ylabel('s / mm')
xlabel('m')
legend(title='Lineare Regression \nSteigung[mm]: ${:.5f}\\pm{:.5f}$ \ny-Achsenabschnitt[mm]: ${:.2f}\\pm{:.2f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(xwerte)))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
#title('Residuenplot des Übersetzungsfaktors')
errorbar(x=xwerte, y=ywerte-anpassung(xwerte), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte,0.*xwerte, zorder=2) # Linie bei Null 
xlabel('m')
ylabel('$s-s_{fit}$ / mm')
legend(title='Residuenplot \n $X^2/n$ = {:.2f}'.format(chiq/(len(xwerte)-2)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()

aliste.append(a)


#Gruppe 3

ywerte=s[18:28]
xwerte=m[18:28]
exwerte=merr*np.ones(len(xwerte))
eywerte=serr*np.ones(len(ywerte))
name="Wellenlaenge3"

a,ea,b,eb,chiq,corr = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(a,ea,b,eb,chiq,corr))
print('somit ist die Wellenlaenge lambda={}nm+-{}nm(stat)+-{}nm(sys)'.format(a*2*k*10**6, ea*2*k*10**6, a*2*kerr*10**6))

def anpassung(x):
    return a*(x)+b

figure()
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, anpassung(xwerte), '-')
ylabel('s / mm')
xlabel('m')
legend(title='Lineare Regression \nSteigung[mm]: ${:.5f}\\pm{:.5f}$ \ny-Achsenabschnitt[mm]: ${:.2f}\\pm{:.2f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(xwerte)))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
#title('Residuenplot des Übersetzungsfaktors')
errorbar(x=xwerte, y=ywerte-anpassung(xwerte), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte,0.*xwerte, zorder=2) # Linie bei Null 
xlabel('m')
ylabel('$s-s_{fit}$ / mm')
legend(title='Residuenplot \n $X^2/n$ = {:.2f}'.format(chiq/(len(xwerte)-2)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()

aliste.append(a)


'''
#Gruppe 4

ywerte=s[21:28]
xwerte=m[21:28]
exwerte=merr*np.ones(len(xwerte))
eywerte=serr*np.ones(len(ywerte))
name="Wellenlaenge4"

a,ea,b,eb,chiq,corr = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(a,ea,b,eb,chiq,corr))
print('somit ist die Wellenlaenge lambda={}nm+-{}nm(stat)+-{}nm(sys)'.format(a*2*k*10**6, ea*2*k*10**6, a*2*kerr*10**6))

def anpassung(x):
    return a*(x)+b

figure()
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, anpassung(xwerte), '-')
ylabel('s / mm')
xlabel('m')
legend(title='Lineare Regression \nSteigung[mm]: ${:.5f}\\pm{:.5f}$ \ny-Achsenabschnitt[mm]: ${:.2f}\\pm{:.2f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(xwerte)))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
#title('Residuenplot des Übersetzungsfaktors')
errorbar(x=xwerte, y=ywerte-anpassung(xwerte), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte,0.*xwerte, zorder=2) # Linie bei Null 
xlabel('m')
ylabel('$s-s_{fit}$ / mm')
legend(title='Residuenplot \n $X^2/n$ = {:.2f}'.format(chiq/(len(xwerte)-2)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()

aliste.append(a)

del aliste[0]

'''

print(aliste)
print(np.mean(aliste), np.std(aliste, ddof=1))
lambdag=np.array([np.mean(aliste)*2*k*10**6, np.std(aliste, ddof=1)/np.sqrt(len(aliste))*2*k*10**6, np.mean(aliste)*2*kerr*10**6])
print('gemittelte Wellenlaenge lambda={} +- {}(stat) +- {:f}(sys)'.format(lambdag[0],lambdag[1],lambdag[2]))


np.savetxt('wellenlaenge.txt', lambdag*10**(-9))

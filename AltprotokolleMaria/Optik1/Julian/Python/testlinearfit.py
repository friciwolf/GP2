#! /usr/bin/env python


from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *
import scipy.optimize

#Berechnung Standardabweichung durch Leseungenauigkeit



phistd=np.std((322.5+np.array([14,14,14,14,13,13,12,12,13,14])/60), ddof=1)
print(phistd)


#Erzeugung Rohdaten
CdHg=np.zeros((8,5))
Bogenminuteliste1=[14,14,14,14,13,13,12,12,13,14]
Bogenminuteliste2=[13,15,15]
CdHg[0,:]=np.array([643.85, 322.5+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 204.5+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])
Bogenminuteliste1=[3,3,3]
Bogenminuteliste2=[23,21,23]
CdHg[1,:]=np.array([579.07, 323.5+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 203.5+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])
Bogenminuteliste1=[6,8,5]
Bogenminuteliste2=[20,19,20]
CdHg[2,:]=np.array([546.07, 324+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 203+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])
Bogenminuteliste1=[23,25,25]
Bogenminuteliste2=[0,0,1]
CdHg[3,:]=np.array([508.58, 324.5+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 202.5+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])
Bogenminuteliste1=[14,14,13]
Bogenminuteliste2=[13,13,12]
CdHg[4,:]=np.array([479.99, 325.5+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 201.5+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])
Bogenminuteliste1=[6,6,7]
Bogenminuteliste2=[18,18,17]
CdHg[5,:]=np.array([467.81, 326+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 201+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])
Bogenminuteliste1=[25,23,22]
Bogenminuteliste2=[1,0,2]
CdHg[6,:]=np.array([435.83, 327+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 200+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])
Bogenminuteliste1=[7,7,7]
Bogenminuteliste2=[19,18,20]
CdHg[7,:]=np.array([404.66, 329+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 198+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])



append01=np.reshape(np.array([0.5*CdHg[:,1]-0.5*CdHg[:,3]]), (8,1))
append02=np.reshape(np.array([np.sqrt(0.5*CdHg[:,2]**2+0.5*CdHg[:,4]**2)*np.pi/180]), (8,1))
CdHg = np.append(CdHg, append01, axis=1)
CdHg = np.append(CdHg, append02, axis=1)
append03=np.reshape(np.array([np.sin((30+0.5*CdHg[:,5])*np.pi/180)/np.sin(30*np.pi/180)]), (8,1))
append04=np.reshape(np.array([CdHg[:,6]*np.absolute(np.cos((30+0.5*CdHg[:,5])*np.pi/180))/(2*np.sin(30*np.pi/180))]), (8,1))
CdHg = np.append(CdHg, append03, axis=1)
CdHg = np.append(CdHg, append04, axis=1)
print(CdHg)

#CdHg:  0-Wellenlaenge*[nm]  1-phi1[grad]  2-ephi1[Grad]  3-phi2[grad]  4-ephi2[grad]  5-delmin[grad]  6-edelmin[radiant]  7-n[]  8-en[]


def nfunction(xdata,*par):
    return par[0] + par[1]*xdata 


p0=(1,1)
popt, pcov = scipy.optimize.curve_fit(f=nfunction, xdata=(CdHg[:,0]*10**-9)**(-2), ydata=CdHg[:,7], p0=p0, sigma=CdHg[:,8])

perr=np.sqrt(np.diag(pcov))    
print(popt,perr)

lambdam2=(CdHg[:,0]*10**(-9))**(-2)
n_CdHg=CdHg[:,7]


chiq=sum(((nfunction(lambdam2,*popt)-n_CdHg)/(CdHg[:,8]))**2)
print(chiq)
print(chiq/(len(lambdam2)-3))

xwerte=lambdam2
ywerte=n_CdHg
eywerte=CdHg[:,8]
exwerte=None
name='CdHg'





figure()
#title('Lineare Regression der Abstandskalibrierung')
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, nfunction(xwerte, *popt), '-', zorder=2)
xlabel('$1/\\lambda^2$ in $m^{-2}$')
ylabel('n')
legend(title='Fit \n$f(x)=a+bx+cx^2$,  $x=1/\\lambda^2$ \n$a=${:.2e} $\pm$ {:.2e} \n$b=${:.2e} $m^2$ $\pm$ {:.2e} $m^2$'.format(popt[0],perr[0],popt[1],perr[1]))
savefig('test_{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
#title('Residuenplot der Abstandskalibrierung')
errorbar(x=xwerte, y=ywerte-nfunction(xwerte, *popt), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, 0.*xwerte, zorder=2) # Linie bei Null 
xlabel('$1/\\lambda^2$ in $m^{-2}$')
ylabel('$n-f(x)$')
legend(title='Residuenplot \n $X^2/n_{{df}}$ = {:.2f}'.format(chiq/(len(xwerte)-2)))
savefig('test_{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()


'''
figure()
#title('Lineare Regression der Abstandskalibrierung')
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, nfunction(xwerte, *popt), '-', zorder=2)
xlabel('x')
ylabel('y')
legend(title='Lineare Regression \nSteigung: ${:.2f}\\pm{:.3f}$ \ny-Achsenabschnitt: ${:.2f}\\pm{:.3f}$ \nDatenpunkte: {}'.format(a, ea, b, eb, len(R-R_mean)))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
#title('Residuenplot der Abstandskalibrierung')
errorbar(x=xwerte, y=ywerte-nfunction(xwerte, *popt), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, 0.*xwerte, zorder=2) # Linie bei Null 
xlabel('R / $\\Omega$')
ylabel('$(S-S_{fit})$ / cm')
legend(title='Residuenplot \n $X^2/n$ = {:.2f}'.format(chiq/(len(R-R_mean)-2)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()

'''




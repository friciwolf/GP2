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

CdHg[0,2]=1/60/np.sqrt(12)

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
for i in range(8):
    print('${:.2f}$&${:.3f}$&${:.3f}$&${:.4f}$&${:.1f}$&${:.5f}$&${:.1f}$\\\\'.format(CdHg[i,0], CdHg[i,1], CdHg[i,3], CdHg[i,5], CdHg[i,6]*10000, CdHg[i,7], CdHg[i,8]*100000))


def nfunction(xdata,*par):
    return par[0] + par[1]*xdata + par[2]*xdata**2

p0=(1,1,1)
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
legend(title='Fit \n$f(x)=a+bx+cx^2$,  $x=1/\\lambda^2$ \n$a=${:.3e} $\pm$ {:.2e} \n$b=${:.2e} $m^2$ $\pm$ {:.1e} $m^2$\n$c=${:.2e} $m^4$ $\pm$ {:.1e} $m^4$'.format(popt[0],perr[0],popt[1],perr[1],popt[2],perr[2]))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
#title('Residuenplot der Abstandskalibrierung')
errorbar(x=xwerte, y=ywerte-nfunction(xwerte, *popt), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, 0.*xwerte, zorder=2) # Linie bei Null 
xlabel('$1/\\lambda^2$ in $m^{-2}$')
ylabel('$n-f(x)$')
legend(title='Residuenplot \n $X^2/n_{{df}}$ = {:.2f}'.format(chiq/(len(xwerte)-3)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

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


#Bestimmen des Aufloesungsvermoegens--------------------------------------

A_theo = 273.44

def A_exp(b,c, s_sp, delmin, lambda_theo):              #lambda_theo in m!
    dndlambda = (-2.*b/(lambda_theo**3.) - 4.*c/(lambda_theo**5.))
    return -dndlambda*2.*s_sp*np.sin(30./180.*np.pi)/np.cos((delmin/2.+30.)*np.pi/180.)

def print_A(b,c,s_sp, delmin, lambda_theo):
    print('b={:.2e}  c={:.2e}   s_sp={:.2e}  delmin={:.4e} lambda_theo={:.4e} gives A_exp={:.4e}'.format(b,c,s_sp, delmin, lambda_theo, A_exp(b,c, s_sp, delmin, lambda_theo)))
    return A_exp(b,c,s_sp, delmin, lambda_theo)

delmin_lambdaungefaehr=CdHg[1,5]

lambdagenau=576.96

print_A(popt[1], popt[2], 0.001, delmin_lambdaungefaehr, lambdagenau*10**(-9))
print_A(popt[1], popt[2], 0.0015, delmin_lambdaungefaehr, lambdagenau*10**(-9))

delmin_lambdaungefaehr_berechnet=2*np.arcsin(nfunction(1/(CdHg[1,0]*10*(-9))**2, *popt)*np.sin(30/180*np.pi))*180/np.pi - 60
print_A(popt[1], popt[2], 0.001, delmin_lambdaungefaehr_berechnet, lambdagenau*10**(-9))
print_A(popt[1], popt[2], 0.0015, delmin_lambdaungefaehr_berechnet, lambdagenau*10**(-9))


delmin_lambdagenau=2*np.arcsin(nfunction(1/(lambdagenau*10*(-9))**2, *popt)*np.sin(30/180*np.pi))*180/np.pi - 60

print(delmin_lambdagenau)
print_A(popt[1], popt[2], 0.001, delmin_lambdagenau, lambdagenau*10**(-9))
print_A(popt[1], popt[2], 0.0015, delmin_lambdagenau, lambdagenau*10**(-9))




#--------------------------------------------------------------------------



Zn=np.zeros((4,5))
Bogenminuteliste1=[22,22,20]
Bogenminuteliste2=[11,11,12]
Zn[0,:]=np.array([636.23, 322.5+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 204.5+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])
Bogenminuteliste1=[12,14,14]
Bogenminuteliste2=[16,17,17]
Zn[1,:]=np.array([481.05, 325.5+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 201.5+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])
Bogenminuteliste1=[2,1,1]
Bogenminuteliste2=[0,0,0]
Zn[2,:]=np.array([472.22, 326+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 201.5+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])
Bogenminuteliste1=[10,9,9]
Bogenminuteliste2=[21,21,20]
Zn[3,:]=np.array([468.01, 326+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 201+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])



append01=np.reshape(np.array([0.5*Zn[:,1]-0.5*Zn[:,3]]), (4,1))
append02=np.reshape(np.array([np.sqrt(0.5*Zn[:,2]**2+0.5*Zn[:,4]**2)*np.pi/180]), (4,1))
Zn = np.append(Zn, append01, axis=1)
Zn = np.append(Zn, append02, axis=1)
append03=np.reshape(np.array([np.sin((30+0.5*Zn[:,5])*np.pi/180)/np.sin(30*np.pi/180)]), (4,1))
append04=np.reshape(np.array([Zn[:,6]*np.absolute(np.cos((30+0.5*Zn[:,5])*np.pi/180))/(2*np.sin(30*np.pi/180))]), (4,1))
Zn = np.append(Zn, append03, axis=1)
Zn = np.append(Zn, append04, axis=1)
print(Zn)


p0=(1,1,1)
popt2, pcov2 = scipy.optimize.curve_fit(f=nfunction, xdata=(Zn[:,0]*10**-9)**(-2), ydata=Zn[:,7], p0=p0, sigma=Zn[:,8])

perr2=np.sqrt(np.diag(pcov2))    
print(popt2,perr2)

lambdam2_2=(Zn[:,0]*10**(-9))**(-2)
n_Zn=Zn[:,7]


chiq2=sum(((nfunction(lambdam2_2,*popt2)-n_Zn)/(Zn[:,8]))**2)
print(chiq2)
print(chiq2/(len(lambdam2_2)-3))


xwerte=lambdam2_2
ywerte=n_Zn
eywerte=Zn[:,8]
exwerte=None
name='Zn'





figure()
#title('Lineare Regression der Abstandskalibrierung')
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, nfunction(xwerte, *popt2), '-', zorder=2)
plot(xwerte, nfunction(xwerte, *popt), '-', zorder=2)

xlabel('$1/\\lambda^2$ in $m^{-2}$')
ylabel('n')
legend(title='Fit \n$f(x)=a+bx+cx^2$,  $x=1/\\lambda^2$ \n$a=${:.3e} $\pm$ {:.2e} \n$b=${:.3e} $m^2$ $\pm$ {:.2e} $m^2$\n$c=${:.3e} $m^4$ $\pm$ {:.2e} $m^4$'.format(popt2[0],perr2[0],popt2[1],perr2[1],popt2[2],perr2[2]))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
#title('Residuenplot der Abstandskalibrierung')
errorbar(x=xwerte, y=ywerte-nfunction(xwerte, *popt2), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, 0.*xwerte, zorder=2) # Linie bei Null 
xlabel('$1/\\lambda^2$ in $m^{-2}$')
ylabel('$n-f(x)$')
legend(title='Residuenplot \n $X^2/n_{{df}}$ = {:.2f}'.format(chiq2/(len(xwerte)-3)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()



#--------------------------------------------------------

#Zn:  0-Wellenlaenge*[nm]  1-phi1[grad]  2-ephi1[Grad]  3-phi2[grad]  4-ephi2[grad]  5-delmin[grad]  6-edelmin[radiant]  7-n[]  8-en[]  9-lambda_berechnet[m] 10-lamdba+delta[m]  11-lambda-delta[m]

print(popt)
def lambda_function(n_exp):
    return (2*(popt[2])/(-popt[1]+np.sqrt((popt[1])**2-4*popt[2]*(popt[0]-n_exp))))**(1/2)


print(lambda_function(1.75))

append05=np.reshape(np.array([lambda_function(Zn[:,7])]), (4,1))
append06=np.reshape(np.array([lambda_function(Zn[:,7]-Zn[:,8])]), (4,1))
append07=np.reshape(np.array([lambda_function(Zn[:,7]+Zn[:,8])]), (4,1))
Zn = np.append(Zn, append05, axis=1)
Zn = np.append(Zn, append06, axis=1)
Zn = np.append(Zn, append07, axis=1)

for i in range(4):
    print('${:.2f}$&${:.3f}$&${:.3f}$&${:.4f}$&${:.1f}$&${:.5f}$&${:.1f}$\\\\'.format(Zn[i,0], Zn[i,1], Zn[i,3], Zn[i,5], Zn[i,6]*10000, Zn[i,7], Zn[i,8]*100000))

print(Zn)
for i in range(4):
    
    n_ber=Zn[i,7]
    n_berm=Zn[i,7]-Zn[i,8]
    n_berp=Zn[i,7]+Zn[i,8]
    l_theo=Zn[i,0]*10**(-9)
    l_ber=Zn[i,9]
    l_berm=Zn[i,11]
    l_berp=Zn[i,10]
    x_ber=1/(l_ber)**2
    x_berm=1/(l_berp)**2
    x_berp=1/(l_berm)**2
    x_theo=1/(l_theo)**2
    
    
    xmin=x_berm-0.02e12
    xmax=x_berp+0.02e12
    n_min=nfunction(xmin, *popt)
    n_max=nfunction(xmax, *popt)
    
    plot(np.linspace(xmin,xmax, 50), nfunction(np.linspace(xmin, xmax, 50), *popt), color='orange', label='$f\ (1/\\lambda^2)$')
    plot((xmin, x_ber),(n_ber, n_ber), color='blue')
    plot((xmin, x_berm),(n_berm, n_berm), color='blue', linestyle='dashed')
    plot((xmin, x_berp),(n_berp, n_berp), color='blue', linestyle='dashed')
    plot((x_berm, x_berm),(n_min, n_berm), color='blue', linestyle='dashed')
    plot((x_berp, x_berp),(n_min, n_berp), color='blue', linestyle='dashed')
    plot((x_ber, x_ber),(n_min, n_ber), color='blue')
    axvline(x_theo, color='red')
    text(x_theo+0.003e12, n_max-0.00005, s='$\\lambda_{{erwartet}}$={:.4}m'.format(l_theo), color='red')
    text(x_berp+0.001e12, n_berm, s='$\\lambda_{{+\\Delta}}$={:.4}m \n$\\lambda_{{exp}}$={:.4}m \n$\\lambda_{{+\\Delta}}$={:.4}m'.format(l_berm, l_ber, l_berp), color='blue')
    xlabel('$1/\\lambda^2$ in $m^{-2}$')
    ylabel('n')
    legend()
    savefig('Zn_{}.pdf'.format(i), bbox_inches = 'tight')
    
    show()
    close()



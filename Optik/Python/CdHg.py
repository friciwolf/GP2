#! /usr/bin/env python


from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *
import scipy.optimize

#Berechnung Standardabweichung durch Leseungenauigkeit


phimean=np.mean((26.5+np.array([27,26,25,35,23,21,19,22,25,21])/60))
phistd=np.std((26.5+np.array([27,26,25,35,23,21,19,22,25,21])/60), ddof=1)
print(phistd)
print(np.linspace(18.5, 35.5, 18))

#Histogramm
histogrammdaten=np.array([27,26,25,35,23,21,19,22,25,21])
figure()
hist(histogrammdaten,linspace(18.5, 35.5, 18))
xticks(np.linspace(19, 35, 17))
yticks([0,1,2])
errorbar((np.mean(histogrammdaten)), (0.5), xerr=(np.std(histogrammdaten, ddof=1)), capsize=5, elinewidth=5)
axvline(np.mean(histogrammdaten), linewidth=4, color='darkorange')
text(np.mean(histogrammdaten)+3, 1.5, '$\\sigma_{{\\psi}}$={:.4f}°\n$\\bar{{\\psi}}$={:.4f}°'.format(phistd, phimean, color='black', fontsize=12))
xlabel('$\\psi=(26.5+x/60$)°,   x = ')
ylabel('Häufigkeit')
savefig('Histogramm_Psi.pdf', bbox_inches = 'tight')
show()


#Erzeugung Rohdaten
M=5
CdHg=np.zeros((M,5))
Bogenminuteliste1=[27,26,25,35,23,21,19,22,25,21]
Bogenminuteliste2=[21,20,20]
CdHg[0,:]=np.array([643.85, 26.5+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 144.5+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])
Bogenminuteliste1=[5,5,3]
Bogenminuteliste2=[15,15,16]
CdHg[1,:]=np.array([546.07, 25.5+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 146+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])
Bogenminuteliste1=[12,13,14]
Bogenminuteliste2=[5,4,5]
CdHg[2,:]=np.array([508.58, 24.5+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 147+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])
#Bogenminuteliste1=[16,15,15]
#Bogenminuteliste2=[23,21,22]
#CdHg[3,:]=np.array([479.99, 24.5+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 147.5+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])
Bogenminuteliste1=[16,17,13]
Bogenminuteliste2=[3,2,1]
CdHg[M-2,:]=np.array([435.83, 22.+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 149.5+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])
Bogenminuteliste1=[5,6,6]
Bogenminuteliste2=[13,14,14]
CdHg[M-1,:]=np.array([404.66, 20.5+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 151+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])


append01=np.reshape(np.array([0.5*CdHg[:,3]-0.5*CdHg[:,1]]), (M,1))
append02=np.reshape(np.array([np.sqrt((0.5*CdHg[:,2])**2+(0.5*CdHg[:,4])**2)*np.pi/180]), (M,1))
CdHg = np.append(CdHg, append01, axis=1)
CdHg = np.append(CdHg, append02, axis=1)
append03=np.reshape(np.array([np.sin((30+0.5*CdHg[:,5])*np.pi/180)/np.sin(30*np.pi/180)]), (M,1))
append04=np.reshape(np.array([CdHg[:,6]*np.absolute(np.cos((30+0.5*CdHg[:,5])*np.pi/180))/(2*np.sin(30*np.pi/180))]), (M,1))
CdHg = np.append(CdHg, append03, axis=1)
CdHg = np.append(CdHg, append04, axis=1)
print(CdHg)

#CdHg:  0-Wellenlaenge*[nm]  1-phi1[grad]  2-ephi1[Grad]  3-phi2[grad]  4-ephi2[grad]  5-delmin[grad]  6-edelmin[radiant]  7-n[]  8-en[]
for i in range(M):
    print('${:.2f}$&${:.3f}$&${:.3f}$&${:.4f}$&${:.4f}$&${:.5f}$&${:.5f}$\\\\'.format(CdHg[i,0], CdHg[i,1], CdHg[i,3], CdHg[i,5], CdHg[i,6], CdHg[i,7], CdHg[i,8]))


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





figure(figsize=((8,5)))
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, nfunction(xwerte, *popt), '-', zorder=2)
xlabel('$1/\\lambda^2$ in $m^{-2}$')
ylabel('n')
ticklabel_format(useMathText=True)
legend(title='Fit \n$f(x)=a+bx+cx^2$,  $x=1/\\lambda^2$ \n$a=${:.5e} $\pm$ {:.2e} \n$b=${:.2e} $m^2$ $\pm$ {:.1e} $m^2$\n$c=${:.2e} $m^4$ $\pm$ {:.1e} $m^4$'.format(popt[0],perr[0],popt[1],perr[1],popt[2],perr[2]))
#savefig('{}_Fit_Messfehler.pdf'.format(name), bbox_inches = 'tight')
savefig('{}_Fit.pdf'.format(name), bbox_inches = 'tight')
show()


figure(figsize=((8,3)))
errorbar(x=xwerte, y=ywerte-nfunction(xwerte, *popt), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, 0.*xwerte, zorder=2) # Linie bei Null 
xlabel('$1/\\lambda^2$ in $m^{-2}$')
ylabel('$n-f(x)$')
ticklabel_format(useMathText=True)
legend(title='Residuenplot \n $X^2/n_{{df}}$ = {:.2f}'.format(chiq/(len(xwerte)-3)))
#savefig('{}_Residuen_Messfehler.pdf'.format(name), bbox_inches = 'tight')
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')
show()





#Bestimmen des Aufloesungsvermoegens--------------------------------------

A_theo = 273.44

def A_exp(b,c, s_sp, delmin, lambda_theo):              #lambda_theo in meter, s_sp spaltabstand in m, delminin in Grad!
    dndlambda = (-2.*b/(lambda_theo**3.) - 4.*c/(lambda_theo**5.))
    return -dndlambda*2.*s_sp*np.sin(30./180.*np.pi)/np.cos((delmin/2.+30.)*np.pi/180.)

def print_A(b,c,s_sp, delmin, lambda_theo):
    print('b={:.2e}  c={:.2e}   s_sp={:.2e}  delmin={:.4e} lambda_theo={:.4e} gives A_exp={:.4e}'.format(b,c,s_sp, delmin, lambda_theo, A_exp(b,c, s_sp, delmin, lambda_theo)))
    return A_exp(b,c,s_sp, delmin, lambda_theo)

lambdagelb=576.96

ngelb=nfunction(1/(lambdagelb*10**(-9))**(2), *popt)
delmin_lambdagelb=180./np.pi*2*np.arcsin(ngelb*np.sin(30.*np.pi/180))-60.

print(ngelb)
print_A(popt[1], popt[2], 0.001, delmin_lambdagelb, lambdagelb*10**(-9))
print_A(popt[1], popt[2], 0.0015, delmin_lambdagelb, lambdagelb*10**(-9))







#--------------------------------------------------------------------------


MZn=1
Zn=np.zeros((MZn,5))
Bogenminuteliste1=[4,0,0]
Bogenminuteliste2=[22,20,22]
Zn[0,:]=np.array([481.05, 24+np.mean(Bogenminuteliste1)/60, phistd/np.sqrt(len(Bogenminuteliste1)), 147.5+np.mean(Bogenminuteliste2)/60, phistd/np.sqrt(len(Bogenminuteliste2))])



append01=np.reshape(np.array([0.5*Zn[:,3]-0.5*Zn[:,1]]), (MZn,1))
append02=np.reshape(np.array([np.sqrt((0.5*Zn[:,2])**2+(0.5*Zn[:,4])**2)*np.pi/180]), (MZn,1))
Zn = np.append(Zn, append01, axis=1)
Zn = np.append(Zn, append02, axis=1)
append03=np.reshape(np.array([np.sin((30+0.5*Zn[:,5])*np.pi/180)/np.sin(30*np.pi/180)]), (MZn,1))
append04=np.reshape(np.array([Zn[:,6]*np.absolute(np.cos((30+0.5*Zn[:,5])*np.pi/180))/(2*np.sin(30*np.pi/180))]), (MZn,1))
Zn = np.append(Zn, append03, axis=1)
Zn = np.append(Zn, append04, axis=1)
print(Zn)



#--------------------------------------------------------

#Zn:  0-Wellenlaenge*[nm]  1-phi1[grad]  2-ephi1[Grad]  3-phi2[grad]  4-ephi2[grad]  5-delmin[grad]  6-edelmin[radiant]  7-n[]  8-en[]  9-lambda_berechnet[m] 10-lamdba+delta[m]  11-lambda-delta[m]

print(popt)
def lambda_function(n_exp):
    return (2*(popt[2])/(-popt[1]+np.sqrt((popt[1])**2-4*popt[2]*(popt[0]-n_exp))))**(1/2)


print(lambda_function(1.75))

append05=np.reshape(np.array([lambda_function(Zn[:,7])]), (MZn,1))
append06=np.reshape(np.array([lambda_function(Zn[:,7]-Zn[:,8])]), (MZn,1))
append07=np.reshape(np.array([lambda_function(Zn[:,7]+Zn[:,8])]), (MZn,1))
Zn = np.append(Zn, append05, axis=1)
Zn = np.append(Zn, append06, axis=1)
Zn = np.append(Zn, append07, axis=1)

for i in range(MZn):
    print('${:.2f}$&${:.3f}$&${:.3f}$&${:.4f}$&${:.1f}$&${:.5f}$&${:.1f}$\\\\'.format(Zn[i,0], Zn[i,1], Zn[i,3], Zn[i,5], Zn[i,6]*10000, Zn[i,7], Zn[i,8]*100000))

print(Zn)
for i in range(MZn):
    
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
    text(x_theo+0.003e12, n_max-0.00005, s='$\\lambda_{{erwartet}}$={:.5}m'.format(l_theo), color='red')
    text(x_berp+0.001e12, n_berm, s='$\\lambda_{{+\\Delta}}$={:.5}m \n$\\lambda_{{exp}}$={:.5}m \n$\\lambda_{{-\\Delta}}$={:.5}m'.format(l_berm, l_ber, l_berp), color='blue')
    xlabel('$1/\\lambda^2$ in $m^{-2}$')
    ylabel('n')
    legend()
    ticklabel_format(useOffset=False, useMathText=True)
    savefig('Zn_{}.pdf'.format(i), bbox_inches = 'tight')
    
    show()
    close()



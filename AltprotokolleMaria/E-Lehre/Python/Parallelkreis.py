from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *
import scipy.optimize



#-----------R=47----------------
BereichsendwertI=0.21
Q=[]
eQ=[]
eQall=[]
#--------Methode Frequenz-------

fm=781.
fmm=769.
fmp=792.

fp=1759.
fpm=1739.
fpp=1779.

f0=1180.
f0m=1161.
f0p=1205.


efm=1/2*((fm-fmm)+(fmp-fm))
efp=1/2*((fp-fpm)+(fpp-fp))
ef0=1/2*((f0-f0m)+(f0p-f0))

deltaf=(fp-fm)
edeltaf=np.sqrt(efp**2+efm**2)

Qf=f0/deltaf
eQf=Qf*np.sqrt((ef0/f0)**2+(edeltaf/deltaf)**2)

#systematischer fehler = (0.02*I+0.005*0.21A)/sqrt(3), bei dieser methode ist nur offset relevant


offsetI = 0.005*0.21/np.sqrt(3) #0.0006


fmb=796.  #b=blau
fpb=1718.  #g=gruen
fmg=773.
fpg=1777.

Qfg=f0/(fpg-fmg)
Qfb=f0/(fpb-fmb)

eQfsys=0.5*((Qfb-Qf)+(Qf-Qfg))

print('f0={:.0f}+-{:.0f},  fm={:.0f}+-{:.0f}, f+={:.0f}+-{:.0f}'.format(f0, ef0, fm, efm, fp, efp))
print('R=47Ohm, Frequenzmethode, Guete={:.2f}+-{:.2f}(stat.)+-{:.2f}(sys.)'.format(Qf, eQf, eQfsys))

Q.append(1.250)
eQ.append(0)
eQall.append(0.003)


Q.append(Qf)
eQ.append(eQf)
eQall.append(eQf+eQfsys)

#-----------Methode Stromueberhoehung

I_CL=0.0107
I_CLm=0.0105
I_CLp=0.0109

I0=0.0091
I0m=0.0090
I0p=0.0092

eI_CL=0.5*((I_CLp-I_CL)+(I_CL-I_CLm))
eI0=0.5*((I0p-I0)+(I0-I0m))

QI=I_CL/I0
eQI=QI*np.sqrt((eI0/I0)**2+(eI_CL/I_CL)**2)


def Fehlersyst(Strom,IBreite):
    return (0.02*Strom+0.005*IBreite)/np.sqrt(3)

eQIsys=QI*np.sqrt((Fehlersyst(I0, BereichsendwertI)/I0)**2+(Fehlersyst(I_CL, BereichsendwertI)/I_CL)**2)



print('I_L={:.4f}+-{:.4f}'.format(I_CL, eI_CL))
print('I0={:.4f}+-{:.4f}'.format(I0, eI0))

print('R=47Ohm, Stromueberhoehungsmethode, Guete={:.2f}+-{:.2f}(stat)+-{:.2f}(sys)'.format(QI, eQI, eQIsys))

Q.append(QI)
eQ.append(eQI)
eQall.append(eQI+eQIsys)

#--------Graph

figure()
x=range(len(Q))
label=['Erwartung','Stromminimum','Stromüberhöhung']
errorbar(x, Q, yerr=eQall, linestyle='none', marker='o', markersize=6, elinewidth=1)
xticks(x,label, rotation='vertical')
margins(0.2)
ylabel('Q')
subplots_adjust(bottom=0.15)
savefig('P47_Fazit.pdf', bbox_inches = 'tight')
show()


#-----------R=100----------------
BereichsendwertI=0.21
Q=[]
eQ=[]
eQall=[]
#--------Methode Frequenz-------

fm=888.
fmm=881.
fmp=894.

fp=1475.
fpm=1470.
fpp=1483.

f0=1137.
f0m=1117.
f0p=1151.


efm=1/2*((fm-fmm)+(fmp-fm))
efp=1/2*((fp-fpm)+(fpp-fp))
ef0=1/2*((f0-f0m)+(f0p-f0))

deltaf=(fp-fm)
edeltaf=np.sqrt(efp**2+efm**2)

Qf=f0/deltaf
eQf=Qf*np.sqrt((ef0/f0)**2+(edeltaf/deltaf)**2)

#systematischer fehler = (0.02*I+0.005*0.21A)/sqrt(3), bei dieser methode ist nur offset relevant


offsetI = 0.005*0.21/np.sqrt(3) #0.0006


fmb=919.  #b=blau
fpb=1421.  #g=gruen
fmg=890.
fpg=1471.

Qfg=f0/(fpg-fmg)
Qfb=f0/(fpb-fmb)

eQfsys=0.5*((Qfb-Qf)+(Qf-Qfg))

print('f0={:.0f}+-{:.0f},  fm={:.0f}+-{:.0f}, f+={:.0f}+-{:.0f}'.format(f0, ef0, fm, efm, fp, efp))
print('R=100Ohm, Frequenzmethode, Guete={:.2f}+-{:.2f}(stat.)+-{:.2f}(sys.)'.format(Qf, eQf, eQfsys))

Q.append(2.297)
eQ.append(0)
eQall.append(0.006)


Q.append(Qf)
eQ.append(eQf)
eQall.append(eQf+eQfsys)

#-----------Methode Stromueberhoehung

I_CL=0.0107
I_CLm=0.0106
I_CLp=0.0108

I0=0.0051
I0m=0.0050
I0p=0.0052

eI_CL=0.5*((I_CLp-I_CL)+(I_CL-I_CLm))
eI0=0.5*((I0p-I0)+(I0-I0m))

QI=I_CL/I0
eQI=QI*np.sqrt((eI0/I0)**2+(eI_CL/I_CL)**2)


def Fehlersyst(Strom,IBreite):
    return (0.02*Strom+0.005*IBreite)/np.sqrt(3)

eQIsys=QI*np.sqrt((Fehlersyst(I0, BereichsendwertI)/I0)**2+(Fehlersyst(I_CL, BereichsendwertI)/I_CL)**2)



print('I_L={:.4f}+-{:.4f}'.format(I_CL, eI_CL))
print('I0={:.4f}+-{:.4f}'.format(I0, eI0))

print('R=100Ohm, Stromueberhoehungsmethode, Guete={:.2f}+-{:.2f}(stat)+-{:.2f}(sys)'.format(QI, eQI, eQIsys))

Q.append(QI)
eQ.append(eQI)
eQall.append(eQI+eQIsys)

#--------Graph

figure()
x=range(len(Q))
label=['Erwartung','Stromminimum','Stromüberhöhung']
errorbar(x, Q, yerr=eQall, linestyle='none', marker='o', markersize=6, elinewidth=1)
xticks(x,label, rotation='vertical')
margins(0.2)
ylabel('Q')
subplots_adjust(bottom=0.15)
savefig('P100_Fazit.pdf', bbox_inches = 'tight')
show()


#-----------R=inf----------------
BereichsendwertI=0.21
Q=[]
eQ=[]
eQall=[]
#--------Methode Frequenz-------

fm=1006.
fmm=1003.
fmp=1011.

fp=1216.
fpm=1216.
fpp=1224.

f0=1119.
f0m=1107.
f0p=1133.


efm=1/2*((fm-fmm)+(fmp-fm))
efp=1/2*((fp-fpm)+(fpp-fp))
ef0=1/2*((f0-f0m)+(f0p-f0))

deltaf=(fp-fm)
edeltaf=np.sqrt(efp**2+efm**2)

Qf=f0/deltaf
eQf=Qf*np.sqrt((ef0/f0)**2+(edeltaf/deltaf)**2)

#systematischer fehler = (0.02*I+0.005*0.21A)/sqrt(3), bei dieser methode ist nur offset relevant


offsetI = 0.005*0.21/np.sqrt(3) #0.0006


fmb=990.  #b=blau
fpb=1251.  #g=gruen
fmg=1029.
fpg=1204.

Qfg=f0/(fpg-fmg)
Qfb=f0/(fpb-fmb)

eQfsys=0.5*((Qfb-Qf)+(Qf-Qfg))

print('f0={:.0f}+-{:.0f},  fm={:.0f}+-{:.0f}, f+={:.0f}+-{:.0f}'.format(f0, ef0, fm, efm, fp, efp))
print('R=inf, Frequenzmethode, Guete={:.2f}+-{:.2f}(stat.)+-{:.2f}(sys.)'.format(Qf, eQf, eQfsys))

Q.append(8.532)
eQ.append(0)
eQall.append(0.026)


Q.append(Qf)
eQ.append(eQf)
eQall.append(eQf+eQfsys)

#-----------Methode Stromueberhoehung

I_CL=0.0109
I_CLm=0.0108
I_CLp=0.0111

I0=0.0022
I0m=0.0022
I0p=0.0023

eI_CL=0.5*((I_CLp-I_CL)+(I_CL-I_CLm))
eI0=0.5*((I0p-I0)+(I0-I0m))

QI=I_CL/I0
eQI=QI*np.sqrt((eI0/I0)**2+(eI_CL/I_CL)**2)


def Fehlersyst(Strom,IBreite):
    return (0.02*Strom+0.005*IBreite)/np.sqrt(3)

eQIsys=QI*np.sqrt((Fehlersyst(I0, BereichsendwertI)/I0)**2+(Fehlersyst(I_CL, BereichsendwertI)/I_CL)**2)



print('I_L={:.4f}+-{:.4f}'.format(I_CL, eI_CL))
print('I0={:.4f}+-{:.4f}'.format(I0, eI0))

print('R=inf, Stromueberhoehungsmethode, Guete={:.2f}+-{:.2f}(stat)+-{:.2f}(sys)'.format(QI, eQI, eQIsys))

Q.append(QI)
eQ.append(eQI)
eQall.append(eQI+eQIsys)

#--------Graph

figure()
x=range(len(Q))
label=['Erwartung','Stromminimum','Stromüberhöhung']
errorbar(x, Q, yerr=eQall, linestyle='none', marker='o', markersize=6, elinewidth=1)
xticks(x,label, rotation='vertical')
margins(0.2)
ylabel('Q')
subplots_adjust(bottom=0.15)
savefig('Pinf_Fazit.pdf', bbox_inches = 'tight')
show()

from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *
import scipy.optimize



L = 4.831e-3
RL = 3.749

C = 4.717e-6
R1 = 0.979

R5 = 5.184

R10 = 9.885




Q=[]
eQ=[]
eQall=[]
#-----------R=1----------------
BereichsendwertI=0.21
#--------Methode Frequenz-------

fm=957.5
fmm=955.8
fmp=959.1

fp=1173.2
fpm=1170.9
fpp=1175.1

f0=1060.3
f0m=1055.8
f0p=1064.4


efm=1/2*((fm-fmm)+(fmp-fm))
efp=1/2*((fp-fpm)+(fpp-fp))
ef0=1/2*((f0-f0m)+(f0p-f0))

deltaf=(fp-fm)
edeltaf=np.sqrt(efp**2+efm**2)

Qf=f0/deltaf
eQf=Qf*np.sqrt((ef0/f0)**2+(edeltaf/deltaf)**2)

#systematischer fehler = (0.02*I+0.005*0.21A)/sqrt(3), bei dieser methode ist nur offset relevant


offsetI = 0.005*0.7/np.sqrt(3) #0.002


fmb=958.8  #b=blau
fpb=1171.8  #g=gruen
fmg=956.0
fpg=1174.5

Qfg=f0/(fpg-fmg)
Qfb=f0/(fpb-fmb)

eQfsys=0.5*((Qfb-Qf)+(Qf-Qfg))

print('f0={:.0f}+-{:.0f},  fm={:.0f}+-{:.0f}, f+={:.0f}+-{:.0f}'.format(f0, ef0, fm, efm, fp, efp))
print('R=1Ohm, Frequenzmethode, Guete={:.2f}+-{:.2f}(stat.)+-{:.2f}(sys.)'.format(Qf, eQf, eQfsys))

#Oszilloskop
Q.append(5.83)
eQ.append(0.1)
eQall.append(0.1)

Q.append(6.769)
eQ.append(0)
eQall.append(0.018)


Q.append(Qf)
eQ.append(eQf)
eQall.append(np.sqrt(eQf**2+eQfsys**2))

#-----------Methode Spannungsueberhoehung------------------

U_CL=3.54
U_CLm=3.53
U_CLp=3.56

U0=0.71
eU0=0.01


eU_CL=0.5*((U_CLp-U_CL)+(U_CL-U_CLm))


QU=U_CL/U0
eQU=QU*np.sqrt((eU0/U0)**2+(eU_CL/U_CL)**2)


def Fehlersyst(Spannung,UBreite):
    return (0.01*Spannung+0.005*UBreite)/np.sqrt(3)

BereichsendwertU=7.
eQUsys=QU*np.sqrt((Fehlersyst(U_CL, BereichsendwertU)/U_CL)**2)

print('U_L={:.3f}+-{:.3f}'.format(U_CL, eU_CL))
print('R=1Ohm, Spannungsueberhoehungsmethode, Guete={:.2f}+-{:.2f}(stat)+-{:.2f}(sys)'.format(QU, eQU, eQUsys))


Q.append(QU)
eQ.append(eQU)
eQall.append(np.sqrt(eQU**2+eQUsys**2))
#-------------Methode Phase-------------


fm=964.9
fmm=964.3
fmp=965.5

fp=1173.3
fpm=1172.5
fpp=1174.2

f0=1062.6
f0m=1062.1
f0p=1063.2


efm=1/2*((fm-fmm)+(fmp-fm))
efp=1/2*((fp-fpm)+(fpp-fp))
ef0=1/2*((f0-f0m)+(f0p-f0))

deltaf=(fp-fm)
edeltaf=np.sqrt(efp**2+efm**2)

Qphi=f0/deltaf
eQphi=Qphi*np.sqrt((ef0/f0)**2+(edeltaf/deltaf)**2)


print('f0={:.0f}+-{:.0f},  fm={:.0f}+-{:.0f}, f+={:.0f}+-{:.0f}'.format(f0, ef0, fm, efm, fp, efp))
print('R=1Ohm, Phasenmethode, Guete={:.2f}+-{:.2f}(stat.)'.format(Qphi, eQphi))

Q.append(Qphi)
eQ.append(eQphi)
eQall.append(eQphi)

#--------Graph
Q_mean,Q_std = analyse.gewichtetes_mittel(np.array(Q),np.array(eQall))


figure()
x=range(len(Q))
label=['Oszilloskop','Erwartung','Strommaximum','Spannungsüberhöhung','Phase']
errorbar(x, Q, yerr=eQall, linestyle='none', marker='o', markersize=6, elinewidth=1)
#plot(x, Q_mean*np.ones(len(x)), label='Q_mean={:.2f}$\pm${:.2f}'.format(Q_mean, Q_std))
xticks(x,label, rotation='vertical')
margins(0.2)
ylabel('Q')
#legend()
subplots_adjust(bottom=0.15)
savefig('S1_Fazit.pdf', bbox_inches = 'tight')
show()
print(eQall)


Q=np.array(Q)
eQ=np.array(eQ)
Qmean,eQmean = analyse.gewichtetes_mittel(Q[2:], eQ[2:])
RRest=np.sqrt(L/C)/Qmean-RL-R1
eRRest=eQmean*np.sqrt(L/C)/Qmean**2
print("Restwiderstand: Cassy: gewichtetes Mittel Q={:.3f}+-{:.3f}, R_Rest={:.3f}+-{:.3f}".format(Qmean,eQmean, RRest, eRRest))

Qmean=Q[0]
eQmean=eQ[0]
RRest=np.sqrt(L/C)/Qmean-RL-R1
eRRest=eQmean*np.sqrt(L/C)/Qmean**2
print("Restwiderstand: Oszilloskop:  Q={:.3f}+-{:.3f}, R_Rest={:.3f}+-{:.3f}".format(Qmean,eQmean, RRest, eRRest))

#-----------R=5----------------


print("\n \n \n R=5 Ohm")
BereichsendwertI=0.21
Q=[]
eQ=[]
eQall=[]
#--------Methode Frequenz-------

fm=912.8
fmm=909.7
fmp=915.5

fp=1233.1
fpm=1229.6
fpp=1235.9

f0=1060.5
f0m=1054.9
f0p=1065.3


efm=1/2*((fm-fmm)+(fmp-fm))
efp=1/2*((fp-fpm)+(fpp-fp))
ef0=1/2*((f0-f0m)+(f0p-f0))

deltaf=(fp-fm)
edeltaf=np.sqrt(efp**2+efm**2)

Qf=f0/deltaf
eQf=Qf*np.sqrt((ef0/f0)**2+(edeltaf/deltaf)**2)

#systematischer fehler = (0.02*I+0.005*0.21A)/sqrt(3), bei dieser methode ist nur offset relevant


offsetI = 0.005*0.21/np.sqrt(3) #0.0006


fmb=914.2  #b=blau
fpb=1231.4  #g=gruen
fmg=911.7
fpg=1233.1

Qfg=f0/(fpg-fmg)
Qfb=f0/(fpb-fmb)

eQfsys=0.5*np.abs(((Qfb-Qf)+(Qf-Qfg)))

print('f0={:.0f}+-{:.0f},  fm={:.0f}+-{:.0f}, f+={:.0f}+-{:.0f}'.format(f0, ef0, fm, efm, fp, efp))
print('R=5Ohm, Frequenzmethode, Guete={:.2f}+-{:.2f}(stat.)+-{:.2f}(sys.)'.format(Qf, eQf, eQfsys))
print()

Q.append(3.583)
eQ.append(0)
eQall.append(0.009)

Q.append(Qf)
eQ.append(eQf)
eQall.append(np.sqrt(eQf**2+eQfsys**2))


#-----------Methode Spannungsueberhoehung------------------

U_CL=2.32
U_CLm=2.33
U_CLp=2.34

U0=0.71
eU0=0.01


eU_CL=0.5*((U_CLp-U_CL)+(U_CL-U_CLm))


QU=U_CL/U0
eQU=QU*np.sqrt((eU0/U0)**2+(eU_CL/U_CL)**2)


def Fehlersyst(Spannung,UBreite):
    return (0.01*Spannung+0.005*UBreite)/np.sqrt(3)

BereichsendwertU=7.
eQUsys=QU*np.sqrt((Fehlersyst(U_CL, BereichsendwertU)/U_CL)**2)

print('U_L={:.3f}+-{:.3f}'.format(U_CL, eU_CL))
print('R=5Ohm, Spannungsueberhoehungsmethode, Guete={:.2f}+-{:.2f}(stat)+-{:.2f}(sys)'.format(QU, eQU, eQUsys))


Q.append(QU)
eQ.append(eQU)
eQall.append(np.sqrt(eQU**2+eQUsys**2))
#-------------Methode Phase-------------

fm=915.5
fmm=913.8
fmp=917.2


fp=1237.7
fpm=1236.0
fpp=1239.3


f0=1062.9
f0m=1061.5
f0p=1064.6




efm=1/2*((fm-fmm)+(fmp-fm))
efp=1/2*((fp-fpm)+(fpp-fp))
ef0=1/2*((f0-f0m)+(f0p-f0))

deltaf=(fp-fm)
edeltaf=np.sqrt(efp**2+efm**2)

Qphi=f0/deltaf
eQphi=Qphi*np.sqrt((ef0/f0)**2+(edeltaf/deltaf)**2)


print('f0={:.0f}+-{:.0f},  fm={:.0f}+-{:.0f}, f+={:.0f}+-{:.0f}'.format(f0, ef0, fm, efm, fp, efp))
print('R=5Ohm, Phasenmethode, Guete={:.2f}+-{:.2f}(stat.)'.format(Qphi, eQphi))


Q.append(Qphi)
eQ.append(eQphi)
eQall.append(eQphi)


#--------Graph
Q_mean,Q_std = analyse.gewichtetes_mittel(np.array(Q),np.array(eQall))


figure()
x=range(len(Q))
label=['Erwartung','Strommaximum','Spannungsüberhöhung','Phase']
errorbar(x, Q, yerr=eQall, linestyle='none', marker='o', markersize=6, elinewidth=1)
#plot(x, Q_mean*np.ones(len(x)), label='Q_mean={:.2f}$\pm${:.2f}'.format(Q_mean, Q_std))
xticks(x,label, rotation='vertical')
margins(0.2)
ylabel('Q')
#legend()
subplots_adjust(bottom=0.15)
savefig('S5_Fazit.pdf', bbox_inches = 'tight')
show()
print(eQall)

Q=np.array(Q)
eQ=np.array(eQ)
Qmean,eQmean = analyse.gewichtetes_mittel(Q[1:], eQ[1:])
RRest=np.sqrt(L/C)/Qmean-RL-R5
eRRest=eQmean*np.sqrt(L/C)/Qmean**2
print("Restwiderstand: Cassy: gewichtetes Mittel Q={:.3f}+-{:.3f}, R_Rest={:.3f}+-{:.3f}".format(Qmean,eQmean, RRest, eRRest))




#-----------R=10----------------

print("\n \n \n R=10 Ohm")
BereichsendwertI=0.21
Q=[]
eQ=[]
eQall=[]
#--------Methode Frequenz-------

fm=849.2
fmm=847.3
fmp=852.1

fp=1323.1
fpm=1321.2
fpp=1325.0

f0=1058.0
f0m=1052.7
f0p=1056.6


efm=1/2*((fm-fmm)+(fmp-fm))
efp=1/2*((fp-fpm)+(fpp-fp))
ef0=1/2*((f0-f0m)+(f0p-f0))

deltaf=(fp-fm)
edeltaf=np.sqrt(efp**2+efm**2)

Qf=f0/deltaf
eQf=Qf*np.sqrt((ef0/f0)**2+(edeltaf/deltaf)**2)

#systematischer fehler = (0.02*I+0.005*0.21A)/sqrt(3), bei dieser methode ist nur offset relevant


offsetI = 0.005*0.21/np.sqrt(3) #0.0006


fmb=851.5  #b=blau
fpb=1320.1  #g=gruen
fmg=848.1
fpg=1325.5

Qfg=f0/(fpg-fmg)
Qfb=f0/(fpb-fmb)

eQfsys=0.5*((Qfb-Qf)+(Qf-Qfg))

print('f0={:.0f}+-{:.0f},  fm={:.0f}+-{:.0f}, f+={:.0f}+-{:.0f}'.format(f0, ef0, fm, efm, fp, efp))
print('R=10Ohm, Frequenzmethode, Guete={:.2f}+-{:.2f}(stat.)+-{:.2f}(sys.)'.format(Qf, eQf, eQfsys))

Q.append(2.347)
eQ.append(0)
eQall.append(0.006)

Q.append(Qf)
eQ.append(eQf)
eQall.append(np.sqrt(eQf**2+eQfsys**2))

#-----------Methode Spannungsueberhoehung------------------

U_CL=1.57
U_CLm=1.57
U_CLp=1.58

U0=0.71
eU0=0.01


eU_CL=0.5*((U_CLp-U_CL)+(U_CL-U_CLm))


QU=U_CL/U0
eQU=QU*np.sqrt((eU0/U0)**2+(eU_CL/U_CL)**2)


def Fehlersyst(Spannung,UBreite):
    return (0.01*Spannung+0.005*UBreite)/np.sqrt(3)

BereichsendwertU=7.
eQUsys=QU*np.sqrt((Fehlersyst(U_CL, BereichsendwertU)/U_CL)**2)

print('U_L={:.3f}+-{:.3f}'.format(U_CL, eU_CL))
print('R=10Ohm, Spannungsueberhoehungsmethode, Guete={:.2f}+-{:.2f}(stat)+-{:.2f}(sys)'.format(QU, eQU, eQUsys))

Q.append(QU)
eQ.append(eQU)
eQall.append(np.sqrt(eQU**2+eQUsys**2))

#-------------Methode Phase-------------

fm=852.5
fmm=851.5
fmp=853.7


fp=1334.4
fpm=1332.9
fpp=1336.5


f0=1063.2
f0m=1060.2
f0p=1065.1




efm=1/2*((fm-fmm)+(fmp-fm))
efp=1/2*((fp-fpm)+(fpp-fp))
ef0=1/2*((f0-f0m)+(f0p-f0))

deltaf=(fp-fm)
edeltaf=np.sqrt(efp**2+efm**2)

Qphi=f0/deltaf
eQphi=Qphi*np.sqrt((ef0/f0)**2+(edeltaf/deltaf)**2)


print('f0={:.0f}+-{:.0f},  fm={:.0f}+-{:.0f}, f+={:.0f}+-{:.0f}'.format(f0, ef0, fm, efm, fp, efp))
print('R=10Ohm, Phasenmethode, Guete={:.2f}+-{:.2f}(stat.)'.format(Qphi, eQphi))


Q.append(Qphi)
eQ.append(eQphi)
eQall.append(eQphi)

#--------Graph
Q_mean,Q_std = analyse.gewichtetes_mittel(np.array(Q),np.array(eQall))


figure()
x=range(len(Q))
label=['Erwartung','Strommaximum','Spannungsüberhöhung','Phase']
errorbar(x, Q, yerr=eQall, linestyle='none', marker='o', markersize=6, elinewidth=1)
#plot(x, Q_mean*np.ones(len(x)), label='Q_mean={:.2f}$\pm${:.2f}'.format(Q_mean, Q_std))
xticks(x,label, rotation='vertical')
margins(0.2)
ylabel('Q')
#legend()
subplots_adjust(bottom=0.15)
savefig('S10_Fazit.pdf', bbox_inches = 'tight')
show()
print(eQall)




#-----------------Restwiderstaende

Q=np.array(Q)
eQ=np.array(eQ)
Qmean,eQmean = analyse.gewichtetes_mittel(Q[1:], eQ[1:])
RRest=np.sqrt(L/C)/Qmean-RL-R10
eRRest=eQmean*np.sqrt(L/C)/Qmean**2
print("Restwiderstand: Cassy: gewichtetes Mittel Q={:.3f}+-{:.3f}, R_Rest={:.3f}+-{:.3f}".format(Qmean,eQmean, RRest, eRRest))

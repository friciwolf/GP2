from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *
import scipy.optimize


Q=[]
eQ=[]
eQall=[]
#-----------R=1----------------
BereichsendwertI=0.21
#--------Methode Frequenz-------

fm=984
fmm=982
fmp=985

fp=1156
fpm=1154
fpp=1157

f0=1065
f0m=1060
f0p=1072


efm=1/2*((fm-fmm)+(fmp-fm))
efp=1/2*((fp-fpm)+(fpp-fp))
ef0=1/2*((f0-f0m)+(f0p-f0))

deltaf=(fp-fm)
edeltaf=np.sqrt(efp**2+efm**2)

Qf=f0/deltaf
eQf=Qf*np.sqrt((ef0/f0)**2+(edeltaf/deltaf)**2)

#systematischer fehler = (0.02*I+0.005*0.21A)/sqrt(3), bei dieser methode ist nur offset relevant


offsetI = 0.005*0.21/np.sqrt(3) #0.0006


fmb=985  #b=blau
fpb=1155  #g=gruen
fmg=984
fpg=1156

Qfg=f0/(fpg-fmg)
Qfb=f0/(fpb-fmb)

eQfsys=0.5*((Qfb-Qf)+(Qf-Qfg))

print('f0={:.0f}+-{:.0f},  fm={:.0f}+-{:.0f}, f+={:.0f}+-{:.0f}'.format(f0, ef0, fm, efm, fp, efp))
print('R=1Ohm, Frequenzmethode, Guete={:.2f}+-{:.2f}(stat.)+-{:.2f}(sys.)'.format(Qf, eQf, eQfsys))

#Oszilloskop
Q.append(5.44)
eQ.append(0.16)
eQall.append(0.16)

Q.append(6.757)
eQ.append(0)
eQall.append(0.018)


Q.append(Qf)
eQ.append(eQf)
eQall.append(eQf+eQfsys)

#-----------Methode Spannungsueberhoehung------------------

U_CL=2.19
U_CLm=2.18
U_CLp=2.21

U0=0.351
eU0=0.001


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
eQall.append(eQU+eQUsys)
#-------------Methode Phase-------------


fm=986
fmm=983
fmp=989

fp=1157
fpm=1154
fpp=1159

f0=1068
f0m=1065
f0p=1070


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

#-----------R=5----------------
BereichsendwertI=0.21
Q=[]
eQ=[]
eQall=[]
#--------Methode Frequenz-------

fm=922
fmm=919
fmp=924

fp=1234
fpm=1231
fpp=1236

f0=1065
f0m=1059
f0p=1070


efm=1/2*((fm-fmm)+(fmp-fm))
efp=1/2*((fp-fpm)+(fpp-fp))
ef0=1/2*((f0-f0m)+(f0p-f0))

deltaf=(fp-fm)
edeltaf=np.sqrt(efp**2+efm**2)

Qf=f0/deltaf
eQf=Qf*np.sqrt((ef0/f0)**2+(edeltaf/deltaf)**2)

#systematischer fehler = (0.02*I+0.005*0.21A)/sqrt(3), bei dieser methode ist nur offset relevant


offsetI = 0.005*0.21/np.sqrt(3) #0.0006


fmb=920  #b=blau
fpb=1237  #g=gruen
fmg=924
fpg=1232

Qfg=f0/(fpg-fmg)
Qfb=f0/(fpb-fmb)

eQfsys=0.5*np.abs(((Qfb-Qf)+(Qf-Qfg)))

print('f0={:.0f}+-{:.0f},  fm={:.0f}+-{:.0f}, f+={:.0f}+-{:.0f}'.format(f0, ef0, fm, efm, fp, efp))
print('R=5Ohm, Frequenzmethode, Guete={:.2f}+-{:.2f}(stat.)+-{:.2f}(sys.)'.format(Qf, eQf, eQfsys))
print()

Q.append(3.564)
eQ.append(0)
eQall.append(0.009)

Q.append(Qf)
eQ.append(eQf)
eQall.append(eQf+eQfsys)


#-----------Methode Spannungsueberhoehung------------------

U_CL=1.194
U_CLm=1.192
U_CLp=1.197

U0=0.351
eU0=0.001


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
eQall.append(eQU+eQUsys)
#-------------Methode Phase-------------

fm=924.
fmm=922.
fmp=927.


fp=1238.
fpm=1236.
fpp=1240.


f0=1069.
f0m=1067.
f0p=1070.




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
#-----------R=10----------------
BereichsendwertI=0.21
Q=[]
eQ=[]
eQall=[]
#--------Methode Frequenz-------

fm=858
fmm=856
fmp=862

fp=1324
fpm=1321
fpp=1327

f0=1065
f0m=1055
f0p=1076


efm=1/2*((fm-fmm)+(fmp-fm))
efp=1/2*((fp-fpm)+(fpp-fp))
ef0=1/2*((f0-f0m)+(f0p-f0))

deltaf=(fp-fm)
edeltaf=np.sqrt(efp**2+efm**2)

Qf=f0/deltaf
eQf=Qf*np.sqrt((ef0/f0)**2+(edeltaf/deltaf)**2)

#systematischer fehler = (0.02*I+0.005*0.21A)/sqrt(3), bei dieser methode ist nur offset relevant


offsetI = 0.005*0.21/np.sqrt(3) #0.0006


fmb=860  #b=blau
fpb=1320  #g=gruen
fmg=853
fpg=1331

Qfg=f0/(fpg-fmg)
Qfb=f0/(fpb-fmb)

eQfsys=0.5*((Qfb-Qf)+(Qf-Qfg))

print('f0={:.0f}+-{:.0f},  fm={:.0f}+-{:.0f}, f+={:.0f}+-{:.0f}'.format(f0, ef0, fm, efm, fp, efp))
print('R=10Ohm, Frequenzmethode, Guete={:.2f}+-{:.2f}(stat.)+-{:.2f}(sys.)'.format(Qf, eQf, eQfsys))

Q.append(2.337)
eQ.append(0)
eQall.append(0.006)

Q.append(Qf)
eQ.append(eQf)
eQall.append(eQf+eQfsys)

#-----------Methode Spannungsueberhoehung------------------

U_CL=0.797
U_CLm=0.794
U_CLp=0.792

U0=0.351
eU0=0.001


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
eQall.append(eQU+eQUsys)

#-------------Methode Phase-------------

fm=860.
fmm=858.
fmp=863.


fp=1335
fpm=1333.
fpp=1337.


f0=1068.
f0m=1070.
f0p=1072.




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



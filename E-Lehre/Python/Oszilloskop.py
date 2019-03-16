import numpy as np
import matplotlib.pyplot as plt
from praktikum import analyse


#--------Rohdaten---------------
f0, ef0 = analyse.gewichtetes_mittel(np.array([1062.,1062.]), np.array([1.,1.]))
fminus, efminus = analyse.gewichtetes_mittel(np.array([974.,976.]), np.array([1.,4.]))
fplus, efplus = analyse.gewichtetes_mittel(np.array([1157.,1155.]), np.array([4.,5.]))




#---------Rechnung--------------
deltaf=fplus-fminus

edeltaf=np.sqrt(efplus**2+efminus**2)

Q_osz=f0/(deltaf)


eQ_osz=Q_osz*np.sqrt((ef0/f0)**2+(edeltaf/deltaf)**2)


print("Q_oszilloskop = {:.2f} +- {:.2f}".format(Q_osz,eQ_osz))

###############################################
#-------------Erwartung----------------------
#################################################3

#--------------Rohdaten----------------

L = 4.831e-3
eL = 0.0025*L
RL = 3.749
eRL = 0.0025*RL

C = 4.717e-6
eC = 0.0025*C

R1 = 0.979
eR1 = 0.0025*R1
R5 = 5.184
eR5 = 0.0025*R5
R10 = 9.885
eR10 = 0.0025*R10
#R20 = 19.75
#eR20 = 0.0025*R20
R47 = 46.60
eR47 = 0.0025*R47

R100=99.15
eR100 = 0.0025*R100

f_erwartet=1/(np.sqrt(L*C)*2*np.pi)
ef_erwartet=f_erwartet*np.sqrt((eL/2/L)**2+(eC/2/C)**2)
print('erwartete Resonanzfrequenz: f_0={:.1f}+-{:.1f}'.format(f_erwartet, ef_erwartet))


def Q_erwartung_serie(Widerstand, eWiderstand):
    Q = 1/(Widerstand+RL)*np.sqrt(L/C)
    eQsquare = (eRL/(RL+Widerstand)**2*np.sqrt(L/C))**2+(eWiderstand/(RL+Widerstand)**2*np.sqrt(L/C))**2+(eL/(RL+Widerstand)*1/(2*(np.sqrt(L*C))))**2+(eC/(RL+Widerstand)*1/2*np.sqrt(L/C**3))**2
    eQ = np.sqrt(eQsquare)
    return Q, eQ

print('Berechnung der Guete durch Baueteile:')
print("Serienschwingkreis")

for Ri in (R1,R5,R10,R47,R100):
    print('R = {:.2f} , Q = {:.3f} +- {:.3f}(syst.)'.format(Ri, *Q_erwartung_serie(Ri,Ri*0.0025)))
    
'''
L=4.7e-3
RL=3.7
C=4.617e-6
R47=46.68
eL=0.0025*L
eC=0.0025*C
eRL=0.0025*RL
'''

def Q_erwartung_parallel(Widerstand, eWiderstand):
    Q = (Widerstand*np.sqrt(C/L)/(1+Widerstand*RL*(C/L)))
    eiQ2=(eWiderstand/(Widerstand)**2*np.sqrt(L/C))**2+(eL/(Widerstand)*1/(2*(np.sqrt(L*C))))**2+(eC/(Widerstand)*1/2*np.sqrt(L/C**3))**2+(eRL*np.sqrt(C/L))**2+(eL*RL*np.sqrt(C/L**3)/2)**2+(eC*RL*np.sqrt(1/C/L)/2)**2
    eiQ=np.sqrt(eiQ2)
    eQ = Q**2*eiQ
    return Q, eQ



print("Parallelschwingkreis")
for Ri in (R47, R100):
    print('R = {:.2f} , Q = {:.4f} +- {:.4f}(syst.)'.format(Ri, *Q_erwartung_parallel(Ri,Ri*0.0025)))
    
print('R = inf , Q = {:.3f} +- {:.3f}(syst.)'.format((1/RL*np.sqrt(L/C)), np.sqrt((eRL/(RL)**2*np.sqrt(L/C))**2+(eL/(RL)*1/(2*(np.sqrt(L*C))))**2+(eC/(RL)*1/2*np.sqrt(L/C**3))**2)))



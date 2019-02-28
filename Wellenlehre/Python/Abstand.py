from __future__ import print_function

from praktikum import cassy1
from praktikum import cassy
import praktikum.analyse as anal
import numpy as np
from pylab import *

Afakt=[]
Afaktsys=[]


#Auswertung Abstand 3
print("Abstand3")
data = cassy1.lese_lab_datei('../Rohdaten/Abstand3.lab')

R1 = data[:,3]
U1 = data[:,2]

eR1=3/4096/sqrt(12)*np.ones(len(R1))
eU1=1/4096/sqrt(12)*np.ones(len(U1))
x
K, eK = np.genfromtxt('K.txt')

S0 = 25.3
eS0 = 0.1
R0 = 1.160

s1 = S0 + K*(R1-R0) 

es1 = sqrt(2)*K*eR1


#Plot Rohdaten
figure()
plot(R1, U1, color="lightgrey", linewidth=1)
scatter(R1, U1, s=1)
ylabel('U / V')
xlabel('R / $k\\Omega$')
legend(title='Abstandsmessung Rohdaten')
savefig('Abstandsmessung_Rohdaten3.pdf', bbox_inches = 'tight')

show()
close()



#systematische Fehler auf s in cm
esyss = sqrt(eS0**2 + (eK*(R1-R0))**2)


#Lineare Regression
x = np.array(np.log(s1))
y = np.array(np.log(U1))
ex = np.array(es1/s1)
ey = np.array(eU1/U1)
xl = "log(s/cm)"
yl = "log(U/V)"
xeinheit = ""
yeinheit = ""

a,ea,b,eb,chiq,corr = anal.lineare_regression_xy(x,y,ex,ey)

plt.errorbar(x,y, ey, ex, marker="x", linestyle="None", capsize=5)
l = max(x)-min(x)
x2 = np.arange(min(x)-l*0.1, max(x)+l*0.1, l/1000)
y2 = a*x2+b
plt.plot(x2, y2, color="orange")
plt.xlabel(xl+" [{}]".format(yeinheit))
plt.ylabel(yl+" [{}]".format(xeinheit))
plt.legend(title="Lineare Regression\n{} = ({:.2f} ± {:.2f}){} $\cdot$ {}+({:.2f}±{:.2f}){}\n$\chi^2 /NDF={:.2f}$".format(yl,a,ea, xeinheit,xl,b, eb, yeinheit, chiq/(len(x)-2)), loc=1)
plt.savefig('Abstand3_LinReg.pdf', bbox_inches = 'tight')
plt.show()
plt.close()


plt.errorbar(x,y-(a*x+b), np.sqrt(ex**2*a**2+ey**2), marker="x", linestyle="None", capsize=5)
plt.axhline(0, color="orange")
plt.xlabel(xl+" [{}]".format(yeinheit))
plt.ylabel(yl+" [{}]".format(xeinheit))
plt.savefig('Abstand3_Residuen.pdf', bbox_inches = 'tight')
plt.show()
plt.close()

Afakt.append(a)

#Verschiebemethode
s1p=s1+esyss
ap,ea,b,eb,chiq,corr = anal.lineare_regression_xy(np.log(s1p),np.log(U1),es1/s1p,eU1/U1)
s1m=s1-esyss
am,ea,b,eb,chiq,corr = anal.lineare_regression_xy(np.log(s1m),np.log(U1),es1/s1m,eU1/U1)
print("Steigungen mit Verschiebemethode: {:.3f}, {:.3f}".format(am, ap))
Afaktsys.append(max(np.abs(ap-a), np.abs(a-am)))
print(Afaktsys)



#------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
#Auswertung Abstand4
print("Abstand4")

data = cassy1.lese_lab_datei('../Rohdaten/Abstand4.lab')

R1 = data[:,3]
U1 = data[:,2]

eR1=3/4096/sqrt(12)*np.ones(len(R1))
eU1=1/4096/sqrt(12)*np.ones(len(U1))

K, eK = np.genfromtxt('K.txt')

S0 = 25.3
eS0 = 0.1
R0 = 1.160

s1 = S0 + K*(R1-R0) 

es1 = sqrt(2)*K*eR1


#Plot Rohdaten
figure()
plot(R1, U1, color="lightgrey", linewidth=1)
scatter(R1, U1, s=1)
ylabel('U / V')
xlabel('R / $k\\Omega$')
legend(title='Abstandsmessung Rohdaten')
savefig('Abstandsmessung_Rohdaten4.pdf', bbox_inches = 'tight')

show()
close()



#systematische Fehler auf s in cm
esyss = sqrt(eS0**2 + (eK*(R1-R0))**2)


#Lineare Regression
x = np.array(np.log(s1))
y = np.array(np.log(U1))
ex = np.array(es1/s1)
ey = np.array(eU1/U1)
xl = "log(s/cm)"
yl = "log(U/V)"
xeinheit = ""
yeinheit = ""

a,ea,b,eb,chiq,corr = anal.lineare_regression_xy(x,y,ex,ey)

plt.errorbar(x,y, ey, ex, marker="x", linestyle="None", capsize=5)
l = max(x)-min(x)
x2 = np.arange(min(x)-l*0.1, max(x)+l*0.1, l/1000)
y2 = a*x2+b
plt.plot(x2, y2, color="orange")
plt.xlabel(xl+" [{}]".format(yeinheit))
plt.ylabel(yl+" [{}]".format(xeinheit))
plt.legend(title="Lineare Regression\n{} = ({:.2f} ± {:.2f}){} $\cdot$ {}+({:.2f}±{:.2f}){}\n$\chi^2 /NDF={:.2f}$".format(yl,a,ea, xeinheit,xl,b, eb, yeinheit, chiq/(len(x)-2)), loc=1)
plt.savefig('Abstand4_LinReg.pdf', bbox_inches = 'tight')
plt.show()
plt.close()


plt.errorbar(x,y-(a*x+b), np.sqrt(ex**2*a**2+ey**2), marker="x", linestyle="None", capsize=5)
plt.axhline(0, color="orange")
plt.xlabel(xl+" [{}]".format(yeinheit))
plt.ylabel(yl+" [{}]".format(xeinheit))
plt.savefig('Abstand4_Residuen.pdf', bbox_inches = 'tight')
plt.show()
plt.close()

Afakt.append(a)

#Verschiebemethode
s1p=s1+esyss
ap,ea,b,eb,chiq,corr = anal.lineare_regression_xy(np.log(s1p),np.log(U1),es1/s1p,eU1/U1)
s1m=s1-esyss
am,ea,b,eb,chiq,corr = anal.lineare_regression_xy(np.log(s1m),np.log(U1),es1/s1m,eU1/U1)
print("Steigungen mit Verschiebemethode: {:.3f}, {:.3f}".format(am, ap))
Afaktsys.append(max(np.abs(ap-a), np.abs(a-am)))
print(Afaktsys)


#------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
#Auswertung Abstand5
print("Abstand5")

data = cassy1.lese_lab_datei('../Rohdaten/Abstand5.lab')

R1 = data[:,3]
U1 = data[:,2]

eR1=3/4096/sqrt(12)*np.ones(len(R1))
eU1=1/4096/sqrt(12)*np.ones(len(U1))

K, eK = np.genfromtxt('K.txt')

S0 = 25.3
eS0 = 0.1
R0 = 1.160

s1 = S0 + K*(R1-R0) 

es1 = sqrt(2)*K*eR1


#Plot Rohdaten
figure()
plot(R1, U1, color="lightgrey", linewidth=1)
scatter(R1, U1, s=1)
ylabel('U / V')
xlabel('R / $k\\Omega$')
legend(title='Abstandsmessung Rohdaten')
savefig('Abstandsmessung_Rohdaten5.pdf', bbox_inches = 'tight')

show()
close()



#systematische Fehler auf s in cm
esyss = sqrt(eS0**2 + (eK*(R1-R0))**2)


#Lineare Regression
x = np.array(np.log(s1))
y = np.array(np.log(U1))
ex = np.array(es1/s1)
ey = np.array(eU1/U1)
xl = "log(s/cm)"
yl = "log(U/V)"
xeinheit = ""
yeinheit = ""

a,ea,b,eb,chiq,corr = anal.lineare_regression_xy(x,y,ex,ey)

plt.errorbar(x,y, ey, ex, marker="x", linestyle="None", capsize=5)
l = max(x)-min(x)
x2 = np.arange(min(x)-l*0.1, max(x)+l*0.1, l/1000)
y2 = a*x2+b
plt.plot(x2, y2, color="orange")
plt.xlabel(xl+" [{}]".format(yeinheit))
plt.ylabel(yl+" [{}]".format(xeinheit))
plt.legend(title="Lineare Regression\n{} = ({:.2f} ± {:.2f}){} $\cdot$ {}+({:.2f}±{:.2f}){}\n$\chi^2 /NDF={:.2f}$".format(yl,a,ea, xeinheit,xl,b, eb, yeinheit, chiq/(len(x)-2)), loc=1)
plt.savefig('Abstand5_LinReg.pdf', bbox_inches = 'tight')
plt.show()
plt.close()


plt.errorbar(x,y-(a*x+b), np.sqrt(ex**2*a**2+ey**2), marker="x", linestyle="None", capsize=5)
plt.axhline(0, color="orange")
plt.xlabel(xl+" [{}]".format(yeinheit))
plt.ylabel(yl+" [{}]".format(xeinheit))
plt.savefig('Abstand5_Residuen.pdf', bbox_inches = 'tight')
plt.show()
plt.close()

Afakt.append(a)

#Verschiebemethode
s1p=s1+esyss
ap,ea,b,eb,chiq,corr = anal.lineare_regression_xy(np.log(s1p),np.log(U1),es1/s1p,eU1/U1)
s1m=s1-esyss
am,ea,b,eb,chiq,corr = anal.lineare_regression_xy(np.log(s1m),np.log(U1),es1/s1m,eU1/U1)
print("Steigungen mit Verschiebemethode: {:.3f}, {:.3f}".format(am, ap))
Afaktsys.append(max(np.abs(ap-a), np.abs(a-am)))
print(Afaktsys)



#------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
#Ergebnisse Zusammenfassen
print("\n \n")
print("Steigungen der drei Messungen:", Afakt)

afakt=np.mean(Afakt)
estatafakt=np.std(Afakt, ddof=1)
esysafakt=max(Afaktsys)
print("gemittelte Steigung mit Abweichung: {:.3f} ± {:.3f}(stat.) ± {:.3f}(sys.)".format(afakt,estatafakt,esysafakt))


np.savetxt('afakt.txt', [[afakt,estatafakt, esysafakt]], header="a-Faktor Umrechnung Spannung in Intensität, stat. Fehler, syst. Fehler")






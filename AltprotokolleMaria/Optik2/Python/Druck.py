#! /usr/bin/env python


from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *
import scipy.optimize



lambdag=np.genfromtxt('wellenlaenge-Julian.txt')[0]
elambdag=np.genfromtxt('wellenlaenge-Julian.txt')[1]+np.genfromtxt('wellenlaenge-Julian.txt')[2]

L=0.01   #in m

em=0.1
eP=5

#----------------Rohdaten-------------------------------------------------------
def Rohdaten():

    
    MR0=np.array([995,869,804,718,613,508,410,312,220])
    MR1=np.array([995,930,842,725,645,539,420,316])
    MR2=np.array([995,850,761,659,557,450,360,270])
    MR3=np.array([995,902,772,700,600,490,390,300])
    MR4=np.array([995,880,786,642,496,392,312])
    MR5=np.array([995,900,811,719,618,520,413,375,278])
    MR6=np.array([995,896,807,712,614,504,459,390,353,325,260])
    MR7=np.array([995,904,822,708,625,513,420,302])
    
    MR=[MR0,MR1,MR2,MR3,MR4,MR5,MR6,MR7]
    print(MR)
    
    
    a=np.array([])
    ea=np.array([])
    b=np.array([])
    eb=np.array([])
    chiq=np.array([])
    
    
    
    for i in (2,5,6):
    
        xwerte=MR[i]
        ywerte=range(len(MR[i]))
        eywerte=0.1*np.ones(len(xwerte))
        exwerte=7*np.ones(len(ywerte))
        name='MR'+str(i)
        print(xwerte)
        
        
        ai,eai,bi,ebi,chiqi,corri = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
        
        print('\n\n\n\nMessreihe {}'.format(i))
        print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(ai,eai,bi,ebi,chiqi,corri))
        print('damit waere delta_n/delta_p={}'.format(ai*lambdag/(2*0.01)))
        a=np.append(a, ai)
        ea=np.append(ea,eai)
        b=np.append(b, bi)
        eb=np.append(eb,ebi)
        chiq=np.append(chiq,chiqi)
        
        
        figure()
        #title('Lineare Regression der Abstandskalibrierung')
        errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
        plot(xwerte, ai*xwerte+bi, '-', zorder=2)
        xlabel('P / hPa')
        ylabel('m')
        legend(title='Lineare Regression \nSteigung[1/hPa]: ${:.5f}\\pm{:.5f}$ \ny-Achsenabschnitt: ${:.2f}\\pm{:.2f}$ \nDatenpunkte: {}'.format(ai, eai, bi, ebi, len(xwerte)))
        savefig('{}_LinReg_Rohdaten.pdf'.format(name), bbox_inches = 'tight')
        show()
        
        
        figure()
        #title('Residuenplot der Abstandskalibrierung')
        errorbar(x=xwerte, y=ywerte-(ai*xwerte+bi), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
        plot(xwerte, 0.*xwerte, zorder=2) # Linie bei Null 
        xlabel('P / hPa-')
        ylabel('m - Fitgerade')
        legend(title='Residuenplot \n $X^2/n_{{df}}$ = {:.2f}'.format(chiqi/(len(xwerte)-2)))
        savefig('{}_Residuen_Rohdaten.pdf'.format(name), bbox_inches = 'tight')
        
        show()
Rohdaten()

#-----------Methode1-----------------------------------------------------------
def Methode1():
    #  Ausschliessen von Punkten, bei denen wir uns verzaehlt haben
        
    MR0=np.array([995,869,804,718,613,508,410,312,220])
    MR1=np.array([995,930,842,725,645,539,420,316]) 
    MR2=np.array([850,761,659,557,450,360,270])    # erster wurde geloescht
    MR3=np.array([995,902,772,700,600,490,390,300])
    MR4=np.array([995,880,786,642,496,392,312])
    MR5=np.array([995,900,811,719,618,520,413])    #letzten beiden wurden geloescht
    MR6=np.array([995,896,807,712,614,504])       #letzten fuenf wurden geloescht
    MR7=np.array([995,904,822,708,625,513,420,302])
    
    MR=[MR0,MR1,MR2,MR3,MR4,MR5,MR6,MR7]
    print(MR)


    a=np.array([])
    ea=np.array([])
    b=np.array([])
    eb=np.array([])
    chiq=np.array([])
    
    
    
    for i in range(8):
    
        xwerte=MR[i]
        ywerte=range(len(MR[i]))
        eywerte=em*np.ones(len(xwerte))
        exwerte=eP*np.ones(len(ywerte))
        name='MR'+str(i)
        print(xwerte)
        
        
        ai,eai,bi,ebi,chiqi,corri = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
        
        print('\n\n\n\nMessreihe {}'.format(i))
        print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(ai,eai,bi,ebi,chiqi,corri))
        print('damit waere delta_n/delta_p={}'.format(ai*lambdag/(2*0.01)))
        a=np.append(a, ai)
        ea=np.append(ea,eai)
        b=np.append(b, bi)
        eb=np.append(eb,ebi)
        chiq=np.append(chiq,chiqi)
        
        
        figure()
        #title('Lineare Regression der Abstandskalibrierung')
        errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
        plot(xwerte, ai*xwerte+bi, '-', zorder=2)
        xlabel('P / hPa')
        ylabel('m')
        legend(title='Lineare Regression \nSteigung[1/hPa]: ${:.5f}\\pm{:.5f}$ \ny-Achsenabschnitt: ${:.2f}\\pm{:.2f}$ \nDatenpunkte: {}'.format(ai, eai, bi, ebi, len(xwerte)))
        savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
        show()
        
        
        figure()
        #title('Residuenplot der Abstandskalibrierung')
        errorbar(x=xwerte, y=ywerte-(ai*xwerte+bi), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
        plot(xwerte, 0.*xwerte, zorder=2) # Linie bei Null 
        xlabel('P / hPa-')
        ylabel('m - Fitgerade')
        legend(title='Residuenplot \n $X^2/n_{{df}}$ = {:.2f}'.format(chiqi/(len(xwerte)-2)))
        savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')
        
        show()
    
    NP=np.array([]) # NP = Delta N / Delta P 
    eNP_stat=np.array([])
    eNP_sys=np.array([])
    
    eNP_stat=np.array([])
    for i in range(8):
        print('Messreihe {}:   a={:.5f}+-{:.5f},   NP=-a*lambda/(2L)={:.3f}e-7,   eNP_stat=ea*lambda/(2L)={:.3f}e-7, eNP_sys=a*elambda/(2L)={:.3f}e-7'.format(i, a[i],ea[i], -a[i]*lambdag/(2*L)*10**7, ea[i]*lambdag/(2*L)*10**7, -a[i]*elambdag/(2*L)*10**7))
        NP=np.append(NP, -a[i]*lambdag/(2*L))
        eNP_stat=np.append(eNP_stat, ea[i]*lambdag/(2*L))
        eNP_sys=np.append(eNP_sys, -a[i]*elambdag/(2*L))
    
    for i in range(8):
        print('{:.0f}&{:.3f}$\pm${:.3f}&{:.3f}&{:.3f}&{:.3f}\\\\'.format(i, -a[i]*100,ea[i]*100, -a[i]*lambdag/(2*L)*10**7, ea[i]*lambdag/(2*L)*10**7, -a[i]*elambdag/(2*L)*10**7))
    
    figure()
    errorbar(x=range(8), y=NP,yerr=eNP_stat,linestyle='none', marker='o')
    ylabel('$\\Delta n / \\Delta P$ [1/hPa]')
    xlabel('MR')
    ticklabel_format(useMathText=True)
    savefig('Methode1_Ergebnisse.pdf'.format(name), bbox_inches = 'tight')
    show()

    
    
    NP_kompat=np.delete(NP, 4)
    eNP_stat_kompat=np.delete(eNP_stat,4)
    
    NP_mean, eNP_stat_mean = analyse.gewichtetes_mittel(NP_kompat,eNP_stat_kompat)
    eNP_sys_mean = max(eNP_sys)
    print('Ergebnis nach gewichtetes Mittel: NP = {:.3f}e-7  +- {:.3f}e-7(stat) +-{:.3f}e-7(sys), SigmaUmgebung={:.1f}'.format(NP_mean*10**7, eNP_stat_mean*10**7, eNP_sys_mean*10**7, (NP_mean*10**7-2.655)/((eNP_stat_mean+eNP_sys_mean)*10**7)))

Methode1()









#----------Methode2-------------------------------------------------------------

MR0=np.array([995,869,804,718,613,508,410,312,220])
MR1=np.array([995,930,842,725,645,539,420,316]) 
MR2=np.array([995,850,761,659,557,450,360,270])    
MR3=np.array([995,902,772,700,600,490,390,300])
MR4=np.array([995,880,786,642,496,392,312])
MR5=np.array([995,900,811,719,618,520,413])    #letzten beiden wurden geloescht
MR6=np.array([995,896,807,712,614,504])       #letzten fuenf wurden geloescht
MR7=np.array([995,904,822,708,625,513,420,302])

MR=[MR0,MR1,MR2,MR3,MR4,MR5,MR6,MR7]


figure(figsize=(10,10))
for i in range(8):

    xwerte=MR[i]
    ywerte=range(len(MR[i]))
    eywerte=em*np.ones(len(xwerte))
    exwerte=eP*np.ones(len(ywerte))
    name='MR'+str(i)
    

    #title('Lineare Regression der Abstandskalibrierung')
    errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1, label='Messreihe {}'.format(i))
    xlabel('P / hPa')
    ylabel('m')
legend(title='Messwerte vor Korrektur')
savefig('Methode2vorKorr.pdf'.format(name), bbox_inches = 'tight')
show()


#verruecke MR2 so, dass der zweite Messwert dem Mittelwert der anderen Messreihen entspricht. Aendere danach den ersten Messwert auf 995

MR2_new=MR[2]+(np.mean([MR[j][1] for j in range(8)])-MR[2][1])
MR2_new[0]=995
MR[2]=MR2_new



#fuege in MR4 einen zusaetzlichen Messwert ein, der dem mittelwert der anderen Messwerte entspricht.
MR4_new=np.insert(MR[4], 3, np.mean([MR[j][3] for j in range(8)]))
MR[4]=MR4_new


    
figure(figsize=(10,10))
for i in range(8):

    xwerte=MR[i]
    ywerte=range(len(MR[i]))
    eywerte=em*np.ones(len(xwerte))
    exwerte=eP*np.ones(len(ywerte))
    name='MR'+str(i)
    

    #title('Lineare Regression der Abstandskalibrierung')
    errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1, label='Messreihe {}'.format(i))
    xlabel('P / hPa')
    ylabel('m')
legend(title='Messwerte nach Korrektur')
savefig('Methode2nachKorr.pdf'.format(name), bbox_inches = 'tight')
show()


P=np.array([])
eP=np.array([])
m=np.array([[0],[0],[0],[0],[0],[0],[0],[0,1]])
for i in range(8):
    mi=[]
    for j in range(8):
        if len(MR[j])>=(i+1):
            a=MR[j][i]
            mi.append(a)
    m[i]=mi
    P=np.append(P, np.mean(mi))
    eP=np.append(eP,np.std(mi,ddof=1)/np.sqrt(len(mi)))
eP[0]=np.mean(eP)
print(m)
print(P)
print(eP)




#Lineare Regression
xwerte=P
ywerte=range(len(P))
eywerte=em*np.ones(len(xwerte))
exwerte=eP
name='gemittelterDruck'



ai,eai,bi,ebi,chiqi,corri = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)


print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(ai,eai,bi,ebi,chiqi,corri))




figure()
#title('Lineare Regression der Abstandskalibrierung')
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, ai*xwerte+bi, '-', zorder=2)
xlabel('P / hPa')
ylabel('m')
legend(title='Lineare Regression \nSteigung[1/hPa]: ${:.5f}\\pm{:.5f}$ \ny-Achsenabschnitt: ${:.2f}\\pm{:.2f}$ \nDatenpunkte: {}'.format(ai, eai, bi, ebi, len(xwerte)))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
#title('Residuenplot der Abstandskalibrierung')
errorbar(x=xwerte, y=ywerte-(ai*xwerte+bi), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, 0.*xwerte, zorder=2) # Linie bei Null 
xlabel('P / hPa-')
ylabel('m - Fitgerade')
legend(title='Residuenplot \n $X^2/n_{{df}}$ = {:.2f}'.format(chiqi/(len(xwerte)-2)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()



print('\n\n\ndamit ist delta_n/delta_p={} +- {}(stat) +-{}(sys), sigma_Umgebung={}'.format(-ai*lambdag/(2*L), (eai*lambdag/(2*L)), -ai*elambdag/(2*L), (-ai*lambdag/(2*L)-2.655*10**(-7))/(-ai*elambdag/(2*L)+eai*lambdag/(2*L))))

'''
#Lineare Regression umgedreht

xwerte=np.arange(len(P))
ywerte=P
eywerte=eP
exwerte=em*np.ones(len(xwerte))
name='gemittelterDruckumgedreht'



ai,eai,bi,ebi,chiqi,corri = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)


print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(ai,eai,bi,ebi,chiqi,corri))
print('damit waere delta_n/delta_p={}'.format(1/(ai*lambdag/(2*0.01))))



figure()
#title('Lineare Regression der Abstandskalibrierung')
errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, ai*xwerte+bi, '-', zorder=2)
ylabel('P / hPa')
xlabel('m')
legend(title='Lineare Regression \nSteigung[hPa]: ${:.5f}\\pm{:.5f}$ \ny-Achsenabschnitt[hPa]: ${:.2f}\\pm{:.2f}$ \nDatenpunkte: {}'.format(ai, eai, bi, ebi, len(xwerte)))
savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
show()


figure()
#title('Residuenplot der Abstandskalibrierung')
errorbar(x=xwerte, y=ywerte-(ai*xwerte+bi), yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
plot(xwerte, 0.*xwerte, zorder=2) # Linie bei Null 
ylabel('(P -fitgerade) / hPa-')
xlabel('m')
legend(title='Residuenplot \n $X^2/n$ = {:.2f}'.format(chiqi/(len(xwerte)-2)))
savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')

show()


print('damit waere delta_n/delta_p={} +- {}'.format(lambdag/(2*L*ai), (eai*lambdag/(2*L*ai**2))))
'''



















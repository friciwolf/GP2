#! /usr/bin/env python


from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *
import scipy.optimize



lambdag=532e-9
elambdag=1e-9

L=0.01   #in m

em=0.1
eP=2





#----------------Rohdaten-------------------------------------------------------
def Rohdaten():

    MR0=np.array([992,855,779,680,582,490,387,303])
    MR1=np.array([994,874,762,677,588,469,381,290])
    MR2=np.array([994,888,796,709,596,522,433,310])
    MR3=np.array([994,903,811,704,608,508,414,327,217])
    MR4=np.array([994,910,816,724,620,532,435,317])
    MR5=np.array([994,907,811,726,627,523,430,325,218])
    MR6=np.array([994,885,798,704,598,502,386,323])
    
    MR=[MR0,MR1,MR2,MR3,MR4,MR5,MR6]
    for i in range(8):
        print("{}&{}&{}&{}&{}&{}&{}&{}\\".format(i,MR0[i],MR1[i],MR2[i],MR3[i],MR4[i],MR5[i],MR6[i]))
    
    
    a =np.array([])
    ea=np.array([])
    b=np.array([])
    eb=np.array([])
    chiq=np.array([])
        
    
    for i in range(len(MR)):
    
        ywerte=MR[i]
        xwerte=np.array(range(len(MR[i])))
        eywerte=eP*np.ones(len(ywerte))
        exwerte=em*np.ones(len(xwerte))
        name='MR'+str(i)
        
        
        ai,eai,bi,ebi,chiqi,corri = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
        
        print('\n\n\n\nMessreihe {}'.format(i))
        print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(ai,eai,bi,ebi,chiqi,corri))
        print('damit waere delta_n/delta_p={} 1/hPa'.format(lambdag/(2*0.01*(-ai))))
        a=np.append(a, ai)
        ea=np.append(ea,eai)
        b=np.append(b, bi)
        eb=np.append(eb,ebi)
        chiq=np.append(chiq,chiqi)
        
        
        figure(figsize=(6,4))
        errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
        plot(xwerte, ai*xwerte+bi, '-', zorder=2)
        ylabel('P / hPa')
        xlabel('m')
        legend(title='Lineare Regression \nSteigung[hPa]: ${:.1f}\\pm{:.1f}$ \ny-Achsenabschnitt [hPa]: ${:.0f}\\pm{:.0f}$ \nDatenpunkte: {}'.format(ai, eai, bi, ebi, len(xwerte)))
        if (i==0) or (i==1):
            savefig('{}_LinReg_Druck.pdf'.format(name), bbox_inches = 'tight')
        show()
        
        
        figure(figsize=(6,2))
        errorbar(x=xwerte, y=ywerte-(ai*xwerte+bi), yerr=np.sqrt(eywerte**2+(exwerte*ai)**2), linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
        plot(xwerte, 0.*xwerte, zorder=2) # Linie bei Null 
        xlabel('m')
        ylabel('P - P(Fitgerade) [hPa]')
        legend(title='Residuenplot \n $X^2/n_{{df}}$ = {:.2f}'.format(chiqi/(len(xwerte)-2)))
        if (i==0) or (i==1):
            savefig('{}_Residuen_Druck.pdf'.format(name), bbox_inches = 'tight')
        
        show()
        

    
    NP=lambdag/(2*L*(-1)*a) # NP = Delta N / Delta P 
    eNP_stat=lambdag/(2*L*a**2)*ea
    eNP_sys=elambdag/(2*L*(-1)*a)


    for i in range(len(NP)):
        print('Messreihe {}:  NP={:.3f}e-7  +-  {:.3f}e-7(stat)  +- {:.3f}e-7 (sys)'.format(i, NP[i]*10**7, eNP_stat[i]*10**7, eNP_sys[i]*10**7))

    for i in range(len(NP)):
        print('{}&{:.2f}&${:.1f}\\pm{:.1f}$&{:.3f}&{:.3f}&{:.3f}\\\\'.format(i, chiq[i]/(len(MR[i])-2), a[i]*(-1), ea[i], NP[i]*10**7, eNP_stat[i]*10**7, eNP_sys[i]*10**7))
        
    figure()
    errorbar(x=range(7), y=NP,yerr=eNP_stat,linestyle='none', marker='o')
    ylabel('$\\Delta n / \\Delta P$ [1/hPa]')
    xlabel('MR')
    ticklabel_format(useMathText=True)
    savefig('Methode1_Ergebnisse.pdf'.format(name), bbox_inches = 'tight')
    show()


    NP_mean, eNP_stat_mean = analyse.gewichtetes_mittel(NP, eNP_stat)
    eNP_sys_mean = max(eNP_sys)
    print('Ergebnis nach gewichtetes Mittel: NP = {:.3f}e-7  +- {:.3f}e-7(stat) +-{:.3f}e-7(sys), SigmaUmgebung={:.1f}'.format(NP_mean*10**7, eNP_stat_mean*10**7, eNP_sys_mean*10**7, (NP_mean*10**7-2.655)/((eNP_stat_mean+eNP_sys_mean)*10**7)))

Rohdaten()






def Methode2():
    MR0=np.array([992,855,779,680,582,490,387,303])
    MR1=np.array([994,874,762,677,588,469,381,290])
    MR2=np.array([994,888,796,709,596,522,433,310])
    MR3=np.array([994,903,811,704,608,508,414,327,217])
    MR4=np.array([994,910,816,724,620,532,435,317])
    MR5=np.array([994,907,811,726,627,523,430,325,218])
    MR6=np.array([994,885,798,704,598,502,386,323])
    
    MR=[MR0,MR1,MR2,MR3,MR4,MR5,MR6]
    
    
    figure(figsize=(8,8))
    
    for i in range(len(MR)):
    
        ywerte=MR[i]
        xwerte=np.array(range(len(MR[i])))
        eywerte=eP*np.ones(len(ywerte))
        exwerte=em*np.ones(len(xwerte))
        name='MR'+str(i)
        
    
        #title('Lineare Regression der Abstandskalibrierung')
        errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1, label='Messreihe {}'.format(i))
        ylabel('P / hPa')
        xlabel('m')
    legend(title='Messwerte Rohdaten')
    #savefig('Methode2vorKorr.pdf'.format(name), bbox_inches = 'tight')
    show()
    
    
    
    
    P=np.array([])
    ePliste=np.array([])
    #m=np.array([[0],[0],[0],[0],[0],[0],[0],[0,1]])
    for i in range(8):
        mi=[]
        for j in range(len(MR)):
            if len(MR[j])>=(i+1):
                a=MR[j][i]
                mi.append(a)
        #m[i]=mi
        P=np.append(P, np.mean(mi))
        ePliste=np.append(ePliste,np.std(mi,ddof=1)/np.sqrt(len(mi)))
    ePliste[0]=np.mean(ePliste[1:])
    #print(m)
    print(P)
    print(ePliste)
    
    
    
    
    #Lineare Regression
    ywerte=P
    xwerte=np.array(range(len(P)))
    exwerte=em*np.ones(len(xwerte))
    eywerte=ePliste
    name='gemittelterDruck'
    
    
    ai,eai,bi,ebi,chiqi,corri = analyse.lineare_regression_xy(xwerte,ywerte,exwerte,eywerte)
    
    
    print('a={:.4e}+-{:.4e}, b={:.4e}+-{:.4e}, chi2={:.4e}, corr={:.4e}'.format(ai,eai,bi,ebi,chiqi,corri))
    
    
    
    
    figure()
    errorbar(x=xwerte, y=ywerte, yerr=eywerte, xerr=exwerte, linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
    plot(xwerte, ai*xwerte+bi, '-', zorder=2)
    ylabel('P / hPa')
    xlabel('m')
    legend(title='Lineare Regression \nSteigung[hPa]: ${:.5f}\\pm{:.5f}$ \ny-Achsenabschnitt[hPa]: ${:.2f}\\pm{:.2f}$ \nDatenpunkte: {}'.format(ai, eai, bi, ebi, len(xwerte)))
    #savefig('{}_LinReg.pdf'.format(name), bbox_inches = 'tight')
    show()
    
    
    figure()
    errorbar(x=xwerte, y=ywerte-(ai*xwerte+bi), yerr=np.sqrt(eywerte**2+(exwerte*ai)**2), linestyle='none', marker='o', markersize=4, elinewidth=1, zorder=1)
    plot(xwerte, 0.*xwerte, zorder=2) # Linie bei Null 
    xlabel('m')
    ylabel('P - P(Fitgerade) [hPa]')
    legend(title='Residuenplot \n $X^2/n_{{df}}$ = {:.2f}'.format(chiqi/(len(xwerte)-2)))
    #savefig('{}_Residuen.pdf'.format(name), bbox_inches = 'tight')
    
    show()
    
    
    NP=lambdag/(2*L*(-1)*ai) # NP = Delta N / Delta P 
    eNP_stat=lambdag/(2*L*(-1)*a**2)*eai
    eNP_sys=elambdag/(2*L*(-1)*ai)
    
    print('gemittelte Drücke:  NP={:.3f}e-7  +-  {:.3f}e-7(stat)  +- {:.3f}e-7 (sys)'.format(NP*10**7, eNP_stat*10**7, eNP_sys*10**7))

#Methode2()




















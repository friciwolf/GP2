#! /usr/bin/env python
"""
Created on Wed Aug 13 11:19:26 2014

@author: henning
"""
from __future__ import print_function

from praktikum import cassy1
from praktikum import analyse
import numpy as np
from pylab import *

def test_datenlesen():

    data = cassy1.lese_lab_datei('lab/Thermo_Rauschmessung.lab')
    # CASSY-Datei hat Zeiten in der 0. Spalte, Druckwerte in der 2. Spalte
    t = data[:,0]
    p = data[:,2]

    figure()
    subplot(2,1,1)
    title('Rohdaten')
    plot(t,p,'.')
    xlabel('t / s')
    ylabel('p')
    ylim(1000.,1020.)
    grid()

    subplot(2,1,2)
    title('Histogramm der Druckwerte')
    hist(p,bins=1000,range=(1000.,1020.),color='green')
    xlabel('p / mbar')
    xlim(1000.,1020.)

    p_mean = np.mean(p)
    p_stdabw = np.std(p,ddof=1)
    p_err = p_stdabw/np.sqrt(len(p))

    print('p_mean = %f, p_stdabw = %f, p_err = %f' % (p_mean,p_stdabw,p_err))

    show()

def test_lineare_regression():

    sigma = 1.0
    xmin = -20.
    xmax =  20.

    # wuerfele Daten
    x=np.arange(xmin,xmax)
    y=np.random.normal(3.+0.5*x,sigma)
    ey=0.*x+sigma

    # Aufruf der linearen Regression
    a,ea,b,eb,chiq,corr = \
        analyse.lineare_regression(x,y,ey)

    print('a=%f+-%f, b=%f+-%f, chi2=%f, corr=%f' % (a,ea,b,eb,chiq,corr))

    figure()
    subplot(2,1,1)
    title('Lineare Regression')
    errorbar(x,y,yerr=ey,fmt='o',color='blue')
    plot(x,a*x+b,'-')
    xlim(xmin-1.,xmax+1.)
    xlabel('x')
    ylabel('y')
    grid()

    subplot(2,1,2)
    title('Residuenplot')
    errorbar(x,y-(a*x+b),yerr=ey,fmt='o',color='blue')
    plot(x,0.*x) # Linie bei Null
    xlim(xmin-1.,xmax+1.)
    ylim(-5,5)
    xlabel('x')
    ylabel('y-(ax+b)')

    show()



def test_lineare_regression_mit_korrelation():

    sigma = 1.0
    xmin = 100.
    xmax = xmin + 20.
    x=np.arange(xmin,xmax)
    y=np.random.normal(3.+2.*x,sigma)
    ey=0.*x+sigma

    # Um die Korrelation zwischen a und b zu minimieren,
    # transformieren wir x geeignet
    x0 = 0.5*(xmin+xmax)
    # x0 = 0
    x = x - x0

    # Aufruf der linearen Regression
    a,ea,b,eb,chiq,corr = \
        analyse.lineare_regression(x,y,ey)

    print('a=%f+-%f, b=%f+-%f (x0=%f), chi2=%f, corr=%f' % \
        (a,ea,b,eb,x0,chiq,corr))

    # Ruecktransformation
    x = x + x0
    b = b - a*x0

    figure()
    subplot(2,1,1)
    title('Lineare Regression')
    errorbar(x,y,yerr=ey,fmt='o',color='blue')
    plot(x,a*x+b,'-')
    xlim(xmin-1.,xmax+1.)
    xlabel('x')
    ylabel('y')

    subplot(2,1,2)
    title('Residuenplot')
    errorbar(x,y-(a*x+b),yerr=ey,fmt='o',color='blue')
    plot(x,0.*x)
    xlim(xmin-1.,xmax+1.)
    ylim(-5,5)
    xlabel('x')
    ylabel('y-(ax+b)')

    show()



def test_lineare_regression_xy():

    sigmax = 0.5
    sigmay = 1.0
    xmin = -20.
    xmax =  20.

    # wuerfele Daten
    x=np.arange(xmin,xmax)
    xdata = np.random.normal(x,sigmax)
    ydata=np.random.normal(3.+0.5*x,sigmay)
    ex=0.*x+sigmax
    ey=0.*x+sigmay

    # Aufruf der linearen Regression
    a,ea,b,eb,chiq,corr = \
        analyse.lineare_regression_xy(xdata,ydata,ex,ey)

    print('Ergebnis: a=%f+-%f, b=%f+-%f, chi2=%f, corr=%f' % (a,ea,b,eb,chiq,corr))

    figure()
    subplot(2,1,1)
    title('Lineare Regression')
    errorbar(xdata,ydata,xerr=ex,yerr=ey,fmt='o',color='blue')
    plot(x,a*x+b,'-')
    xlim(xmin-1.,xmax+1.)
    xlabel('x')
    ylabel('y')
    grid()

    subplot(2,1,2)
    title('Residuenplot')
    errorbar(xdata,ydata-(a*xdata+b),xerr=ex,yerr=ey,fmt='o',color='blue')
    plot(x,0.*x) # Linie bei Null
    xlim(xmin-1.,xmax+1.)
    ylim(-5,5)
    xlabel('x')
    ylabel('y-(ax+b)')

    show()

def test_fourier():

    tmin = 100.
    tmax = 500.
    tstep = 0.2
    freq = 0.123

    t = np.arange(tmin,tmax,tstep)
    y = np.cos(2.*np.pi*freq*t)

    figure()
    subplot(2,1,1)
    title('Daten')
    plot(t,y,'.')
    xlabel('$t$ / s')
    ylabel('amp')
    grid()

    subplot(2,1,2)
    title('Fourierspektrum')
    freq,amp = analyse.fourier(t,y)
    freq_fft,amp_fft = analyse.fourier_fft(t,y)
    plot(freq,amp,'.',color='blue',label="Fourier")
    amp_fft = np.max(amp) / np.max(amp_fft) * amp_fft
    plot(freq_fft,amp_fft,'.',color='red',label="FFT")
    xlabel('$f$ / Hz')
    ylabel('amp')
    grid()
    legend()

    fpeak = analyse.peakfinder_schwerpunkt(freq,amp)
    fpeak_fft = analyse.peakfinder_schwerpunkt(freq_fft,amp_fft)
    axvline(fpeak,color='blue')
    axvline(fpeak_fft,color='red')
    xlim(0.,np.max(freq))
    ylim(0.,max(np.max(amp),np.max(amp_fft)) * 1.1)

    show()

def test_exp_einhuellende():

    tmin = 0.
    tmax = 500.
    tstep = 0.2
    freq = 0.0123
    delta = 0.003
    A = 1.0
    sigma = 0.0002

    t = np.arange(tmin,tmax,tstep)
    y = np.random.normal(A*np.cos(2.*np.pi*freq*t)*np.exp(-delta*t),sigma)
    ey = 0.*t+sigma

    A0,sigmaA0,deltaF,sigmaDelta = analyse.exp_einhuellende(t,y,ey)
    huelle = A0*np.exp(-deltaF*t)

    print('A0=%f+-%f, delta=%f+-%f' % (A0,sigmaA0,deltaF,sigmaDelta))

    figure()
    title('Exponentielle Einhuellende')
    plot(t,y,'.')
    plot(t,huelle,'.',color='red')
    plot(t,-huelle,'.',color='red')
    xlabel('$t$ / s')
    ylabel('amp')
    grid()

    show()

def test_gew_mittel():

    y  = np.array([3.0,3.2,3.4])
    ey = np.array([0.5,0.1,0.2])

    xm,sx = analyse.gewichtetes_mittel(y,ey)
    print('Mittelwert aus %d Werten: %f +- %f' % (len(y),xm,sx))

def test_mittel_stdabw():

    x = np.array([12.4, 12.5, 12.6, 12.4, 12.5, 12.8, 12.9, 12.5, 12.3, 12.4])
    xm, sx = analyse.mittelwert_stdabw(x)
    print('Mittelwert: %g, Stdabw.: %g' % (xm, sx))


if __name__ == '__main__':

    print('Beispiele eingelesen...')

    test_datenlesen()
    test_lineare_regression()
    test_lineare_regression_mit_korrelation()
    test_lineare_regression_xy
    test_fourier()
    test_exp_einhuellende()
    test_gew_mittel()
    test_mittel_stdabw()

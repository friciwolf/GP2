#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from builtins import range

from praktikum import analyse
from praktikum import cassy
import numpy as np
import os
from pylab import *

inputfile = 'labx/kondensator.labx'
#inputfile = 'txt/kondensator.txt'
data = cassy.CassyDaten(inputfile)
data.info()

# Bereich für logarithmischen Fit (in ms)
tmin = 0.101
tmax = 4.001

# Beginn der "Rauschmessung" für die Offset-Korrektur (in ms)
toffset = 8.0

figure(1, figsize=(25,10))

N = data.anzahl_messungen()
for m in range(1, N+1):

    t = data.messung(m).datenreihe('t').werte
    data.messung(m).datenreihe('t').info()
    # Im labx-Format scheinen die Zeitwerte in s statt ms gespeichert zu sein.
    if os.path.splitext(inputfile)[1] == '.labx':
        t *= 1000.0 # s -> ms
    UR = data.messung(m).datenreihe('U_A1').werte
    UC = data.messung(m).datenreihe('U_B1').werte

    subplot(3,N,m)
    # Grafische Darstellung der Rohdaten
    plot(t, UR, color='red', label='$U_R$')
    plot(t, UC, color='green', label='$U_C$')
    xlabel('t / ms')
    ylabel('$U$ / V')
    ylim(0.,12.)
    legend(loc='best')

    subplot(3,N,m+N)
    UR0 = UR[0]

    # Offsetkorrektur
    _, Uend = analyse.untermenge_daten(t, UR, toffset, t[-1])
    Uoffset = Uend.mean()
    print('Uoffset = %g V' % Uoffset)
    logUR = np.log((UR-Uoffset)/UR0)

    # Messbereich -> Digitalisierungsfehler (Cassy-ADC hat 12 bits => 4096 mögliche Werte)
    sigmaU = 20.0 / 4096. / np.sqrt(12.)
    sigmaLogUR = sigmaU / UR

    # Extrahiere Daten für Fit
    t_fit, logUR_fit = analyse.untermenge_daten(t, logUR, tmin, tmax)
    _, sigmaLogUR_fit = analyse.untermenge_daten(t, sigmaLogUR, tmin, tmax)

    errorbar(t_fit, logUR_fit, yerr=sigmaLogUR_fit, fmt='.')
    xlabel('t / ms')
    ylabel('$\log\,U/U_0$')

    # Lineare Regression zur Bestimmung der Zeitkonstanten
    a,ea,b,eb,chiq,corr = analyse.lineare_regression(t_fit, logUR_fit, sigmaLogUR_fit)
    tau = 1./a
    sigma_tau = tau * ea/a
    print('tau = (%g +- %g) ms   b = (%g +- %g)   chi2/dof = %g / %g' % (tau, sigma_tau, b, eb, chiq, len(t_fit)-2))
    plot(t_fit, a*t_fit+b, color='red')

    subplot(3,N,m+2*N)
    # Residuenplot
    resUR = logUR_fit - (a*t_fit+b)
    eresUR = sigmaLogUR_fit
    errorbar(t_fit, resUR, yerr=eresUR, fmt='.')
    xlabel('t / ms')
    ylabel(r'$\log\,U/U_0 - (t/\tau + b)$')

show()

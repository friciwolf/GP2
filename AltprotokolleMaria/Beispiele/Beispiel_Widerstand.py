#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from builtins import range

from praktikum import analyse
from praktikum import cassy
import numpy as np
from pylab import *

inputfile = 'labx/widerstand.labx'
#inputfile = 'txt/widerstand.txt'
data = cassy.CassyDaten(inputfile)

# Es gibt nur eine einzige Messung in der Datei.
U = data.messung(1).datenreihe('U_B1').werte
I = data.messung(1).datenreihe('I_A1').werte

# Messbereich -> Digitalisierungsfehler (Cassy-ADC hat 12 bits => 4096 mögliche Werte)
sigmaU = 20.0 / 4096. / np.sqrt(12.) * np.ones(len(U))
sigmaI = 0.2 / 4096. / np.sqrt(12.) * np.ones(len(I))

figure()

# Grafische Darstellung der Rohdaten
subplot(2,1,1)
errorbar(I, U, xerr=sigmaI, yerr=sigmaU, color='red', fmt='.', marker='o', markeredgecolor='red')
xlabel('$I$ / A')
ylabel('$U$ / V')

# Lineare Regression
R,eR,b,eb,chiq,corr = analyse.lineare_regression_xy(I, U, sigmaI, sigmaU)
print('R = (%g +- %g) Ohm,   b = (%g +- %g) V,  chi2/dof = %g / %g  corr = %g' % (R, eR, b, eb, chiq, len(I)-2, corr))
plot(I, R*I+b, color='green')

# Residuen
subplot(2,1,2)
# Für den Residuenplot werden die Beiträge von Ordinate und Abszisse (gewichtet mit der Steigung) quadratisch addiert.
sigmaRes = np.sqrt((R*sigmaI)**2 + sigmaU**2)
errorbar(I, U-(R*I+b), yerr=sigmaRes, color='red', fmt='.', marker='o', markeredgecolor='red')
xlabel('$I$ / A')
ylabel('$(U-(RI+b))$ / V')

show()

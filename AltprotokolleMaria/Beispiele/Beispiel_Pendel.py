#! /usr/bin/env python

from __future__ import print_function
from praktikum import cassy
from praktikum import analyse
import numpy as np
from pylab import *

data = cassy.CassyDaten('lab/Pendel.lab')
timeValues = data.messung(1).datenreihe('t').werte
voltage = data.messung(1).datenreihe('U_A1').werte
voltageError = 0. * voltage + 0.01
offset = analyse.gewichtetes_mittel(voltage, voltageError)[0]
voltage = voltage - offset

figure(1)
title('Pendel')

subplot(2,1,1)
plot(timeValues, voltage)
grid()
xlabel('Zeit / s')
ylabel('Spannung / V')
einhuellende = analyse.exp_einhuellende(timeValues, voltage, voltageError)
plot(timeValues, +einhuellende[0] * exp(-einhuellende[2] * timeValues))
plot(timeValues, -einhuellende[0] * exp(-einhuellende[2] * timeValues))

subplot(2,1,2)
fourier = analyse.fourier_fft(timeValues, voltage)
frequency = fourier[0]
amplitude = fourier[1]
plot(frequency, amplitude)
grid()
xlabel('Frequenz / Hz')
ylabel('Amplitude')

maximumIndex = amplitude.argmax();
xlim(frequency[max(0, maximumIndex-10)], frequency[min(maximumIndex+10, len(frequency))])
peak = analyse.peakfinder_schwerpunkt(frequency, amplitude)
axvline(peak)

L = 0.667
g = ((2 * np.pi * peak)**2) * L

print('g = %f m/s^2' % g)

show()

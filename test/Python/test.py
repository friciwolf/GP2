import numpy as np
import praktikum_addons.bib as bib
import matplotlib.pyplot as plt

x,y = bib.c_open("../WegaufKal3.lab", ["R_B1","s"])
ex = np.ones(len(x))*0.005
ey = np.ones(len(y))*0.1/np.sqrt(12)
ax1, ax2 = bib.pltmitres(x,y, ex, ey,yl="s",xl="R", yeinheit = "cm", xeinheit="$k\Omega$", ratios=[5,1])
ax1.set_ylim(top=120)
plt.show()
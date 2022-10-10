"""
This script produces a Figure that shows the atmospheric
parameters evolution of the planets LP8909 b and LP8909 c,
 using VPLANET's STELLAR and ATMESC modules.

Laura N. R. do Amaral, Universidad Nacional Autónoma de México, 2022
Date:  Oct 6th 2022
"""
import os
import pathlib
import subprocess
import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

import vplanet

try:
    import vplot as vpl
except:
    print("Cannot import vplot. Please install vplot.")

path = pathlib.Path(__file__).parents[0].absolute()
sys.path.insert(1, str(path.parents[0]))
from get_args import get_args

# Defining the directory where the data is
planetb = []
planetc = []
stellar = []

for i in range(1,19):
          planetb.append('./LP8909_'+f'{i}'+'/LP8909.b.forward')
          planetc.append('./LP8909_'+f'{i}'+'/LP8909.c.forward')
  #        stellar.append('./LP8909_'+f'{i}'+'/LP8909.LP8909.forward')


# Loading the data
btime = []
bage = []
bSurfWaterMass = []
bOxygenMantleMass = []
bPlanetRadius = []
bEnvelopeMass = []
bDEnvMassDt = []
bOxygenMass = []
bFXUV = []

ctime = []
cage = []
cSurfWaterMass = []
cOxygenMantleMass = []
cPlanetRadius = []
cEnvelopeMass = []
cDEnvMassDt = []
cOxygenMass = []
cFXUV = []


for i in range(0, 18):
    btime.append(np.genfromtxt(planetb[i], usecols=(0), unpack=True))
    bage.append(np.genfromtxt(planetb[i], usecols=(1), unpack=True))
    bSurfWaterMass.append(np.genfromtxt(planetb[i], usecols=(2), unpack=True))
    bOxygenMantleMass.append(np.genfromtxt(planetb[i], usecols=(4), unpack=True))
    bPlanetRadius.append(np.genfromtxt(planetb[i], usecols=(5), unpack=True))
    bEnvelopeMass.append(np.genfromtxt(planetb[i], usecols=(6), unpack=True))
#    bDEnvMassDt.append(np.genfromtxt(planetb[i], usecols=(7), unpack=True))  
    bOxygenMass.append(np.genfromtxt(planetb[i], usecols=(8), unpack=True))
    bFXUV.append(np.genfromtxt(planetb[i], usecols=(9), unpack=True))                    
    
    ctime.append(np.genfromtxt(planetc[i], usecols=(0), unpack=True))
    cage.append(np.genfromtxt(planetc[i], usecols=(1), unpack=True))
    cSurfWaterMass.append(np.genfromtxt(planetc[i], usecols=(2), unpack=True))
    cOxygenMantleMass.append(np.genfromtxt(planetc[i], usecols=(4), unpack=True))
    cPlanetRadius.append(np.genfromtxt(planetc[i], usecols=(5), unpack=True))
    cEnvelopeMass.append(np.genfromtxt(planetc[i], usecols=(6), unpack=True))
#    cDEnvMassDt.append(np.genfromtxt(planetc[i], usecols=(7), unpack=True))  
    cOxygenMass.append(np.genfromtxt(planetc[i], usecols=(8), unpack=True))
    cFXUV.append(np.genfromtxt(planetc[i], usecols=(9), unpack=True))           
    
# Plot
fig, axes = plt.subplots(nrows=2, ncols=3, sharex=True, figsize=(7, 5))

time = []

cmap = [
    vpl.colors.dark_blue,
    vpl.colors.red,
    vpl.colors.orange,
    vpl.colors.purple,
    vpl.colors.pale_blue,
]


# alpha value
d = [1,0.5]

# linewidth
b = 1

#linestyle
line = ['-','--',':']

for i in range(0,3):
# dSurfaceWater = 10 TO, O2 = 1
         axes[0, 0].plot(bage[i+6],bSurfWaterMass[i+6], color=cmap[0], alpha=d[0],lw=b, ls = line[i])
         axes[1, 0].plot(bage[i+6],bOxygenMantleMass[i+6], color=cmap[0], alpha=d[0], lw=b, ls = line[i])
         axes[0, 1].plot(bage[i+6],bPlanetRadius[i+6], color=cmap[0], alpha=d[0], lw=b, ls = line[i])
         axes[1, 1].plot(bage[i+6],bEnvelopeMass[i+6], color=cmap[0], alpha=d[0], lw=b, ls = line[i])
         axes[0, 2].plot(bage[i+6],bOxygenMass[i+6], color=cmap[0], alpha=d[0], lw=b, ls = line[i])
         axes[1, 2].plot(bage[i+6],bFXUV[i+6], color=cmap[0], alpha=d[0], lw=b, ls = line[i])

         axes[0, 0].plot(cage[i+6],cSurfWaterMass[i+6], color=cmap[1], alpha=d[0], lw=b, ls = line[i])
         axes[1, 0].plot(cage[i+6],cOxygenMantleMass[i+6], color=cmap[1], alpha=d[0],lw=b, ls = line[i])
         axes[0, 1].plot(cage[i+6],cPlanetRadius[i+6], color=cmap[1], alpha=d[0],lw=b, ls = line[i])
         axes[1, 1].plot(cage[i+6],cEnvelopeMass[i+6], color=cmap[1], alpha=d[0], lw=b, ls = line[i])
         axes[0, 2].plot(cage[i+6],cOxygenMass[i+6], color=cmap[1], alpha=d[0], lw=b, ls = line[i])
         axes[1, 2].plot(cage[i+6],cFXUV[i+6], color=cmap[1], alpha=d[0], lw=b, ls = line[i])
# dSurfaceWater = 10 TO, O2 = 0   
         axes[0, 0].plot(bage[i+15],bSurfWaterMass[i+15], color=cmap[0], alpha=d[1],lw=b, ls = line[i])
         axes[1, 0].plot(bage[i+15],bOxygenMantleMass[i+15], color=cmap[0], alpha=d[1], lw=b, ls = line[i])
         axes[0, 1].plot(bage[i+15],bPlanetRadius[i+15], color=cmap[0], alpha=d[1], lw=b, ls = line[i])
         axes[1, 1].plot(bage[i+15],bEnvelopeMass[i+15], color=cmap[0], alpha=d[1], lw=b, ls = line[i])
         axes[0, 2].plot(bage[i+15],bOxygenMass[i+15], color=cmap[0], alpha=d[1], lw=b, ls = line[i])
         axes[1, 2].plot(bage[i+15],bFXUV[i+15], color=cmap[0], alpha=d[1], lw=b, ls = line[i])

         axes[0, 0].plot(cage[i+15],cSurfWaterMass[i+15], color=cmap[1], alpha=d[1], lw=b, ls = line[i])
         axes[1, 0].plot(cage[i+15],cOxygenMantleMass[i+15], color=cmap[1], alpha=d[1],lw=b, ls = line[i])
         axes[0, 1].plot(cage[i+15],cPlanetRadius[i+15], color=cmap[1], alpha=d[1],lw=b, ls = line[i])
         axes[1, 1].plot(cage[i+15],cEnvelopeMass[i+15], color=cmap[1], alpha=d[1], lw=b, ls = line[i])
         axes[0, 2].plot(cage[i+15],cOxygenMass[i+15], color=cmap[1], alpha=d[1], lw=b, ls = line[i])
         axes[1, 2].plot(cage[i+15],cFXUV[i+15], color=cmap[1], alpha=d[1], lw=b, ls = line[i])


axes[0, 1].set_title("Surface Water 10 TO", loc="center")

label = [r'Surface Water (TO)', r'O$_{2}$ in the Mantle (bar)',r'Planetary Radius (R$_{\oplus}$)', 
              r'Envelope Mass (M$_{\oplus}$)', r'O$_{2}$ in the upper atmosphere (bar)', r'XUV Flux (W/m$^{2}$)']

axes[0, 0].set_ylabel(label[0])
axes[1, 0].set_ylabel(label[1])
axes[0, 1].set_ylabel(label[2])
axes[1, 1].set_ylabel(label[3])
axes[0, 2].set_ylabel(label[4])
axes[1, 2].set_ylabel(label[5])
for i in range(0,3):
        axes[1, i].set_xlabel('System Age (years)')


# Legend
legend_elements = [
    Line2D([0], [0], ls="-", color="black", alpha=1, lw = 2, label=r"O$_{2}$ sink"),
    Line2D([0], [0], ls="-", color="black", alpha=0.5, lw = 2, label=r"No O$_{2}$ sink"),
    Line2D([0], [0], ls="-", color=cmap[0], alpha=1, lw = 2, label=r"LP 8909 b"),
    Line2D([0], [0], ls="-", color=cmap[1], alpha=1, lw = 2, label=r"LP 8909 c"),
    Line2D([0], [0], ls="-", color="black", alpha=1, lw = 1, label=r"Initial Envelope Mass 0 M$_{\oplus}$ "),
    Line2D([0], [0], ls="--", color="black", alpha=1, lw = 1, label=r"Initial Envelope Mass 0.01 M$_{\oplus}$ "),
    Line2D([0], [0], ls=":", color="black", alpha=1, lw = 1, label=r"Initial Envelope Mass 0.1 M$_{\oplus}$ "),
]


axes[1, 2].legend(
    handles=legend_elements,
    bbox_to_anchor=(0.63,0.77, 0, 0),
    loc="center",
    ncol=1,
    fontsize=5,
)

# Format all axes
for ax in axes.flatten():

    # Format x axis
    #ax.set_xlim(bage[1], bage[-1])
    ax.set_xscale("log")
    # Set rasterization
    ax.set_rasterization_zorder(0)

# Save figure
if sys.argv[1] == "pdf":
    fig.savefig("LP8909_atmesc_10TO.pdf", bbox_inches="tight", dpi=300)
if sys.argv[1] == "png":
    fig.savefig("LP8909_atmesc_10TO.png", bbox_inches="tight", dpi=300)

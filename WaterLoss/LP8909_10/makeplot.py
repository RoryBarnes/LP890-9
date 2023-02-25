"""
This script produces a figure that show the time evolution of planetary and stellar parameters for
LP890-9 system, using VPLANET's ATMESC, and STELLAR modules.

@autor: Laura N.  R. do Amaral, Universidad Nacional Autónoma de México, 2022
@email: laura.nevesdoamaral@gmail.com
Date: Sep. 15st, 2022
"""

import os
import pathlib
import subprocess
import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import vplot as vpl
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.lines import Line2D

import vplanet

path = pathlib.Path(__file__).parents[0].absolute()
sys.path.insert(1, str(path.parents[0]))
from get_args import get_args

# Check correct number of arguments
if len(sys.argv) != 2:
     print("ERROR: Incorrect number of arguments.")
     print("Usage: " + sys.argv[0] + " <pdf | png>")
     exit(1)
if sys.argv[1] != "pdf" and sys.argv[1] != "png":
     print("ERROR: Unknown file format: " + sys.argv[1])
     print("Options are: pdf, png")
     exit(1)
plt.rcParams.update({"font.size": 16, "legend.fontsize": 16})

# Run vplanet
output = vplanet.run(path / "vpl.in", units=False)

Time = output.LP8909.Age

HZR = output.LP8909.HZLimRunaway
HZM = output.LP8909.HZLimMaxGreenhouse
HZVenus = output.LP8909.HZLimRecVenus
HZMars = output.LP8909.HZLimEarlyMars

planets = output.bodies[1:]

SurfWaterMass = np.array([planet.SurfWaterMass for planet in planets])
OxygenMantleMass = np.array([planet.OxygenMantleMass for planet in planets])
EnvelopeMass = np.array([planet.EnvelopeMass for planet in planets])
PlanetRadius = np.array([planet.PlanetRadius for planet in planets])
DEnvMassDt = np.array([planet.DEnvMassDt for planet in planets])
OxygenMass = np.array([planet.OxygenMass for planet in planets]) 
FXUV = np.array([planet.FXUV for planet in planets]) 

# Plot!
fig, axes = plt.subplots(nrows=2, ncols=4, sharex="col", figsize=(12, 5))

style = ["-", "--", "-."]
color = [vpl.colors.red, vpl.colors.dark_blue]

a = 1

for i in range(0, 2):
    axes[0, 0].plot(
        Time,
        SurfWaterMass[i],
        color=color[i],
        linewidth=a,
        linestyle=style[i],
        alpha=0.5,
    )
    axes[0, 1].plot(
        Time,
        EnvelopeMass[i],
        color=color[i],
        linewidth=a,
        linestyle=style[i],
        alpha=0.5,
    )
    axes[0, 2].plot(
        Time,
        PlanetRadius[i],
        color=color[i],
        linewidth=a,
        linestyle=style[i],
        alpha=0.5,
    )
    axes[1, 0].plot(
        Time,
        OxygenMass[i],
        color=color[i],
        linewidth=a,
        linestyle=style[i],
        alpha=0.5,
    )
    axes[1, 3].plot(
        Time,
        FXUV[i],
        color=color[i],
        linewidth=a,
        linestyle=style[i],
        alpha=0.5,
    )
    axes[0, 3].plot(
        Time,
        OxygenMantleMass[i],
        color=color[i],
        linewidth=a,
        linestyle=style[i],
        alpha=0.5,
    )
    axes[1, 2].plot(
        Time,
        DEnvMassDt[i],
        color=color[i],
        linewidth=a,
        linestyle=style[i],
        alpha=0.5,
    )


# Legend
legend_elements = [
    Line2D(
        [0], [0], ls=style[0], color=color[0], lw=1, label="LP8909-9 b"),
    Line2D([0], [0], ls=style[1], color=color[1], lw=1, label="LP8909-9 c")
]

plt.legend(handles=legend_elements, ncol=1, loc="upper right", fontsize=7)



axes[1, 1].fill_between(
    Time,
    HZR,
    HZM,
    color=vpl.colors.purple,
    alpha=0.5,
)

axes[1, 1].fill_between(
    Time,
    HZVenus,
    HZMars,
    color=vpl.colors.orange,
    alpha=0.5,
)

axes[1, 1].annotate(
    "HZ",
    xy=(0.1, 0.5),
    xycoords="axes fraction",
    horizontalalignment="left",
    verticalalignment="bottom",
    color="w",
)

axes[0, 0].set_ylabel("Surface Water (TO)")
axes[0, 1].set_ylabel(r"Envelope Mass (M$_{\oplus}$)")
axes[0, 2].set_ylabel(r"Planetary Radius (R$_{\oplus}$)")
axes[0, 3].set_ylabel(r"Absorbed O2 by the mantle (bars)")
axes[1, 0].set_ylabel("Oxygen Pressure (bars)")
axes[1, 1].set_ylabel("Semi-Major Axis (AU)")
axes[1, 2].set_ylabel(r"DEnvMassDt (M$_{\oplus}$ Myr$^{-1}$)")
axes[1, 3].set_ylabel(r"XUV flux (W/m$^{2}$)")

for i in range(0, 4):
    axes[0, i].set_xlim(1e6, 50e6)
    axes[1, i].set_xlim(1e6, 50e6)
    axes[0, i].set_xscale("log")
    axes[1, i].set_xscale("log")
    axes[0, i].set_xlabel("  ")
    axes[1, i].set_xlabel("System Age (year)")

axes[0, 1].set_yscale("log")


# LP890-9 b position
axes[1,1].axhline(y= 0.01875, xmin=0.0, xmax=7.0e9, ls=style[0], color=color[0], lw = 0.5) 
# LP890-9 c position
axes[1,1].axhline(y= 0.03984, xmin=0.0, xmax=7.0e9, ls=style[1], color=color[1], lw = 0.5) 

# Annotate best fit
axes[1,1].annotate(
    "LP 890 9 b's orbit",
    xy=(0.5,  0.001),
    xycoords="axes fraction",
    fontsize=8,
    horizontalalignment="right",
    verticalalignment="bottom",
)
axes[1,1].annotate(
    "LP 890 9 c's orbit",
    xy=(0.5,  0.07),
    xycoords="axes fraction",
    fontsize=8,
    horizontalalignment="right",
    verticalalignment="bottom",
)


# Save figure
if sys.argv[1] == "pdf":
    fig.savefig("LP8909_atmesc.pdf", bbox_inches="tight", dpi=300)
if sys.argv[1] == "png":
    fig.savefig("LP8909_atmesc.png", bbox_inches="tight", dpi=300)

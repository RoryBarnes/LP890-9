"""
Adapted from Fig. 22 in Barnes et al. (2020). Original figure by David Fleming.
"""
import vplanet
import vplot
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pathlib
import sys

if len(sys.argv) != 2:
    print("ERROR: Must specify file type")
    print(f"USAGE: $ python {sys.argv[0]} <png | pdf>")
    exit(0)

# Path hack
path = pathlib.Path()

# Typical plot parameters that make for pretty plot
mpl.rcParams["figure.figsize"] = (10, 8)
mpl.rcParams["font.size"] = 16.0

# Run vplanet
output = vplanet.get_output(path, units=False)

# Extract data
time = output.b.Time / 1.0e9
ecc1 = output.b.Eccentricity
ecc2 = output.c.Eccentricity
varpi1 = output.b.LongP
varpi2 = output.c.LongP
a1 = output.b.SemiMajorAxis
a2 = output.c.SemiMajorAxis
i1 = output.b.Inc
i2 = output.c.Inc

# Plot
fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True)
color = "k"

## Upper left: semi-major axes ##
axes[0, 0].plot(time, a1, color="C3", zorder=-1, label="b")
axes[0, 0].plot(time, a2, color="C0", zorder=-1, label="c")

# Format
axes[0, 0].set_xlim(time.min(), time.max())
axes[0, 0].set_ylabel("Semi-major Axis (au)")

## Upper right: eccentricities ##
axes[0, 1].plot(time, ecc1, color="C3", zorder=-1, label="b")
axes[0, 1].plot(time, ecc2, color="C0", zorder=-1, label="c")

# Format
axes[0, 1].set_xlim(time.min(), time.max())
axes[0, 1].set_ylim(0.0)
axes[0, 1].set_ylabel("Eccentricity")
axes[0, 1].legend(loc=0)

## Lower left: inclinations ##
# Format
axes[1, 0].set_xlabel("Time (Gyr)")
axes[1, 0].plot(time, i1, color="C3", zorder=-1)
axes[1, 0].plot(time, i2, color="C0", zorder=-1)
axes[1, 0].set_ylabel(r"Inclination ($^{\circ}$)")

## Lower right: diff between longitude of periapses ##
# varpiDiff = np.fabs(np.fmod(varpi1 - varpi2, 360.0))
varpiDiff = np.abs((varpi1 - varpi2 + 180) % 360 - 180)
axes[1, 1].scatter(time, varpiDiff, color="C3", s=10, zorder=-1)

# Format
axes[1, 1].set_xlim(time.min(), time.max())
axes[1, 1].set_ylim(0, 180)
axes[1, 1].set_xlabel("Time (Gyr)")
axes[1, 1].set_ylabel(r"$\Delta \varpi$ ($^{\circ}$)")

# Final formating
fig.tight_layout()
for ax in axes.flatten():
    # Rasterize
    ax.set_rasterization_zorder(0)

# Save the figure
ext = sys.argv[1]
fig.savefig(path / f"ApseLock.{ext}", bbox_inches="tight", dpi=600)

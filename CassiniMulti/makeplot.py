import vplanet
import vplot
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pathlib
import sys

if len(sys.argv) != 2:
    print("ERROR: Must specify file type")
    print(f"USAGE: python {sys.argv[0]} <png | pdf>")
    exit(0)

# Path hack
path = pathlib.Path()

# Run vplanet
out = vplanet.get_output(path, units=False)
time = out.TGstar.Time / 1e3

fig = plt.figure(figsize=(6.5, 8))
plt.subplot(3, 2, 1)
plt.plot(time, out.TGb.Obliquity, color="k")
plt.plot(time, out.TGc.Obliquity, color=vplot.colors.red)
# plt.yscale("log")
plt.ylabel(r"Obliquity ($^\circ$)")

plt.subplot(3, 2, 2)
plt.plot(time, out.TGb.Inc, color="k")
plt.plot(time, out.TGc.Inc, color=vplot.colors.red)
plt.ylabel(r"Inclination ($^\circ$)")

plt.subplot(3, 2, 3)
plt.plot(time, out.TGb.RotPer, color="k")
plt.plot(time, out.TGc.RotPer, color=vplot.colors.red)
plt.ylabel("Rotation Period (days)")

plt.subplot(3, 2, 4)
plt.plot(time, out.TGb.DynEllip, color="k", label="b")
plt.plot(time, out.TGc.DynEllip, color=vplot.colors.red, label="c")
plt.ylabel("Dynamical Ellipticity")
plt.legend(loc="upper right", fontsize=12, ncol=1)

plt.subplot(3, 2, 5)
plt.plot(time, out.TGb.CassiniOne, color="k")
plt.plot(time, out.TGc.CassiniOne, color=vplot.colors.red)
plt.xlabel("Time (kyr)")
plt.ylabel("$\sin{\Psi}$")

plt.subplot(3, 2, 6)
plt.plot(time, out.TGb.CassiniTwo, color="k")
plt.plot(time, out.TGc.CassiniTwo, color=vplot.colors.red)
plt.xlabel("Time (kyr)")
plt.ylabel("$\cos{\Psi}$")

# Save the figure
ext = sys.argv[1]
fig.tight_layout()
fig.savefig(path / f"CassiniMulti.{ext}")

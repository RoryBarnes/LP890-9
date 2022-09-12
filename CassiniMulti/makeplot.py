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

# Path hacks
path = pathlib.Path(__file__).parents[0].absolute()
sys.path.insert(1, str(path.parents[0]))

# Run vplanet
out = vplanet.run(path / "vpl.in", units=False)
time = out.star.Time / 1e3

fig = plt.figure(figsize=(6.5, 8))
plt.subplot(3, 2, 1)
plt.plot(time, out.b.Obliquity, color="k")
plt.plot(time, out.c.Obliquity, color=vplot.colors.red)
plt.yscale("log")
plt.ylabel(r"Obliquity ($^\circ$)")

plt.subplot(3, 2, 2)
plt.plot(time, out.b.Inc, color="k")
plt.plot(time, out.c.Inc, color=vplot.colors.red)
plt.ylabel(r"Inclination ($^\circ$)")

plt.subplot(3, 2, 3)
plt.plot(time, out.b.RotPer, color="k")
plt.plot(time, out.c.RotPer, color=vplot.colors.red)
plt.ylabel("Rotation Period (days)")

plt.subplot(3, 2, 4)
plt.plot(time, out.b.DynEllip, color="k", label="b")
plt.plot(time, out.c.DynEllip, color=vplot.colors.red, label="c")
plt.ylabel("Dynamical Ellipticity")
plt.legend(loc="upper right", fontsize=12, ncol=1)

plt.subplot(3, 2, 5)
plt.plot(time, out.b.CassiniOne, color="k")
plt.plot(time, out.c.CassiniOne, color=vplot.colors.red)
plt.xlabel("Time (kyr)")
plt.ylabel("$\sin{\Psi}$")

plt.subplot(3, 2, 6)
plt.plot(time, out.b.CassiniTwo, color="k")
plt.plot(time, out.c.CassiniTwo, color=vplot.colors.red)
plt.xlabel("Time (kyr)")
plt.ylabel("$\cos{\Psi}$")

# Save the figure
ext = sys.argv[1]
fig.tight_layout()
fig.savefig(path / f"CassiniMulti.{ext}")

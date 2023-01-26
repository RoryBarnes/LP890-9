import numpy as np
import matplotlib.pyplot as plt
from vplanet import get_output
from vplot import colors
import pathlib

path = pathlib.Path()
sims = [s for s in path.iterdir() if s.is_dir()]
time = []
semiMajorAxis = []

for sim in sims:
    try:
        out = get_output(path / sim, units=False)
    except Exception as ex:
        print(ex)
    try:
        time.append(out.star.Time/1e9)
        semiMajorAxis.append(out.c.SemiMajorAxis)
    except AttributeError:
        print('Semi-major axis output not found in ' + str(sim))

c_semi_major_axis           = np.ones(len(time[0])) * 0.03984
c_semi_major_axis_upper_lim = np.ones(len(time[0])) * 0.04006
c_semi_major_axis_lower_lim = np.ones(len(time[0])) * 0.03962

fig, ax = plt.subplots(1, 1)
ax.plot(time[0], c_semi_major_axis, color='k', ls='--')
ax.fill_between(time[0], c_semi_major_axis_upper_lim, c_semi_major_axis_lower_lim, color='gray', alpha=0.5)
for i, _ in enumerate(sims):
    ax.plot(time[i], semiMajorAxis[i], c='k', lw=0.5, alpha=0.7)
ax.set_ylim(0.038, 0.045)
ax.set_xlabel('Time (Gyr)')
ax.set_ylabel('Semi-major axis (au)')
fig.savefig(path / 'sma-evolutions.pdf', dpi=600)

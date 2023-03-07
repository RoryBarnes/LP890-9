import numpy as np
import matplotlib.pyplot as plt
from vplanet import get_output
from vplot import colors
import pathlib
import pandas as pd


path = pathlib.Path()
sims = [s for s in path.iterdir() if s.is_dir()]
for sim in sims:
    if 'paulbonneym_parametersweep' in sims:
        sims.remove(sim)
time = []
brot = []
crot = []
bobl = []
cobl = []
bcas1 = []
ccas1 = []
bcas2 = []
ccas2 = []
number_sims = 0


for sim in sims:
    try:
        out = get_output(path / sim, units=False)
    except Exception as ex:
        print(ex)
    try:
        tt = out.TGstar.Time
        end = np.searchsorted(tt, float(1e4), side='left')
        if end != len(tt): # Don't include any simulations that didn't run at least 10 kyr
            time.append(out.TGstar.Time[0:end] / 1e3) # Convert to kyr
            brot.append(out.TGb.RotPer[0:end])
            crot.append(out.TGc.RotPer[0:end])
            bobl.append(out.TGb.Obliquity[0:end])
            cobl.append(out.TGc.Obliquity[0:end])
            bcas1.append(out.TGb.CassiniOne[0:end])
            ccas1.append(out.TGc.CassiniOne[0:end])
            bcas2.append(out.TGb.CassiniTwo[0:end])
            ccas2.append(out.TGc.CassiniTwo[0:end])
            number_sims += 1
    # except TypeError as terr:
    #     print(terr)
    except AttributeError:
        print('Obliquity, sin(Psi), or cos(Psi) output not found in ' + str(sim))


# Need to read directly from the .forward files for Paul's parameter sweep,
# since the input and output files are in different directories.
paul_path = path / 'paulbonneym_parametersweep/outs'
paul_sims = [s for s in paul_path.iterdir() if s.is_dir()]
column_names = ['Time', 'RotPer', 'LongP', 'SemiMajorAxis', 'Eccentricity',
                'SurfEnFluxTot', 'Obli', 'PrecA', 'CassiniOne', 'CassiniTwo',
                'PrecFNat', 'DynEllip', 'DeltaT']
for sim in paul_sims:
    for file in sim.iterdir():
        if 'b.forward' in str(file):
            b_output_data = pd.read_csv(file, sep=' ', names=column_names, index_col=False)
            time.append(b_output_data['Time'] / 1e3) # Convert to kyr
            brot.append(b_output_data['RotPer'])
            bobl.append(b_output_data['Obli'])
            bcas1.append(b_output_data['CassiniOne'])
            bcas2.append(b_output_data['CassiniTwo'])
        if 'c.forward' in str(file):
            c_output_data = pd.read_csv(file, sep=' ', names=column_names, index_col=False)
            crot.append(c_output_data['RotPer'])
            cobl.append(c_output_data['Obli'])
            ccas1.append(c_output_data['CassiniOne'])
            ccas2.append(c_output_data['CassiniTwo'])
            number_sims += 1


for i in range(number_sims):
    if cobl[i][0] == 23.500077: # Hand-picked highlighted simulation
        red_idx = i
        # print(bobl[i][0], cobl[i][0])


fig, ax = plt.subplots(4, 2, figsize=(9, 6))
for i in range(number_sims):
    if i != red_idx:
        try:
            ax[0, 0].plot(time[i], brot[i], c='k', lw=0.5, alpha=0.01)
        except IndexError as ick:
            print(ick)
            print(i)
        ax[0, 1].plot(time[i], crot[i], c='k', lw=0.5, alpha=0.01)
        ax[1, 0].plot(time[i], bobl[i], c='k', lw=0.5, alpha=0.01)
        ax[1, 1].plot(time[i], cobl[i], c='k', lw=0.5, alpha=0.01)
        ax[2, 0].plot(time[i], bcas1[i], c='k', lw=0.5, alpha=0.01)
        ax[2, 1].plot(time[i], ccas1[i], c='k', lw=0.5, alpha=0.01)
        ax[3, 0].plot(time[i], bcas2[i], c='k', lw=0.5, alpha=0.01)
        ax[3, 1].plot(time[i], ccas2[i], c='k', lw=0.5, alpha=0.01)

ax[0, 0].plot(time[red_idx], brot[red_idx], c='r', lw=1, alpha=1)
ax[0, 1].plot(time[red_idx], crot[red_idx], c='r', lw=1, alpha=1)
ax[1, 0].plot(time[red_idx], bobl[red_idx], c='r', lw=1, alpha=1)
ax[1, 1].plot(time[red_idx], cobl[red_idx], c='r', lw=1, alpha=1)
ax[2, 0].plot(time[red_idx], bcas1[red_idx], c='r', lw=1, alpha=1)
ax[2, 1].plot(time[red_idx], ccas1[red_idx], c='r', lw=1, alpha=1)
ax[3, 0].plot(time[red_idx], bcas2[red_idx], c='r', lw=1, alpha=1)
ax[3, 1].plot(time[red_idx], ccas2[red_idx], c='r', lw=1, alpha=1)

ax[0, 0].set_title('LP 890-9 b')
ax[0, 1].set_title('LP 890-9 c')
ax[0, 0].set_ylabel('Rot. per. (days)')
ax[1, 0].set_ylabel(r'Obliquity ($^\circ$)')
ax[2, 0].set_ylabel(r'$\sin\Psi$')
ax[3, 0].set_ylabel(r'$\cos\Psi$')
ax[3, 0].set_xlabel('Time (kyr)')
ax[3, 1].set_xlabel('Time (kyr)')
for a in ax.ravel():
    a.set_xlim(0., 8.)
fig.savefig(path / 'obliquity-evol.png', dpi=600)

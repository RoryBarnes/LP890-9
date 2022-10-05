import numpy as np
import matplotlib.pyplot as plt
from vplanet import get_output
from vplot import colors
import pathlib
import pandas as pd


def number_bins(number_sims):
  # Sturges' rule.
  return int(np.ceil(1. + np.log2(number_sims)))


path = pathlib.Path()
sims = [s for s in path.iterdir() if s.is_dir()]
for sim in sims:
    if 'paulbonneym_parametersweep' in sims:
        sims.remove(sim)
init_bobl  = []
init_cobl  = []
final_bobl = []
final_cobl = []
number_sims = 0


for sim in sims:
    try:
        out = get_output(path / sim, units=False)
    except Exception as ex:
        print(ex)
        pass
    try:
        time = out.TGstar.Time
        # end = int(np.where(time == float(1e4))[0]) # Ensuring we use the values at 10 kyr as the "final" values
        end = np.searchsorted(time, float(1e4), side='left')
        if end != len(time): # Don't include any simulations that didn't run at least 10 kyr
            init_bobl.append(out.TGb.Obliquity[0])
            init_cobl.append(out.TGc.Obliquity[0])
            final_bobl.append(out.TGb.Obliquity[end])
            final_cobl.append(out.TGc.Obliquity[end])
            number_sims += 1
    # except TypeError as terr:
    #     print(terr)
    except AttributeError:
        print('Obliquity output not found in ' + str(sim))


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
            init_bobl.append(b_output_data['Obli'].iloc[0])
            final_bobl.append(b_output_data['Obli'].iloc[-1])
        if 'c.forward' in str(file):
            c_output_data = pd.read_csv(file, sep=' ', names=column_names, index_col=False)
            init_cobl.append(c_output_data['Obli'].iloc[0])
            final_cobl.append(c_output_data['Obli'].iloc[-1])
            number_sims += 1


bins = number_bins(number_sims)
fig, ax = plt.subplots(2, 2)
ax[0, 0].hist(init_bobl, bins=bins, weights=np.ones_like(init_bobl)/number_sims, color=colors.orange)
ax[0, 0].set_title('LP 890-9 b')
ax[0, 1].hist(init_cobl, bins=bins, weights=np.ones_like(init_bobl)/number_sims, color=colors.pale_blue)
ax[0, 1].set_title('LP 890-9 c')
ax[1, 0].hist(final_bobl, bins=bins, weights=np.ones_like(init_bobl)/number_sims, color=colors.orange)
ax[1, 0].set_xlim(0.003, 0.015)
ax[1, 1].hist(final_cobl, bins=bins, weights=np.ones_like(init_bobl)/number_sims, color=colors.pale_blue)
ax[1, 1].set_xlim(0.1, 0.6)
for a in ax[0]:
    a.axhline(1/bins, ls='--', c='k')
    a.set_xlim(0., 180.)
    a.set_xlabel(r'Initial obliquity ($^\circ$)')
for a in ax[1]:
    a.set_xlabel(r'Obliquity after 10 kyr ($^\circ$)')
fig.savefig(path / 'obliquity-histogram.pdf', dpi=600)

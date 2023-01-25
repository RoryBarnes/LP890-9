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
bobl = []
cobl = []
bpreca = []
cpreca = []
blonga = []
clonga = []
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
            # Need to grab longs. of asc. node from .log files, forgot to list as VPLanet output
            longas = []
            with open(path / sim / 'TG.log') as log:
                content = [line.strip().split() for line in log.readlines()]
                for line in content:
                    if line:
                        if line[0] == '(LongA)':
                            longas.append(float(line[7]))
                if len(longas) != 4:
                    print('Something went wrong reading the .log file')
                    exit(1)
            # Values at the end of the simulation
            blonga.append(longas[2])
            clonga.append(longas[3])
            bobl.append(out.TGb.Obliquity[-1])
            cobl.append(out.TGc.Obliquity[-1])
            bpreca.append(out.TGb.PrecA[-1])
            cpreca.append(out.TGc.PrecA[-1])
            number_sims += 1
    except AttributeError:
        print('Obliquity or precession angle output not found in ' + str(sim))
    except FileNotFoundError:
        print('Log file not found in ' + str(sim))



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
            bobl.append(b_output_data['Obli'].iloc[-1])
            bpreca.append(b_output_data['PrecA'].iloc[-1])
        if 'c.forward' in str(file):
            c_output_data = pd.read_csv(file, sep=' ', names=column_names, index_col=False)
            cobl.append(c_output_data['Obli'].iloc[-1])
            cpreca.append(c_output_data['PrecA'].iloc[-1])
            number_sims += 1
        if '.log' in str(file):
            longas = []
            with open(file) as log:
                content = [line.strip().split() for line in log.readlines()]
                for line in content:
                    if line:
                        if line[0] == '(LongA)':
                            longas.append(float(line[7]))
                if len(longas) != 4:
                    print('Something went wrong reading the .log file')
                    exit(1)
                # Values at the end of the simulation
                blonga.append(longas[2])
                clonga.append(longas[3])

bobl = np.array(bobl)
cobl = np.array(cobl)
bpreca = np.array(bpreca)
cpreca = np.array(cpreca)
blonga = np.array(blonga)
clonga = np.array(clonga)

x1 = np.sin(bobl) * np.cos(bpreca + blonga)
y1 = np.sin(bobl) * np.sin(bpreca + blonga)
x2 = np.sin(cobl) * np.cos(cpreca + clonga)
y2 = np.sin(cobl) * np.sin(cpreca + clonga)

theta = np.linspace(0., 2.*np.pi, 1000)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].scatter(x1, y1, c=colors.orange, label='b')
ax[1].scatter(x2, y2, c=colors.pale_blue, label='c')
ax[0].set_ylabel(r'$\sin(\varepsilon) \sin(\psi + \Omega)$')
ax[0].set_title('LP 890-9 b')
ax[1].set_title('LP 890-9 c')
for a in ax:
    a.plot(np.sin(theta), np.cos(theta), c='k') # edge of the phase space
    a.set_xlabel(r'$\sin(\varepsilon) \cos(\psi + \Omega)$')
    a.set_xlim(-1.1, 1.1)
    a.set_ylim(-1.1, 1.1)

fig.savefig('cassini-states.png', dpi=200)

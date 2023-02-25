import pathlib
import sys
from statistics import mean
from fractions import Fraction

import matplotlib as mpl
import matplotlib.pyplot as plt

import vplanet
import sys

"""
# Check correct number of arguments
if (len(sys.argv) != 2):
    print('ERROR: Incorrect number of arguments.')
    print('Usage: '+sys.argv[0]+' <pdf | png>')
    exit(1)
if (sys.argv[1] != 'pdf' and sys.argv[1] != 'png'):
    print('ERROR: Unknown file format: '+sys.argv[1])
    print('Options are: pdf, png')
    exit(1)
"""

# Path hacks
path = pathlib.Path(__file__).parents[0].absolute()
sys.path.insert(1, str(path.parents[0]))


cPlotName = "LP890-9_ResArg"
# Run vplanet
output = vplanet.run(path / "vpl.in", quiet=True, units=False)
time = output.star.Time
aMeanLb = output.b.MeanLongitude
aMeanLc = output.c.MeanLongitude
aLongPb = output.b.LongP
aLongPc = output.c.LongP
aSemiAb = output.b.SemiMajorAxis
aSemiAc = output.c.SemiMajorAxis
aOrbPb = output.b.OrbPeriod
aOrbPc = output.c.OrbPeriod
aEnergyTotal = output.b.TotEnergy

# Comparing initial to final total energy of system
dEnergyInit = aEnergyTotal[0]
dEnergyFinal = aEnergyTotal[-1]
print("")
print("Initial total energy:", dEnergyInit)
print("Final total energy:", dEnergyFinal)

dEnergyErr = abs(dEnergyFinal/dEnergyInit - 1)
print("Percent change in Energy:", str(dEnergyErr * 100 ) + "%")

dOrbPRatio = 0
if aOrbPb[0] > aOrbPc[0]:
	dOrbPRatio = aOrbPb[0] / aOrbPc[0]
if aOrbPb[0] < aOrbPc[0]:
	dOrbPRatio = aOrbPc[0] / aOrbPb[0]

iOrbPRatio = int(dOrbPRatio)
fOrbPFrac = Fraction(dOrbPRatio).limit_denominator(2)
dResExact = float(fOrbPFrac)
tOrbPFrac = dResExact.as_integer_ratio()
dResNumerator = fOrbPFrac.numerator
dResDenominator = fOrbPFrac.denominator

dTolerance = dOrbPRatio - dResExact
print("Expected Resonance:", str(dResNumerator) + 
                        ":" + str(dResDenominator))
print("OrbPeriod tolerance:", dTolerance)
print("")

# Changed to a Resonance Argumet of 3:1 for c:b satellites
aRes1 = 3 * aMeanLc - aMeanLb - 2 * aLongPc
aRes2 = 3 * aMeanLc - aMeanLb - 2 * aLongPb
aRes3 = 3 * aMeanLc - aMeanLb - aLongPc - aLongPb


aaResonances = [[dAng % 360 for dAng in aRes1], 
                [dAng % 360 for dAng in aRes2], 
                [dAng % 360 for dAng in aRes3]]
aResArguments = [r"$3\lambda_c - \lambda_b - 2\varpi_c$", 
                r"$3\lambda_c - \lambda_b - 2\varpi_b$", 
                r"$3\lambda_c - \lambda_b - \varpi_c - \varpi_b$"]

dMeanLb0 = aMeanLb[0] % 360
dMeanLc0 = aMeanLc[0] % 360
dMeanLDiff = dMeanLc0 - dMeanLb0
print("Initial Mean Longitude of b:", dMeanLb0, "degrees.")
print("Initial Mean Longitude of c:", dMeanLc0, "degrees.")
print("Initial Mean Longitude difference:", dMeanLDiff, "degrees.")
print("")

dToleranceLib = 10.0 # [deg] Denotes how large the exclusion is

"""
Below we shift the resonant argument arrays by 180 deg
since we are trying to find any exclusion zones around
+/-180 deg. If there are, then any of the resonant
arguments are in a resonance oscillating around 0 deg
"""
aiResValues = [0, 180] #Most resonances are centered around either 0 or 180 degrees.
for iRes in aiResValues:
    for i in range(len(aaResonances)):
        dAngShift = 180
        dMeanResArg = int(mean(aaResonances[i])) + iRes - dAngShift
        aResShift = [dAng + iRes - dAngShift for dAng in aaResonances[i]]
        dResMin = min(aResShift)
        dResMax = max(aResShift)
        #trough of the assumed cyclic curve cannot exceed lower than this value
        dToleranceMin = iRes - dAngShift + dToleranceLib / 2.0
        #Crest of the assumed cyclic curve cannot exceed higher than this value
        dToleranceMax = iRes + dAngShift - dToleranceLib / 2.0
        
        print("Resonant Argument " + str(aResArguments[i]))
        print("Mean angle:", dMeanResArg, "degrees.")
        if dResMin > dToleranceMin and dResMax < dToleranceMax:
            print("Satellites are in a resonance around " + 
                    str(iRes) + " degrees.")
        elif dResMin < dToleranceMin or dResMax > dToleranceMax:
            print("Satellites are not in a resonance around " + 
                    str(iRes) + " degrees.")
        print("")

# plotting
mpl.rcParams['figure.figsize'] = (6.5,6.5)
mpl.rcParams['font.size'] = 11.0

fig, axes = plt.subplots(ncols=1, nrows=len(aaResonances), sharey=False)
n = 5 # Adjusts how many points can be cut off to save reduce file size
aTimeKilo = time[::n] / 1000.0 # time expressed in kiloyears
for sim in range(len(aaResonances)):
    aResArg = aaResonances[sim][::n]
    axes[sim].scatter(aTimeKilo, aResArg, 
                    label = aResArguments[sim], color = "black", s = 1.0)
    axes[sim].set_xlabel("Time [kyr]")
    axes[sim].set_ylabel(aResArguments[sim] + " [$^\circ$]", fontsize=12)
    axes[sim].set_xlim(min(aTimeKilo), max(aTimeKilo))
    axes[sim].set_ylim(0.0, 360.0)
fig.tight_layout()

if (sys.argv[1] == 'pdf'):
    plt.savefig(path / (cPlotName + ".pdf"), bbox_inches="tight", dpi=400)
elif (sys.argv[1] == 'png'):
    plt.savefig(path / (cPlotName + ".png"), bbox_inches="tight", dpi=400)
else:
    print("Your first argument needs to be either png or pdf")
  

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [10, 8]
plt.rcParams.update({   'font.size': 28,
                        "font.family": "serif",
                        "font.serif": ["CMU serif"],
                        "font.sans-serif" : ["CMU sans serif"]})
plt.rc('axes', unicode_minus=False)
plt.rc('axes', unicode_minus=False)
plt.rc('pgf', texsystem='pdflatex')


file = 'CBS/data/MT/NbN_5nm_07022022-_heating_data.txt'
data = np.transpose(np.loadtxt(file,skiprows=1,usecols=(0,6),delimiter=','))

temp = data[0]
ind = data[1]

plt.plot(temp,ind,'-k')
plt.xlabel('Temperature (K)')
plt.ylabel("Mutual Inductance (nH)")
plt.minorticks_on()
# plt.show()
plt.savefig('/mnt/localdiskd/Semester 8/Project - Superconductivity/Report/images/MTintro.pdf')
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [10, 8]
plt.rcParams.update({   'font.size': 28,
                        "font.family": "serif",
                        "font.serif": ["CMU serif"],
                        "font.sans-serif" : ["CMU sans serif"]})
plt.rcParams['mathtext.fontset'] = 'stix'

plt.rc('axes', unicode_minus=False)
plt.rc('axes', unicode_minus=False)
plt.rc('pgf', texsystem='pdflatex')

def diff(x,y):
    return [(y[i+1]-y[i])/(x[i+1]-x[i]) for i in range(x.size -1)]

path = "CBS/data/tunneljunction_NbNAlNAg_17032022/ivtest_3.4Kr3.txt"
data = np.transpose(np.loadtxt(path, usecols=(0,1),skiprows=1))

plt.plot(data[0],data[1],'-k')
plt.xlabel('Voltage (mV)')
plt.ylabel('Current (mA)')
plt.minorticks_on()
plt.show()
# plt.savefig('/mnt/localdiskd/Semester 8/Project - Superconductivity/Report/images/tunintroIV.pdf')

plt.clf()
didv = diff(data[0],data[1])

dat = np.array([data[0,1:],didv])
dat[1] = dat[1]/np.average(dat[1,5:15])
plt.xlabel('Voltage (mV)')
plt.ylabel(r'${\frac{dI}{dV}} \; / \; {\left(\frac{dI}{dV}\right)_N}$')
plt.tight_layout()
plt.minorticks_on()
plt.plot(dat[0],dat[1],'-g')
plt.show()
# plt.savefig('/mnt/localdiskd/Semester 8/Project - Superconductivity/Report/images/tunintrodidv.pdf')

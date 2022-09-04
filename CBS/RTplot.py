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
plt.rcParams['mathtext.fontset'] = 'stix'


file = 'CBS/data/tunneljunction_NbNAlNAg_17032022/RTHeating2.txt'
data = np.transpose(np.loadtxt(file,skiprows=1,usecols=(0,3)))

temp = data[0]
res = data[1]

plt.plot(temp,res,'-k')
plt.xlabel('Temperature (K)')
plt.ylabel("Resistance (Ohms)")
plt.minorticks_on()
plt.show()
# # plt.savefig('/mnt/localdiskd/Semester 8/Project - Superconductivity/Report/images/tunnelRT.pdf')






# file = 'CBS/data/RT_GNBN14_21022022/heatingrun1.txt'
# data = np.transpose(np.loadtxt(file,skiprows=1,usecols=(0,4)))

# temp = data[0]
# res = data[1]
# fig, ax = plt.subplots(1,1)

# ax.plot(temp,res,'-k')
# ax.vlines(12.88,-5,19.95,linestyles='dotted',color='black')
# ax.set_xlabel('Temperature (K)')
# ax.set_ylabel("Resistance (Ohms)")
# ax.set_ylim(-1,)

# xt = ax.get_xticks() 
# xt=np.append(xt,12.88)

# xtl=xt.tolist()
# xtl[-1]=r"$T_c$"
# ax.set_xticks(xt)
# ax.set_xticklabels(xtl)

# plt.minorticks_on()
# # plt.show()
# plt.savefig('/mnt/localdiskd/Semester 8/Project - Superconductivity/Report/images/RTintro.pdf')
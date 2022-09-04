import numpy as np
import matplotlib.pyplot as plt
import confitmodule as cm
from scipy.signal import savgol_filter

plt.rcParams['figure.figsize'] = [10, 8]
plt.rcParams.update({   'font.size': 28,
                        "font.family": "serif",
                        "font.serif": ["CMU serif"],
                        "font.sans-serif" : ["CMU sans serif"],
                        })
plt.rc('axes', unicode_minus=False)
plt.rc('axes', unicode_minus=False)
plt.rc('pgf', texsystem='pdflatex')
plt.rcParams['mathtext.fontset'] = 'stix'


def diff(x,y):
    return [(y[i+1]-y[i])/(x[i+1]-x[i]) for i in range(x.size -1)]

# list = [
# 'iv_2.9K.txt',
# 'iv_3.4K.txt',
# 'iv_4.0K.txt',
# 'iv_5.0K.txt',
# 'iv_7.0K.txt',
# 'iv_9.0K.txt',
# 'iv_11.0K.txt',
# 'iv_13.0K.txt',
# 'iv_14.0K.txt']

list =[
'iv3k.txt',
'iv3.5k.txt',
'iv4k.txt',
'iv5k.txt',
'iv6k.txt',
'iv8k.txt',
'iv10k.txt',
'iv12k.txt',
'iv13k.txt',
'iv15k.txt',
'iv16k.txt',
'iv16.5k.txt',
'iv17k.txt'
]

fig, ax1 = plt.subplots()
#inset
insetfont  = {'fontsize': 20,
 'fontweight' : 10}
left, bottom, width, height = [0.67, 0.2, 0.2, 0.2]
ax2 = fig.add_axes([left, bottom, width, height])
file1 = 'CBS/data/goodtunneljunc-NbNAloAg_2903+0704/rtheat.txt'
rtdat = np.transpose(np.loadtxt(file1,skiprows=1,usecols=(0,4)))
ax2.plot(rtdat[0],rtdat[1],'-k')
ax2.set_title('RT',fontdict=insetfont)
ax2.set_xlim(15.5,17.5)
ax2.set_ylim(8,13)
ax2.set_xticks([16,16.5,17])
ax2.tick_params(axis='x', labelsize=16 )
ax2.tick_params(axis='y', labelsize=16 )


for file in list:
    path = f"CBS/data/goodtunneljunc-NbNAloAg_2903+0704/{file}"
    data = np.transpose(np.loadtxt(path, usecols=(0,1),skiprows=1))

    didv = diff(data[0],data[1])

    dat = np.array([data[0,1:],didv])
    dat[1] = dat[1]/np.average(dat[1,5:15])
    dat[1] = savgol_filter(dat[1], 15, 2) # window size, polynomial order
    slope_shift = (np.average(dat[1][-20:])-np.average(dat[1][:20]))/(dat[0][-1]-dat[0][0])
# print((dat[0]-dat[0][0]))
    # plt.plot(dat[0],dat[1] - (dat[0]-dat[0][0])*slope_shift,'b')
    dat[1] = dat[1] - (dat[0]-dat[0][0])*slope_shift
    lbl = file.split("v")[1].split('.txt')[0]
    ax1.plot(dat[0],dat[1],'o-',markersize=2,label=lbl)


plt.minorticks_on()
ax1.set_xlabel('Voltage (mV)')
ax1.set_ylabel(r'${\frac{dI}{dV}} \; / \; {\left(\frac{dI}{dV}\right)_N}$')
ax1.legend(loc=2,prop={'size': 19})
# plt.tight_layout()
# ax1.set_xlim(-9,9)
# plt.show()
plt.savefig('/mnt/localdiskd/Semester 8/Project - Superconductivity/Report/images/goodtundidv.pdf')


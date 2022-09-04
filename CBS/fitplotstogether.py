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

]

for file in list:
    path = f"CBS/data/goodtunneljunc-NbNAloAg_2903+0704/{file}"
    T=float(file.split("v")[1].split("k")[0])
    data = np.transpose(np.loadtxt(path, usecols=(0,1),skiprows=1))

    didv = diff(data[0],data[1])
    dat = np.array([data[0,1:],didv])
    if T==16.5 : dat = dat[:,100:-100]
    dat[1] = dat[1]/np.average(dat[1,5:15])

    dat[1] = savgol_filter(dat[1], 15, 2) # window size, polynomial order

    slope_shift = (np.average(dat[1][-20:])-np.average(dat[1][:20]))/(dat[0][-1]-dat[0][0])
    dat[1] = dat[1] - (dat[0]-dat[0][0])*slope_shift


    lcut1 = -5.5
    lcut2 = -2.5
    rcut1 = 2.5
    rcut2 = 5.5
    wt=100

    mask = (lcut2 > dat[0])*(dat[0] > lcut1)+(rcut1<dat[0])*(dat[0]<rcut2)
    unc = mask*1/wt + ~mask*(np.max(dat[1])-np.max(dat[0]))/10

    fit,err = cm.Conductancefit(dat,T,unc,inter='False')

    V = np.linspace(dat[0][0],dat[0][-1],500)
    if T == 16.5 : fit[0],fit[1] = 1.5, 0.9
    if T == 4.0 : fit[0],fit[1]=0.18617034,3.06114686
    if T == 16.0 : fit[0],fit[1]=1.00809552,1.50193351

    G_values = [cm.G_cond(i,fit[0],fit[1],T) for i in V]
    G_values = np.array(G_values)/G_values[0]

    print(T,fit[0],2.355*np.sqrt(np.diag(err))[0],fit[1],2.355*np.sqrt(np.diag(err))[1])
    plt.plot(V,G_values,'-',label=f'Fit @ {T}K')
    plt.plot(dat[0],dat[1],'o',markersize=1.5,color=plt.gca().lines[-1].get_color())


plt.xlabel('Voltage (mV)')
plt.ylabel(r'${\frac{dI}{dV}} \; / \; {\left(\frac{dI}{dV}\right)_N}$')
plt.legend(loc=3,prop={'size': 17})
plt.minorticks_on()
plt.tight_layout()
plt.xlim(-7,7)
# plt.show()
plt.savefig('/mnt/localdiskd/Semester 8/Project - Superconductivity/Report/images/tundidvfinal.pdf')

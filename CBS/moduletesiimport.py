import confitmodule as cm
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


filenames = ['1.18 K.dat',
'2.35 K.dat',
'3.5 K.dat',
'4.6 K.dat',
'5.0 K.dat',
'6.0 K.dat',
'6.2 K.dat',
'6.4 K.dat']


# for file in filenames:

#     T = float(file.split(" ")[0])
#     path = "/mnt/localdiskd/Semester 8/Project - Superconductivity/Code/CBS/data/testfit/" + f"{file}"
#     data = np.transpose(np.loadtxt(path,delimiter="\t"))
#     fit = cm.Conductancefit(data,T)
#     print(T , fit[0], fit[1])





path = "/mnt/localdiskd/Semester 8/Project - Superconductivity/Code/CBS/data/testfit/" + f"{filenames[1]}"
data = np.transpose(np.loadtxt(path,delimiter="\t"))
data[1] = savgol_filter(data[1], 5, 3)
T=1.18
fit = cm.Conductancefit(data,T,inter=True)
print(T , fit[0], fit[1])
# Gam, Delta = fit[0], fit[1]
V = np.linspace(-8,8,512)
G_values = [cm.G_cond(i,0.6935768282797028,1.2913417412133714,T) for i in V]
G_values = G_values/np.max(G_values)
plt.plot(V,G_values,'-r')
plt.plot(data[0],data[1],'-g')

# plt.plot(data[0],np.divide(G_values,data[1]))
plt.show()

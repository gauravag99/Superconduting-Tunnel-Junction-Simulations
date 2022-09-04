import numpy as np
import scipy.constants as const
import scipy.integrate as scint
import scipy.optimize as sc
import matplotlib.pyplot as plt
from numba import njit
from scipy import interpolate


#Constants:
kb = const.physical_constants["Boltzmann constant in eV/K"][0]*1e3


@njit
def Dfermi(E,V,T):
    return (1/(np.cosh((E+V)/(2*kb*T)) )**2 * (4*kb*T))

@njit
def dos(E,Gam,Delta):
    return np.real((np.abs(E)+complex(0,Gam))/np.sqrt((np.abs(E)+complex(0,Gam))**2 - Delta**2))

def G_cond(V,Gam,Delta,T):
    tmp = lambda E : dos(E,Gam,Delta)*Dfermi(E,V,T)
    return scint.quad(tmp,-100,100)[0]


def Conductancefit(data,T,sig,inter=True):
    t1 = data[0]
    t2= data[1]

    def vectorize1(V,Gam,Delta):
        #faster fitting but could have errors as it interpolates in between
        small_V = np.linspace(min(V),max(V),300)
        out = [G_cond(i, Gam, Delta,T) for i in small_V]
        def cond(x):
            tck = interpolate.splrep(small_V, out)
            return interpolate.splev(x, tck)
        ans = cond(V)
        return np.array(ans)/ans[0]

    
    def vectorize2(V,Gam,Delta):
        #slow fitting, only use when data points are around 400
        out = [G_cond(i, Gam, Delta,T) for i in V]

        return np.array(out)/out[0]

    bounds = ([0,0],[5 ,5])
    if inter == True:
        fit,err= sc.curve_fit(vectorize1,t1,t2,bounds=bounds,sigma=sig)
    else:
        fit,err= sc.curve_fit(vectorize2,t1,t2,bounds=bounds,sigma=sig)

    return fit,err
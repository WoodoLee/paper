import math 
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

def calN(gT, A, oa, error):
    N = 2 / ( (error * oa * gT * A)**2 )
    return N 

mumass    = 105.6583715 # muon mass [MeV]
emass     = 0.510998928 # electron mass [MeV]
E_max_mrf = mumass/2.0  # maximum positron energy from muon decay in muon-rest-frame (MRF)
mumom     = 300.0 # muon beam momentum [MeV]
beta      = mumom / math.sqrt( pow(mumom,2)+pow(mumass,2) ) # muon beam velocity (~ 0.9432)
Gamma     = math.sqrt( pow(mumom,2)+pow(mumass,2) )/mumass # ~ 3.0103
gT  = Gamma*2.1969811 # [us]
E_max_lab = Gamma*0.5*mumass*(1+beta) # maximum positron energy from muon decay in lab-frame [MeV] (~ 309.031 MeV)
E_max_lab = Gamma*mumass; # (obsolete), used in TDR

oa   = 2.0*math.pi/2.111
A = 0.42 * 0.5

arrN = []
arrE = []

for i in range(5,100):    
    error = i * 1e-8   
    N = calN(gT, A, oa, error)
    arrE.append(error)
    arrN.append(N)


targetE = 1e-7
targetN = calN(gT, A, oa, targetE)
print(targetN * 1e-13)

plt.plot( arrE , arrN , c = 'blue', label = 'e+ numbers vs $\omega_{a}^{Error}$')
plt.ylabel(' number of e+')
plt.xlabel('$\omega_{a}^{Error}$')
plt.gca().invert_xaxis()
plt.scatter(targetE, targetN, c= 'red', label = 'target(e+ numbers , $\omega_{a}^{Error}$)')
plt.annotate(str(0.1) + 'ppm , ' + str(round(targetN * 1e-13, 2)) + ' T'  ,xy=(targetE,targetN),xytext=(0.4*1e-6,1.5*1e+13),arrowprops={'color':'red'})
plt.grid(True)
plt.legend()
plt.show()
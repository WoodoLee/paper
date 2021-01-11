import math 
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
font = {
#    'weight' : 'bold',
    'size'   : 25
    }

plt.rc('font', **font)


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

for i in range(5,10000):    
    error = i * 1e-8   
    N = calN(gT, A, oa, error)
    arrE.append(error)
    arrN.append(N)



targetE1 = 1e-7
targetE2 = 1e-6
targetE3 = 1e-5
targetE4 = 1e-4
targetN1 = calN(gT, A, oa, targetE1)
targetN2 = calN(gT, A, oa, targetE2)
targetN3 = calN(gT, A, oa, targetE3)
targetN4 = calN(gT, A, oa, targetE4)
print(targetN1 * 1e-13)
print(targetN2 * 1e-13)
print(targetN3 * 1e-13)
targetE = [targetE1,targetE2,targetE3,targetE4]
targetN = [targetN1,targetN2,targetN3,targetN4] 

#plt.plot( arrE , arrN , c = 'blue', label = 'e+ numbers vs $\omega_{a}^{Error}$')
plt.plot( arrE , arrN , c = 'blue')
plt.ylabel(' number of $e^{+}$')
plt.xlabel('$\omega_{a}^{Error}$')
plt.gca().invert_xaxis()
#plt.scatter(targetE, targetN, c= 'red', label = 'target(e+ numbers , $\omega_{a}^{Error}$)')
plt.scatter(targetE, targetN, c= 'red', label = 'target')
plt.xscale("log")
plt.yscale("log")
#plt.annotate(str(0.1) + 'ppm , ' + str(round(targetN * 1e-13, 2)) + ' T'  ,xy=(targetE,targetN),xytext=(0.4*1e-6,1.5*1e+13),arrowprops={'color':'red'})
plt.grid(True)
plt.legend()

plt.show()

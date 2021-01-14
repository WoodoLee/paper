import math
import numpy as np
import matplotlib.pyplot as plt
import math

plt.rcParams['font.family'] = 'Times New Roman'
font = {
#    'weight' : 'bold',
    'size'   : 25
    }

plt.rc('font', **font)


mumass    = 105.6583715
emass     = 0.510998928 # MeV
E_max_mrf = mumass/2.0  #n energy from muon decay in muon-rest-frame (MRF)
mumom     = 300.0 # muon beam momentum [MeV]
beta      = mumom/math.sqrt( pow(mumom,2)+pow(mumass,2) )  # muon beam velocity (~ 0.9432)
Gamma     = math.sqrt( pow(mumom,2)+pow(mumass,2) )/mumass # ~ 3.0103
gammatau  = Gamma*2.1969811 # [us]
E_max_lab = Gamma*0.5*mumass*(1+beta) # maximum positron energy from muon decay in lab-frame [MeV] (~ 309.031 MeV)
omega_a   = 2.0*math.pi/2.111
N0 = 100000000. #number of muons
tW = 5e-9 #ASIC time window
A = 0.42 *0.5 # Asymmetry

tWa = []
ne = []
nb = []

for i in range(6000):
    tWa.append( tW * i )

for i in range(5999):
    nb.append(i*1e-2)
    nEt1= N0 * math.exp ( -tWa[i] / (gammatau*1e-6) )  - N0 * math.exp ( -tWa[i+1] / (gammatau*1e-6) )
    nEt2= N0 * math.exp ( -tWa[i] / (gammatau*1e-6) ) * ( 1 + A * math.cos(omega_a * tWa[i]))  - N0 * math.exp ( -tWa[i+1] / (gammatau*1e-6) )* ( 1 + A * math.cos(omega_a * tWa[i+1])) 
    nEt = nEt1 - nEt2
    ne.append(nEt2)

print(ne[0])

plt.plot( nb , ne , c = 'red')
plt.grid(True)
plt.ylabel('number of pile up $e^{+}$')
plt.xlabel('time ($\mu s$)')
plt.ylim(0,100000)
plt.show()
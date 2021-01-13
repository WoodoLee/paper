import os, sys
import ROOT as root
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
font = {
# 'weight' : 'bold',
    'size'   : 25
    }

plt.rc('font', **font)

def importROOT(filename):
  f = root.TFile.Open(filename, "read")
  fTree = f.Get("MC")
  dataFitResult, columnsFitResult = fTree.AsMatrix(return_labels=True)
  dfFile = pd.DataFrame(data=dataFitResult, columns=columnsFitResult)
  return(dfFile)



name = "/home/wdlee/Work/data/g2wd.root"


dfMcRaw = importROOT(name)

print(dfMcRaw['mcTime'])
dfMcT = dfMcRaw['mcTime']

nMax = 60 / 2
nbins = int(nMax *1e-6 / (5e-9)) 


plt.hist(dfMcT.values, bins=nbins, range= (0,nMax), edgecolor = 'blue', histtype='step', color='blue')
plt.xlim(0, nMax)
plt.ylabel('number of $e^{+}$')
plt.xlabel('Decay time ($\mu s$)')
plt.grid(b=True, which='both', axis='both')
plt.yscale("log")
plt.show()
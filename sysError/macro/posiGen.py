import os, sys
import ROOT as root
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
font = {
# 'weight' : 'bold',
    'size'   : 40
    }

plt.rc('font', **font)

def importROOT(filename):
  f = root.TFile.Open(filename, "read")
  fTree = f.Get("tree1")
  dataFitResult, columnsFitResult = fTree.AsMatrix(return_labels=True)
  dfFile = pd.DataFrame(data=dataFitResult, columns=columnsFitResult)
  return(dfFile)



name = "/home/wdlee/data1/posiGen/momN.root"


dfMcRaw = importROOT(name)

dfMcT = dfMcRaw['pMagTot']
dfMcLow = dfMcT[dfMcT < 200]
dfMcHigh = dfMcT[dfMcT > 275]
dfMcTarget = dfMcT[dfMcT > 200]
dfMcTarget = dfMcTarget[dfMcTarget < 275]

print(dfMcTarget)

print(len(dfMcT))
print(len(dfMcLow))
print(len(dfMcTarget))
print(len(dfMcHigh))

perTarget = (len(dfMcTarget) / len(dfMcT))* 100
perHigh = (len(dfMcHigh) / len(dfMcT)) * 100
perLow = (len(dfMcLow) / len(dfMcT)) * 100

print(perTarget)
print(perHigh)
print(perLow)

nMax = 350
nbins = int(nMax *3) 


plt.hist(dfMcT.values, bins=nbins, range= (0,nMax), edgecolor = 'blue', histtype='step', color='blue')
plt.hist(dfMcTarget.values, bins=nbins, range= (0,nMax), edgecolor = 'red', color='red', alpha = 0.3, label='Target range , ' + str(perTarget) + ' % ')
plt.hist(dfMcLow.values, bins=nbins, range= (0,nMax), edgecolor = 'yellow', color='yellow', alpha = 0.3, label='Low range , ' + str(perLow) + ' % ')
plt.hist(dfMcHigh.values, bins=nbins, range= (0,nMax), edgecolor = 'Black', color='Black', alpha = 0.3, label='High range , ' + str(perHigh) + ' % ')
plt.xlim(0, nMax)
plt.ylabel('number of $e^{+}$')
plt.xlabel('$P_{e^+}$ (MeV/c)')
plt.grid(b=True, which='both', axis='both')
plt.legend(prop={'size': 25})
plt.show()
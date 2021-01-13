import os, sys
import ROOT as root
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F
from ROOT import gROOT, gBenchmark, gRandom, gSystem
import numpy as np
import pandas as pd
name = "/home/wdlee/Work/data/g2wd.root"
f = root.TFile(name)
tMC = f.Get("MC")


def importROOT(filename):
  f = root.TFile.Open(filename, "read")
  fTree = f.Get("MC")
  dataFitResult, columnsFitResult = fTree.AsMatrix(return_labels=True)
  dfFile = pd.DataFrame(data=dataFitResult, columns=columnsFitResult)
  return(dfFile)

dfTest = importROOT(name)

print(dfTest)
# Create a new canvas, and customize it.
c1 = TCanvas( 'c1', 'Dynamic Filling Example', 200, 10, 700, 500 )
c1.SetGridx()
c1.SetGridy()
# c1.SetFillColor( 42 )
# c1.GetFrame().SetFillColor( 21 )
# c1.GetFrame().SetBorderSize( 6 )
# c1.GetFrame().SetBorderMode( -1 )



nMax = 60 / 2
nbins = nMax *1e-6 / (5e-9) 

print(nbins)
hpx    = TH1F( 'hpx', 'This is the px distribution', int(nbins), 0, int(nMax) )
#hpx.SetFillColor( 48 )



# For speed, bind and cache the Fill member functions,
histos = [ 'hpx' ]
for name in histos:
   exec('%sFill = %s.Fill' % (name,name))



histArr = np.array([])

for i in tMC:
  test = i.mcTime
  hpx.Fill( test )
  #histArr = np.append(histArr, test)

print(histArr)

hpx.Draw()
# hpx.SetFillColor( 0 )
# hpx.SetFillColor( 48 )
c1.Modified()
c1.Update()

# plt.hist(histArr, cumulative=True, label='cumulative=True')
# plt.hist(histArr, cumulative=False, label='cumulative=False')
# plt.legend(loc='upper left')
# plt.show()

## wait for input to keep the GUI (which lives on a ROOT event dispatcher) alive
if __name__ == '__main__':
   rep = ''
   while not rep in [ 'q', 'Q' ]:
      # Check if we are in Python 2 or 3
      if sys.version_info[0] > 2:
         rep = input( 'enter "q" to quit: ' )
      else:
         rep = raw_input( 'enter "q" to quit: ' )
      if 1 < len(rep):
         rep = rep[0]
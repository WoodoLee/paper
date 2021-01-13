import os, sys
import ROOT as root
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F, TPad
from ROOT import TCanvas, TColor, TGaxis
from ROOT import gROOT, gBenchmark, gRandom, gSystem
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ROOT import kBlack, kBlue, kRed

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


nameMc = "/home/wdlee/data1/pileUp/mcTruthZcorrec.root"
namePile = "/home/wdlee/data1/pileUp/result/100k/100kpileUp.root"


fMc= root.TFile.Open(nameMc, "read")
fPileUp= root.TFile.Open(namePile, "read")



hMc = fMc.Get("mc Decay Time")
hPileUp = fPileUp.Get("mc Decay Time")
print (hMc.GetEntries())
print (hPileUp.GetEntries())


# hMc.Draw()
# hPileUp.Draw("pe , same ")

def createRatio(h1, h2):
   h3 = h1.Clone("h3")
   h3.SetLineColor(kBlack)
   h3.SetMarkerStyle(21)
   h3.SetTitle("")
   # h3.SetMinimum(0.8)
   # h3.SetMaximum(1.35)
   # # Set up plot for markers and errors
   h3.Sumw2()
   h3.SetStats(0)
   h3.Divide(h2)
   # Adjust y-axis settings
   y = h3.GetYaxis()
   y.SetTitle("ratio h1/h2 ")
   y.SetNdivisions(505)
   y.SetTitleSize(20)
   y.SetTitleFont(43)
   y.SetTitleOffset(1.55)
   y.SetLabelFont(43)
   y.SetLabelSize(15)
   # Adjust x-axis settings
   x = h3.GetXaxis()
   x.SetTitleSize(20)
   x.SetTitleFont(43)
   x.SetTitleOffset(4.0)
   x.SetLabelFont(43)
   x.SetLabelSize(15)
   return h3


h1 = hMc
h2 = hPileUp
h1.SetLineColor(kBlack)
h2.SetLineColor(kBlue)
h3 = createRatio(h2, h1)

c = TCanvas("c", "canvas", 800, 800)
# Upper histogram plot is pad1
pad1 = TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
pad1.SetBottomMargin(0)  # joins upper and lower plot
pad1.SetGridx()
pad1.Draw()
pad1.cd()
h1.Draw()
h2.Draw("same")
# to avoid clipping the bottom zero, redraw a small axis
h1.GetYaxis().SetLabelSize(0.0)
axis = TGaxis(-5, 20, -5, 220, 20, 220, 510, "")
axis.SetLabelFont(43)
axis.SetLabelSize(15)
axis.Draw()

# Lower ratio plot is pad2
c.cd()  # returns to main canvas before defining pad2
pad2 = TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
pad2.SetTopMargin(0)  # joins upper and lower plot
pad2.SetBottomMargin(0.2)
pad2.SetGridx()
pad2.Draw()
 

# create required parts
# draw everything
# pad1.cd()
# h1.Draw()
# h2.Draw("same")
# # to avoid clipping the bottom zero, redraw a small axis
# h1.GetYaxis().SetLabelSize(0.0)
# axis = TGaxis(-5, 20, -5, 220, 20, 220, 510, "")
# axis.SetLabelFont(43)
# axis.SetLabelSize(15)
# axis.Draw()

pad2.cd()
h3.Draw("ep")

c.Update()

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
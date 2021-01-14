#include "TCanvas.h"
#include "TRandom3.h"
#include "TGraph.h"
#include "TMath.h"
#include "TArc.h"
#include "cmath"
void graph() {
  const Double_t mumass    = 105.6583715; // muon mass [MeV]
  const Double_t emass     = 0.510998928; // electron mass [MeV]
  const Double_t E_max_mrf = mumass/2.0;  // maximum positron energy from muon decay in muon-rest-frame (MRF)

  // Experimental parameters at J-PARC
  const Double_t mumom     = 300.0; // muon beam momentum [MeV]
  const Double_t beta      = mumom/sqrt( pow(mumom,2)+pow(mumass,2) );  // muon beam velocity (~ 0.9432)
  const Double_t Gamma     = sqrt( pow(mumom,2)+pow(mumass,2) )/mumass; // ~ 3.0103

  const Double_t gammatau  = Gamma*2.1969811; // [us]
  const Double_t E_max_lab = Gamma*0.5*mumass*(1+beta); // maximum positron energy from muon decay in lab-frame [MeV] (~ 309.031 MeV)
  //const Double_t E_max_lab = gamma*mumass; // (obsolete), used in TDR

  const Double_t omega_a   = 2.0*TMath::Pi()/2.111;

  const double N0 = 100000000.; //number of muons
  const double tW = 5e-9; //ASIC time window
  const double A = 0.42 *0.5; // Asymmetry
  
  const int nB = 6000;
  double tWa[nB];
  double ne[nB];
  
  for (int i =0; i < nB; i++)
  { 
    tWa[i] = tW * i;
  }
  
  for (int j =0; j < nB-1; j++)
  {
    double nEt1= N0 * exp ( -tWa[j] / (gammatau*1e-6) )  - N0 * exp ( -tWa[j+1] / (gammatau*1e-6) );
    double nEt2= N0 * exp ( -tWa[j] / (gammatau*1e-6) ) * ( 1 + A * cos(omega_a * tWa[j]))  - N0 * exp ( -tWa[j+1] / (gammatau*1e-6) )* ( 1 + A * cos(omega_a * tWa[j+1])) ;
       
    double nEt = nEt1 - nEt2;
    
    ne[j] = ceil(nEt2);
    //ne[j] = nEt;
    
    cout << ceil(ne[0]) << endl;
  }
  
  //double ne = N0 * exp ( -tW / (gammatau*1e+6) ) * (1-A * TMath::Cos(omega_a * tW));
  //double ne = N0 * exp ( -tW / (gammatau*1e-6) )  - N0 * exp ( -tW / (gammatau*1e-6) );

  //cout << ne << endl; 
  TGraph *gr = new TGraph(nB,tWa,ne);

    TCanvas *c1 = new TCanvas("c1"," time window vs pileup number",200,10,700,500);
    gr->SetLineColor(2);
    gr->SetMarkerColor(2);
    gr->SetMarkerStyle(20);
    gr->SetTitle("time window vs pileup number");
    gr->GetXaxis()->SetTitle("s");
    gr->GetYaxis()->SetTitle("#of piled up e+");
    gr->Draw("AP");

}

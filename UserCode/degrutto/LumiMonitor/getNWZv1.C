#ifndef __CINT__
#include <TROOT.h>
#include <Rtypes.h>
#include <TString.h>
#endif



#include "TSystem.h"
#include <stdlib.h>
#include <stdio.h>
#include "TFile.h"
#ifdef __CINT__
  /// usage getNWZ file.root run

void getNWZv1(){

  std::cout << "ciao " << std::endl;
  const char *file = gSystem->Getenv("filenamev1");
  const char *run = gSystem->Getenv("run");

  std::cout << "file " << file << std::endl;
  std::cout << "run " << run << std::endl;

  TFile * root_file = new TFile(file, "read");

  
  // 
std::cout << "ciao " << std::endl; 
 std::string dirW = "/DQMData/Run " + string(run) + "/Physics/Run summary/EwkMuLumiMonitorDQM/TMASS"; 
 std::cout << "dirW " <<  dirW << std::endl; 
  TH1D * histoW = root_file->Get(dirW.c_str());
   std::cout << "N of W [50-200] v1== " << histoW->Integral(50,200) << endl;
//return 0;



  

}

 



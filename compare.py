import ROOT

fNo = ROOT.TFile.Open("nTupleNo.root")
trNo = fNo.Get("Dstar")

fYes = ROOT.TFile.Open("nTuple.root")
trYes = fYes.Get("Dstar")

hNo  = ROOT.TH1D("hNo", "", 30, 0.135, 0.15)
hYes = ROOT.TH1D("hYes", "", 30, 0.135, 0.15)

trNo.Draw("mDstar -mD >> hNo", "mDstar -mD < 0.155", "goff")
trYes.Draw("mDstar -mD >> hYes", "mDstar -mD < 0.155", "goff")

hNo.Draw()
hNo.Print("all")
hYes.SetLineColor(2)
hYes.Draw("same")
hYes.Print("all")

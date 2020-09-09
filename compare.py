import ROOT

fNo = ROOT.TFile.Open("nTupleNo.root")
trNo = fNo.Get("Dstar")

fYes = ROOT.TFile.Open("nTupleYes.root")
trYes = fYes.Get("Dstar")

hNo  = ROOT.TH1D("hNo", "", 200, 0.143, 0.148)
hYes = ROOT.TH1D("hYes", "", 200, 0.143, 0.148)

trNo.Draw("mDstar -mD >> hNo", "mDstar -mD < 0.150", "goff")
trYes.Draw("mDstar -mD >> hYes", "mDstar -mD < 0.150", "goff")

c = ROOT.TCanvas('c','')

hYes.SetLineColor(2)
hYes.Draw("hist e")
hYes.Print("all")
hNo.Draw("hist e same")

c.SaveAs('plot.pdf')

import ROOT
from ROOT import Belle2
beam_spot = Belle2.BeamSpot()

ip  = ROOT.TVector3(-490e-4, 170e-4, -250e-4)
ipC = ROOT.TMatrixDSym(3)
ipC[0,0] = (0.3e-4)**2
ipC[1,1] = (0.3e-4)**2
ipC[2,2] = (4e-4)**2


cov = ROOT.TMatrixDSym(3)
cov[0,0] = (10e-4)**2
cov[1,1] = (2e-4)**2
cov[2,2] = (250e-4)**2

beam_spot.setIP(ip, ipC)
beam_spot.setSizeCovMatrix(cov)

iov = Belle2.IntervalOfValidity(0,0,-1,-1)
Belle2.Database.Instance().storeData("BeamSpot", beam_spot, iov)

#!/usr/bin/env python3

######################################################
#
# Stuck? Ask for help at questions.belle2.org
#
# e+e- -> ccbar -> D*+ antyhing event generation
#
# This tutorial demonstrates how to generate
#
# e+e- -> ccbar -> D*+ anything
#
# events with EvtGen in BASF2, where the decay of D*+
# is specified by the given .dec file.
#
# The generated events are saved to the output ROOT file.
# In each event the generated particles (MCParticle objects)
# are stored in the StoreArray<MCParticle>.
#
# Contributors: A. Zupanc (June 2014)
#               U. Tamponi (October 2019)
#
######################################################

import basf2 as b2
import modularAnalysis as ma
import simulation as si
import reconstruction as re
import generators as ge


from beamparameters import add_beamparameters

b2.logging.log_level = b2.LogLevel.INFO


# Defining one path
my_path = b2.create_path()




# generation of 100 events according to the specified DECAY table
# e+e- -> ccbar -> D*+ anthing
# D*+ -> D0 pi+; D0 -> K- pi+
#


#Constraining BeamSpot
beamparameters = add_beamparameters(my_path, "Y4S")

def Sqr(x):
  return x*x if x >= 0 else -x*x

# In [um]
vtxPos = [-490,  170, -250]
#          xx      ,  xy   ,   xz    ,     yy  ,   yz,       zz
covMat = [10.,        0,      0,          0.2,      0,        250]


vtxPos = [x*1e-4 for x in vtxPos]
covMat = [Sqr(x*1e-4) for x in covMat]

beamparameters.param("covVertex", covMat)
beamparameters.param("vertex", vtxPos)


ma.setupEventInfo(100, path=my_path)
ge.add_inclusive_continuum_generator(finalstate="ccbar",
                                     particles=["D*+"],
                                     userdecfile=b2.find_file('ccbar.dec'),
                                     path=my_path)


# simulation
si.add_simulation(path=my_path)

# reconstruction
re.add_reconstruction(path=my_path)



re.add_mdst_output(mc=True, filename='ccbarGenerated.root', path=my_path)


# print event numbers
my_path.add_module('EventInfoPrinter')

# Process the events
b2.process(my_path)

# print out the summary
print(b2.statistics)

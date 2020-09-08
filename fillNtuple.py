#!/usr/bin/env python3

input_file = 'ccbarGenerated.root'

import basf2 as b2
import modularAnalysis as ma
import variables.collections as vc
import vertex as vx

#b2.logging.log_level = b2.LogLevel.WARNING

path = b2.create_path()
ma.inputMdstList("default", [input_file], path=path)

# Book charged Kaons and Pions
from stdCharged import stdK, stdPi
stdK("higheff",  path=path)
stdPi("higheff", path=path)

# Reconstruct D0 decay
ma.reconstructDecay('D0:my -> K-:higheff pi+:higheff', cut='1.75 < M < 1.95', path=path)

# Reconstruct D* decay
ma.reconstructDecay('D*+:my -> D0:my pi+:higheff', cut='1.90 < M < 2.25' , path=path)

# Fit vertex
vx.treeFit('D*+:my', conf_level=0, path=path)

#ma.printList('D0:my', True, path=path)
#ma.printVariableValues('D0:my', ['M', 'p'], path=path)

ma.printMCParticles(path=path)


from variables import variables as vm

vm.addAlias('xDstar',  'x')
vm.addAlias('yDstar',  'y')
vm.addAlias('zDstar',  'z')

vm.addAlias('xGenDstar',  'mcProductionVertexX')
vm.addAlias('yGenDstar',  'mcProductionVertexY')
vm.addAlias('zGenDstar',  'mcProductionVertexZ')

vm.addAlias('dxDstar',  'dx')
vm.addAlias('dyDstar',  'dy')
vm.addAlias('dzDstar',  'dz')

vm.addAlias('pDstar',  'p')
vm.addAlias('eDstar',  'E')
vm.addAlias('eCmsDstar',  'useCMSFrame(E)')
vm.addAlias('mDstar',  'M')
vm.addAlias('mD', 'daughter(0,M)')
vm.addAlias('slowPiID', 'daughter(1,pionID)')


Vars = [ 'xDstar',  'yDstar',  'zDstar',  'xGenDstar', 'yGenDstar', 'zGenDstar', 'dxDstar', 'dyDstar', 'dzDstar', 'pDstar',  'eDstar',  'eCmsDstar', 'mDstar',  'mD', 'slowPiID']
Vars.append('isSignal')



# Match to the MC truth information
ma.matchMCTruth('D*+:my', path=path)


ma.variablesToNtuple('D*+:my', Vars, 
                     filename='nTuple.root', treename="Dstar", path=path)


b2.process(path, max_event=1000)
print(b2.statistics)
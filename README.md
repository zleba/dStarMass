# dStarMass
Repository to test effect of the beam spot constraint on the reconstructed dStarMass

## Running the MC event generation
Init the basf2 environment:
``
. ./init.sh
``

Then generate the Dstar events in the e+e- collisions:
``
./ccGenerate.py
``


## Filling the nTuples
Call
``
./fillNtuple.py
``
to fill the root file with interesting variables to analyze

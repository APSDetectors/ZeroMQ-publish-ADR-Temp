# ZeroMQ-publish-ADR-Temp

A simple example how to use zeroMQ (publish/subscribe).

* zeroMQ-publish-ADR-50mK.vi is a simple LabView VI which reads the 50mK temperature NI SharedVariable from the StarCryo ADR magnet controller (on a HPD Denali 102 Cryostat) and publishes is on a zeroMQ socket. The practical reason for this was that we wanted to access the ADR temperature from the linux machine. This was easier than trying to figure out how to directly read NI SharedVariables from linux.

* zeroMQ-subscribe-multipart.vi is just a zeroMQ subscriber which reads the published temperature

* test-zmq-labview-ADR.py is a python script which can run on any other machine (e.g., a linux machine) to read the zmq published temperature. 

## Installation Notes
* Requires zeroMQ LabView binding (via JKI VI Package Manager). 
* ZeroMQ Socket Library v3.4.1.107 by Martijn Jasperse (http://zeromq.org/bindings:labview)
* Obviously the StarCryo ADR controller system!



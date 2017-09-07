#!/APSshare/anaconda/x86_64/bin/python
import sys
import zmq
import time

port = "5555"

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

#denali2.xray.aps.anl.gov: 164.54.101.7
socket.connect ("tcp://164.54.101.7:%s" % port)

socket.setsockopt(zmq.SUBSCRIBE, "")

while(1):
    message = socket.recv()
    print "ADR 50mK temp: %s K" % message
    time.sleep(1)


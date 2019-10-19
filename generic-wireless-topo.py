##!/usr/bin/python

import time
from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import OVSKernelAP
from mn_wifi.cli import CLI_wifi
from mn_wifi.devices import GetTxPower
from mn_wifi.link import wmediumd
from mn_wifi.propagationModels import propagationModel


def topology():

    print("Welcome to mininet-Wifi")
    net = Mininet_wifi(controller = Controller, link=wmediumd, accessPoint =OVSKernelAP,allAutoAssociation=True,fading_coefficient=3)

    info("*** Creating nodes\n")
    ap1 = net.addAccessPoint('ap1', ssid= 'iGrid-ap1', mode = 'g', channel = '1',
    model='DI524', position = '10,30,0', range = '20')
    ap2 = net.addAccessPoint('ap2', ssid= 'iGrid-ap2', mode = 'g', channel = '6',
    model='DI524',position = '40,30,0', range = '20')
    sta1 = net.addStation('sta1', mac = '00:00:00:00:00:01', ip = '10.0.0.1/8',
    antennaHeight='1', antennaGain='5',position = '10,20,0',active_scan=1,scan_freq="2412 2437 2462")
    sta2 = net.addStation('sta2', mac = '00:00:00:00:00:02', ip = '10.0.0.2/8',
    antennaHeight='1', antennaGain='5',position = '28,30,0',active_scan=1,scan_freq="2412 2437 2462")
    sta3 = net.addStation('sta3', mac = '00:00:00:00:00:03', ip = '10.0.0.3/8',
    antennaHeight='1', antennaGain='5',  position = '10,40,0',active_scan=1,scan_freq="2412 2437 2462")
    sta4 = net.addStation('sta4', mac = '00:00:00:00:00:04', ip = '10.0.0.4/8',
    antennaHeight='1', antennaGain='5',  position = '50,40,0', active_scan=1,scan_freq="2412 2437 2462")
    cl = net.addController('cl', controller=Controller)

    #Takes 5 minutes before to proceed
    #time.sleep(40)
    net.setPropagationModel(model="longDistance", exp=4)



    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()
    
    #time.sleep(90)

    net.plotGraph(max_x=60, max_y=60)

    info("*** Enabling Association control (AP)\n")
    
    net.setAssociationCtrl(ac='ssf')
    net.auto_association()


    info("*** Creating links and associations\n")
    net.addLink(ap1, ap2)
    #net.addLink(ap1, sta1)
    #net.addLink(ap2, sta2)
    #net.addLink(ap1,sta3)
    #net.addLink(ap2,sta4)

    info("*** Starting network\n")
    net.build()
    cl.start()
    ap1.start([cl])
    ap2.start([cl])

    info("*** Running CLI\n")
    CLI_wifi(net)
    


    info("*** Stopping the network \n")
    net.stop()

#setLogLevel('info')
#topology()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
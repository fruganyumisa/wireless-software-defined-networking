##!/usr/bin/python

from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import OVSKernelAP
from mn_wifi.cli import CLI_wifi


def topology():

    print("Welcome to mininet-Wifi")
    net = Mininet_wifi(controller = Controller, accessPoint =OVSKernelAP)

    info("*** Creating nodes\n")
    ap1 = net.addAccessPoint('ap1', ssid= 'iGrid-ap1', mode = 'g', channel = '1',
    position = '10,30,0', range = '20')
    ap2 = net.addAccessPoint('ap2', ssid= 'iGrid-ap2', mode = 'g', channel = '6',
    position = '50,30,0', range = '20')
    sta1 = net.addStation('sta1', mac = '00:00:00:00:00:01', ip = '10.0.0.1/8',
    position = '10,20,0')
    sta2 = net.addStation('sta2', mac = '00:00:00:00:00:02', ip = '10.0.0.2/8',
    position = '50,20,0')
    sta3 = net.addStation('sta3', mac = '00:00:00:00:00:03', ip = '10.0.0.3/8',
    position = '10,40,0')
    sta4 = net.addStation('sta4', mac = '00:00:00:00:00:04', ip = '10.0.0.4/8',
    position = '50,40,0')
    cl = net.addController('cl', controller=Controller)


    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    net.plotGraph(max_x=60, max_y=60)

    info("*** Enabling Association control (AP)\n")
    net.setAssociationCtrl('ssf')


    info("*** Creating links and associations")
    net.addLink(ap1, ap2)
    net.addLink(ap1, sta1)
    net.addLink(ap2, sta2)
    net.addLink(ap1,sta3)
    net.addLink(ap2,sta4)

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
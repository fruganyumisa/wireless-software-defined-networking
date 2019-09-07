#!/usr/bin/python3

from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import OVSKernelAP
from mn_wifi.cli import CLI_wifi


def topology():
    net = Mininet_wifi (controller= Controller, accessPoint=OVSKernelAP)
    info("*** Creating nodes \n")
    h1 = net.addHost('h1', mac= '00:00:00:00:00:01', ip = '10.0.0.1/8')
    sta1 = net.addStation('sta1', mac = '00:00:00:00:00:02', ip = '10.0.0.2/8')
    sta2 = net.addStation('sta2', mac = '00:00:00:00:00:05', ip = '10.0.0.5/8')
    sta3 = net.addStation('sta3', mac = '00:00:00:00:00:06', ip = '10.0.0.6/8')
    sta4 = net.addStation('sta4', mac = '00:00:00:00:00:07', ip = '10.0.0.7/8')
    sta5 = net.addStation('sta5', mac = '00:00:00:00:00:08', ip = '10.0.0.8/8')
    sta6 = net.addStation('sta6', mac = '00:00:00:00:00:09', ip = '10.0.0.9/8')

    ap1 = net.addAccessPoint('ap1', ssid = 'iGrid-Ap1', mode = 'g', channel = '1',
    position = '30,50,0', range = '30')
    ap2 = net.addAccessPoint('ap2', ssid = 'iGrid-Ap2', mode = 'g', channel = '2',
    position = '60,50,0', range = '30')
    ap3 = net.addAccessPoint('ap3', ssid = 'iGrid-Ap3', mode = 'g', channel = '3',
    position = '90,50,0', range = '30')
    # ap4 = net.addAccessPoint('ap3', ssid = 'iGrid-Ap3', mode = 'g', channel = '1',
    # position = '120,50,0', range = '30')
    # ap5 = net.addAccessPoint('ap3', ssid = 'iGrid-Ap3', mode = 'g', channel = '1',
    # position = '150,50,0', range = '30')
    # ap6 = net.addAccessPoint('ap3', ssid = 'iGrid-Ap3', mode = 'g', channel = '1',
    # position = '180,50,0', range = '30')
    cl = net.addController('cl', controller = Controller)

    info("*** Configuring wifi nodes \n")
    net.configureWifiNodes()

    info("*** Associating and Creating links \n")
    net.addLink(ap1, h1)
    net.addLink(ap1, ap2)
    net.addLink(ap2, ap3)

    net.plotGraph(max_x = 250, max_y = 250)

    #net.controllAssociation
    net.startMobility(time = 0, AC = 'ssf')
    net.mobility(sta1, 'start', time = 0, position = '1,50,0')
    net.mobility(sta1, 'stop', time = 79, position = '159,50,0')
    net.stopMobility(time = 80)


    info("*** Starting the network \n")
    net.build()
    cl.start()
    ap1.start([cl])
    ap2.start([cl])
    ap3.start([cl])
  


    info("*** Running CLI\n")
    CLI_wifi(net)
    


    info("**** Stopping the network \n")
    net.stop()



if __name__ == '__main__':
    setLogLevel('info')
    topology()
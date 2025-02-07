#!/usr/bin/python

"""
This example shows how to create a network and run multiple tests.
For a more complicated test example, see udpbwtest.py.
"""

from mininet.cli import CLI
from mininet.log import info, output
from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo

def ifconfigTest( net ):
    "Run ifconfig on all hosts in net."
    hosts = net.hosts
    for host in hosts:
        output(host.cmd( 'ifconfig' ))

if __name__ == '__main__':
    info( "*** Creating network\n" )
    #network = Mininet( TreeTopo( depth=2, fanout=2 ), ipBase= "100.0.0.0/24")
     #                 , switch=OVSKernelSwitch )
    network = Mininet( SingleSwitchTopo())
    info( "*** Starting network\n" )
    network.start()
    info( "*** Running ping test\n" )
    network.pingAll()
    network.iperf()
    info( "*** Running ifconfig test\n" )
   #ifconfigTest( network )
    info( "*** Starting CLI (type 'exit' to exit)\n" )
    CLI( network )
    info( "*** Stopping network\n" )
    network.stop()

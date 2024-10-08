#example use: python3 macChanger.py -i eth0 -m 00:11:11:11:11:11
#note: when i write this code i use wsl kali linux command line, if change_mac_adress function dont run edit 18 to 20 rows for your OS.

import subprocess
import optparse
import re

def get_user_input():
    
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="a interface what you want to change")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="write a new mac adress")
    
    return parse_object.parse_args()

def change_mac_adress(user_interface, user_mac_adress):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_adress])
    subprocess.call(["ifconfig", user_interface, "up"])
    
def control_new_mac(interface):
    
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    
    if new_mac:
        return new_mac.group(0)
    else:
        return None
    

print("Mac Changer started!")
(user_input, arguments) = get_user_input()
change_mac_adress(user_input.interface, user_input.mac_address)

finalized_mac = control_new_mac(user_input.interface)

if finalized_mac == user_input.mac_address:
    print("Success!")
else:
    print("Fail!")
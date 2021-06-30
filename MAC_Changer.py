#!/use/vin/env python3
import subprocess
import optparse
import pyfiglet


def welcome():
    subprocess.call("clear", shell=True)
    welcome = pyfiglet.figlet_format("Li0N H4cKeR")
    print(welcome+"INSTA : @0xH4cKeR\n")

def get_arg():
    pa = optparse.OptionParser()
    pa.add_option("-i", "--interface", dest="interface", help="InterFace to change its MAC Address")
    pa.add_option("-m", "--macaddress", dest="newmac", help="New MAC Address")
    return pa.parse_args()

def textin(interface, mac):
    print("\n[+] Changing MAC Address for " + interface + " to " + mac)

def change_addr(interface, new_mac):
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)
welcome()
(options, arguments) = get_arg()
textin(options.interface, options.newmac)
change_addr(options.interface, options.newmac)

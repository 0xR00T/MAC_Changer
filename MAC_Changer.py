#!/use/vin/env python3
import subprocess
import optparse
import pyfiglet

subprocess.call("clear", shell=True)
welcome = pyfiglet.figlet_format("Li0N H4cKeR")
print(welcome+"INSTA : @0xH4cKeR\n")
pa = optparse.OptionParser()
pa.add_option("-i", "--interface", dest="interface", help="InterFace to change its MAC Address")
pa.add_option("-m", "--macaddress", dest="newmac", help="New MAC Address")
(options, arguments) = pa.parse_args()
print("\n[+] MAC Address changer\n")
interface = options.interface
new_mac = options.newmac
print("[+] Changing MAC Address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

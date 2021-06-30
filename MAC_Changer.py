#!/use/vin/env python3
import subprocess
import optparse
import pyfiglet


def welcome():
    print("""

██╗     ██╗ ██████╗ ███╗   ██╗    ██╗  ██╗██╗  ██╗ ██████╗██╗  ██╗███████╗██████╗ 
██║     ██║██╔═████╗████╗  ██║    ██║  ██║██║  ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║     ██║██║██╔██║██╔██╗ ██║    ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
██║     ██║████╔╝██║██║╚██╗██║    ██╔══██║╚════██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████╗██║╚██████╔╝██║ ╚████║    ██║  ██║     ██║╚██████╗██║  ██╗███████╗██║  ██║
╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
            INSTA : @0xH4cKeR     GitHub : 0xR00T                     \n""")

def get_arg():
    pa = optparse.OptionParser()
    pa.add_option("-i", "--interface", dest="interface", help="InterFace to change its MAC Address")
    pa.add_option("-m", "--macaddress", dest="newmac", help="New MAC Address")
    (options, arguments) = pa.parse_args()
    if not options.interface:
        welcome()
        print("[-] Please use --help or -h for more info\n")
        exit()
    elif not options.newmac:
        welcome()
        print("[-] Please use --help or -h for more info\n")
        exit()
    return options

def textin(interface, mac):
    print("\n[+] Changing MAC Address for " + interface + " to " + mac)

def change_addr(interface, new_mac):
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)

    
options = get_arg()
subprocess.call("clear", shell=True)
welcome()
textin(options.interface, options.newmac)
change_addr(options.interface, options.newmac)

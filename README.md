# MAC_Changer

How to use MAC Changer
root@kali~# cd MAC_Changer/

root@kali~/MAC_Changer # git clone https://github.com/0xR00T/MAC_Changer.git

root@kali~/MAC_Changer # pip3 install -r requirements.txt

root@kali~/MAC_Changer # sudo python3 MAC_Changer.py -h
                                                        
INSTA : @0xH4cKeR

Usage: MAC_Changer.py [options]

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        InterFace to change its MAC Address
  -m NEWMAC, --macaddress=NEWMAC
                        New MAC Address
                                     
root@kali~/MAC_Changer # sudo python3 MAC_Changer.py -i eth0 -m 00:11:22:33:44:55
                                                        
INSTA : @0xH4cKeR


[+] MAC Address changer

[+] Changing MAC Address for eth0 to 00:11:22:33:44:55

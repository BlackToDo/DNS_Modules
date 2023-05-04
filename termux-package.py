#!/usr/bin/python3
import os
import time
import sys

os.system("clear")

print('''\033[91m
    _____ ___ ___ __  __ _   ___  __  ___  _   ___ _  __   _   ___ ___ 
  |_   _| __| _ \  \/  | | | \ \/ / | _ \/_\ / __| |/ /  /_\ / __| __|
    | | | _||   / |\/| | |_| |>  <  |  _/ _ \ (__| ' <  / _ \ (_ | _| 
    |_| |___|_|_\_|  |_|\___//_/\_\ |_|/_/ \_\___|_|\_\/_/ \_\___|___|                                                                       
                                                                                                                                                                                                                              
CREATED BY NITRO HACKER
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

print (''' \033[95m
+--------------------------------------+
| This Tool Install All Basic Packages |
+--------------------------------------+
| Coded By Nitro Hacker|version : 2.3  |
+--------------------------------------+''')

slowprint(''' \033[93m
[01] pkg install avahi
[02] pkg install c-ares
[03] pkg install dns2tcp
[04] pkg install dnslookup
[05] pkg install dnsmap
[06] pkg install dnsmasq
[07] pkg install dnstop
[08] pkg install dnsutils
[09] pkg install dnsutils-static
[10] pkg install dog
[11] pkg install hash-slinger
[12] pkg install haskell-resolv
[13] pkg install iodine
[14] pkg install knot-utils
[15] pkg install ldns
[16] pkg install ldns-static
[17] pkg install libdns-sd
[18] pkg install libdns-sd-static
[19] pkg install libknot
[20] pkg install libresolv-wrapper
[21] pkg install mdns-scan''')
slowprint('''\033[96m
This Command for access Storage in Termux
[00] termux-setup-storage''')
print ("                                            ")
choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("pkg update")
os.system ("pkg upgrade -y")
os.system ("pkg install avahi")
os.system ("pkg install c-ares")
os.system ("pkg install dns2tcp")
os.system ("pkg install dnslookup")
os.system ("pkg install dnsmap")
os.system ("pkg install dnstop")
os.system ("pkg install dnsutils")
os.system ("pkg install dnsutils-static")
os.system ("pkg install dog")

os.system ("termux-setup-storage")
  
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
print("\033[95m+-------------------------------------------------+")
slowprint('''\033[95m|             Welcome To NITRO HACKER           |
|           Subscribe Our YouTube Channel         |
| Watch Ours Tutorials For Learn Ethical Hacking  |''')
print("+-------------------------------------------------+")


input("\n\nPress the enter key to exit : ")

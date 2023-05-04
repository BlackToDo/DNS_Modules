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
| This Tool Install DNS MODULES |
+--------------------------------------+
| Coded By Avishka Dulara|version : 1.0  |
+--------------------------------------+''')

slowprint(''' \033[93m
+-------------1st Bulk--------------------+
[01] pkg install avahi
[02] pkg install c-ares
[03] pkg install dns2tcp
[04] pkg install dnslookup
+-------------2nd Bulk--------------------+
[05] pkg install dnsmap
[06] pkg install dnsmasq
[07] pkg install dnstop
[08] pkg install dnsutils
+-------------3rd Bulk--------------------+
[09] pkg install dnsutils-static
[10] pkg install dog
[11] pkg install hash-slinger
[12] pkg install haskell-resolv
[13] pkg install iodine
[14] pkg install knot-utils
+-------------4th Bulk--------------------+
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

print ("Install Finish 1st Bulk")

os.system ("pkg install dnsmap")
os.system ("pkg install dnsmasq")
os.system ("pkg install dnstop")
os.system ("pkg install dnsutils")

print ("Install Finish 2nd Bulk")

os.system ("pkg install dnsutils-static")
os.system ("pkg install dog")
os.system ("pkg install hash-slinger")
os.system ("pkg install haskell-resolv")
os.system ("pkg install iodine")
os.system ("pkg install knot-utils")

print ("Install Finish 3rd Bulk")

os.system ("pkg install ldns")
os.system ("pkg install ldns-static")
os.system ("pkg install libdns-sd")
os.system ("pkg install libdns-sd-static")
os.system ("pkg install libknot")
os.system ("pkg install libresolv-wrapper")
os.system ("pkg install mdns-scan")

print ("Install Finish 4th Bulk")

os.system ("termux-setup-storage")
  
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
print("\033[95m+-------------------------------------------------+")
slowprint('''\033[95m|             Welcome,           |
|           Install Finished         |''')
print("+-------------------------------------------------+")


input("\n\nPress the enter key to exit : ")

#!/usr/bin/env python3
import string
import random
import ipaddress

print('-----------------------------------------')
print('Network Configuration Generator')
print('-----------------------------------------')
deviceType = input('Type: (1) router, (2) switch: ')
deviceHostname = input('Hostname: ')
interfaceSpeed = input('Interface Speed (mbps): ')
if deviceType == '1':
    outsideInt = input('Outside Interface: ')
    outsideIP = input('Outside Interface IP: ')
    outsideMask = input('Outside Mask: ')
    insideInt = input('Inside Interface: ')
    insideIP = input('Inside Interface IP: ')
    insideMask = input('Inside Mask: ')
if deviceType == '2':
    stackMember = input('Stack Member:')
    interfaceQty = input('Interface Count: ')
    managementVlan = input('Management VLAN: ')
    managementNetwork = input('Management Network: ')
    uplinkInterface = input('Uplink Port: ')
    accessInterface = input('Access Ports: ')
    accessVlan = input('Access VLAN: ')
randomPW = input('Random PW? (y/n): ')
print('-----------------------------------------')

#define interface speeds
if interfaceSpeed == '10':
    iface = 'ethernet'
elif interfaceSpeed == '100':
    iface = 'fastethernet'
elif interfaceSpeed == '1000':
    iface = 'gigabit'
elif interfaceSpeed == '10000':
    iface = 'tengigabit'
else:
    print('Error in speed type.')
#define enable password params
randPasswordLength = 16
randPasswordQty = 1

for y in range(randPasswordQty):
    password = ''
    for c in range(randPasswordLength):
        password += random.choice(string.hexdigits)

if deviceType == '1':
    print('Router Configuration')
    print('-------------------------')
    print('enable')
    print('config terminal')
    print('hostname', deviceHostname)
    print('interface', iface, outsideInt)
    print('ip address', outsideIP, outsideMask)
    print('no shutdown')
    print('interface', iface, insideInt)
    print('ip address', insideIP, insideMask)
    print('no shutdown')
    print('line vty 0 15')
    print('password', password)
    print('login')
    print('logging sync')
    print('line con 0')
    if randomPW == 'y':
        print('enable secret', password)
elif deviceType == '2':
    print('Switch Configuration')
    print('-------------------------')
    print('enable')
    print('config terminal')
    print('hostname', deviceHostname)
    if managementVlan == '1':
        print('interface vlan', managementVlan)
        print('ip address', managementNetwork)
    if managementVlan >= '2':
        print('interface vlan 1')
        print('shutdown')
        print('interface vlan', managementVlan)
        print('ip address', managementNetwork)
        print('no shutdown')
        print('vlan', managementVlan)
        print('name Management VLAN')
    print('interface', uplinkInterface)
    print('interface range', iface, stackMember,'/0/',accessInterface)
    print('line vty 0 15')
    print('password', password)
    print('login')
    print('logging sync')
    print('line con 0')
    if randomPW == 'y':
        print('enable secret', password)
else:
    print('Error, not supported.')
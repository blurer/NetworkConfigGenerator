# Network Programmability Tool

Two python programs so far:
* netProgPW.py -> generates a random 16 character password. Not required, but same code is used to generate enable secret passwords in getConf.py.
* genConf.py -> script to generate router or switch base configuration. 

Others:
* routeport.yml -> to be used later
* switchport.yml -> to be used later

Usage:

```
# bl @ bl-mac in ~/Documents/projects/Network-Configuration-Generator on git:master o [21:32:53] 
$ ./netProgPW.py 
d5eafDbA27ff3cC1
```

Router config:

```
# bl @ bl-mac in ~/Documents/projects/Network-Configuration-Generator on git:master x [21:33:43] 
$ ./genConf.py 
-----------------------------------------
Network Configuration Generator
-----------------------------------------
Type: (1) router, (2) switch: 1
Hostname: router_1
Interface Speed (mbps): 1000
Outside Interface: 1/0/1
Outside Interface IP: 11.12.13.14
Outside Mask: 255.255.255.0
Inside Interface: 1/0/2
Inside Interface IP: 10.1.1.1
Inside Mask: 255.255.255.0
Random PW? (y/n): y
-----------------------------------------
Router Configuration
-------------------------
enable
configuration terminal
hostname router_1
interface gigabit 1/0/1
ip address 11.12.13.14 255.255.255.0
no shutdown
interface gigabit 1/0/2
ip address 10.1.1.1 255.255.255.0
no shutdown
line vty 0 15
password A6331De7cfafa6F5
login
logging sync
line con 0
enable secret A6331De7cfafa6F5
```

```
R1#
R1#enable
R1#config terminal
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#hostname router_1
router_1(config)#interface fastethernet 0/0
router_1(config-if)#ip address 11.1.1.1 255.255.255.0
router_1(config-if)#no shutdown
router_1(config-if)#interface fastethernet 0/1
router_1(config-if)#ip address 10.1.1.1 255.255.255.0
router_1(config-if)#no shutdown
router_1(config-if)#line vty 0 15
router_1(config-line)#password 2CbC24f738cD56Ca
router_1(config-line)#login
router_1(config-line)#logging sync
router_1(config-line)#line con 0
router_1(config-line)#enable secret 2CbC24f738cD56Ca
```
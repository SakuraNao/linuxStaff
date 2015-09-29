#archLinux wifi Connection.md

**ip iw wpa_supplicant are needed** 

*wpxxx is your wifi device name*

1. ```ip link``` #check device and mode
2. ````sudo ip link set wpxxx up``` #turn your device on
3. ```iw dev wxxx link``` #check connection
4. ```iw dev wpxxx scan``` #scan the network
5. ```sudo iw dev set type ibss```
6. ```sudo wpa_supplicant -Dnl80211 -iwpxxx -c/etc/wpa_supplicant.conf```
#change wpa_supplicant.conf to your own one, get the base by ```wifi-menu -o``` 
and use those info to revise the example which can be found at /etc/netctl/example
7. ```sudo dhcpcd wpxxx``` #get id address 

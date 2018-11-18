# -*- coding: utf-8 -*-
import pywifi
import time
from pywifi import const

import logging

pywifi.set_loglevel(logging.INFO)

wifi=pywifi.PyWiFi()

iface=wifi.interfaces()[0]

print(iface.name())
iface.scan()  #扫描wifi网络

time.sleep(5)

wifinets=iface.scan_results()
for wifinet in wifinets:
    print(wifinet)
    print(wifinet.bssid)

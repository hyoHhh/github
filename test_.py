# -*- coding: utf-8 -*-
import pywifi
import time
from pywifi import const

import logging

pywifi.set_loglevel(logging.INFO)


def connect():

    wifi = pywifi.PyWiFi()  #初始wifi

    iface = wifi.interfaces()[0]  #激活第一块网卡
    iface.disconnect()  # 断开所有连接
    profile=pywifi.Profile()  #链接wifi，配置文件

    profile.ssid="TP-LINK_FE9A"
    profile.auth=const.AUTH_ALG_OPEN #open公开需要密码
    profile.akm.append(const.AKM_TYPE_WPA2PSK) #默认的加密算法
    profile.cipher=const.CIPHER_TYPE_CCMP #网络链接方式,数据格式ccmp
    profile.key="12345678"
    iface.remove_all_network_profiles()  #清空当前wifi所有的配置
    tmp_profile=iface.add_network_profile(profile)  #设置配置文件
    iface.connect(tmp_profile)
    time.sleep(10)
    isOk=False  #假定链接不上
    if iface.status()==const.IFACE_CONNECTED:
        isOK=True

        print("链接成功")

    else:
        print("失败")

    iface.disconnect() #无论成功和失败，都断开
def disconnet():
    wifi = pywifi.PyWiFi()  #初始wifi

    iface = wifi.interfaces()[0]  #激活第一块网卡
    iface.disconnect()  # 断开所有连接

print(connect())



connect()
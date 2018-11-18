# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from datetime import datetime
try:
    options=webdriver.ChromeOptions()
    options.set_headless()
    # options.add_argument(‘--headless‘)
    options.add_argument('--disable-gpu')
    time.sleep(3)
    driver=webdriver.Chrome(options=options)
    cooki0={'domain': 'www.kxdao.net', 'httpOnly': True, 'name': 'G1NZ_2132_saltkey','path': '/', 'secure': True,'value': 'vwRhDroI'}
    cooki2={'domain': 'www.kxdao.net', 'httpOnly': True, 'name': 'G1NZ_2132_auth','path': '/', 'secure': True,'value': 'a19aJ3I7h51sYEEzxrWDLZuG0Y3AlNxC%2FH7%2FsKfbx%2BFRT%2BRdXLfchEetKRebvn8MkuOz2DzEs26qAB2J2zAJxGwVGQ'}
    driver.get('https://www.kxdao.net')
    driver.add_cookie(cookie_dict=cooki0)
    driver.add_cookie(cookie_dict=cooki2)
    driver.get('https://www.kxdao.net')
    res=driver.find_element_by_css_selector('#pper_a > img')
    res.click()
    driver.close()
    print("执行成功，成功时间{}".format(datetime.now()))
except Exception as e:
    print("执行失败，错误时间{}".format(datetime.now()))







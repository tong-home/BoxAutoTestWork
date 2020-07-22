#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import logging
import logging.config
from appium import webdriver

logging.config.fileConfig(r'D:/Study/PycharmProjects/BoxAutoTestWork/config/log.conf')
logging=logging.getLogger()
# Read mobile os Version
os_version = os.popen('adb shell getprop ro.build.version.release').read()

def appium_start():
    config = {
        'platformName': 'Android',  # 平台
        'platformVersion': os_version,  # 系统版本
        'deviceName': "ZHAIGJ1HTD000009D",  # 测试设备ID
        'appPackage': 'com.jw.audiolauncher',
        'appActivity': 'com.jw.aduiolauncher.view.activity.MainActivity',
        'newCommandTimeout': 30,
       # 'automationName': 'Appium',
        #'unicodeKeyboard': True, # 编码,可解决中文输入问题
        'uiautomationName' : 'uiautomator2',
        'resetKeyboard': True}
    logging.info('run APP')
    driver = webdriver.Remote('http://localhost:4723/wd/hub', config)
    driver.implicitly_wait(5)
    return driver

if __name__ == '__main__':
    appium_start()

"""
{"platformName":"Android","platformVersion":"8.1.0","deviceName":"ZHAIGJ1HTD000009D","appPackage":"com.jw.audiolauncher",
"appActivity":"com.jw.aduiolauncher.view.activity.MainActivity","newCommandTimeout":30,"automationName":"Appium","unicodeKeyboard":true,
"uiautomationName":"uiautomator2","resetKeyboard":true}

"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2020/3/20 16:07
# @Author       : tongmu
# @File         : RunTestCase.py
from time import sleep
import unittest
from config.appium_config import *

class MyTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        logging.info('===setup====')
        self.driver = appium_start()
        sleep(5)
        logging.info("test start")


    def test_calculator(self):
        #ogging.info('start first test')
        #self.driver.find_element_by_id("fragment_serviceProgress").click()
        self.driver.wait_activity("com.jw.aduiolauncher.view.activity.MainActivity", 10)
        act1 = self.driver.find_element_by_id("base_call")
        title = act1.get_attribute("text")
        logging.info("now find is " +title)
        act1.click()
        sleep(5)
        self.driver.save_screenshot("./Screenshots/%s.png" % title)
        #self.driver.find_element_by_id('com.jw.audiolauncher:id/ry_dial_keyboard').send_keys('200001')
        self.driver.ta
        sleep(3)
        self.driver.find_element_by_name('取消').click()
        self.driver.find_element_by_id('com.jw.audiolauncher:id/rl_dial_button')
        self.driver.save_screenshot("./Screenshots/phone.png")
        logging.info('test end')


    @classmethod
    def tearDown(self):
        logging.info('===tearDown====')
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

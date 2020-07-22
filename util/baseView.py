#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/10 16:45
# @Author : Carpe diem
# @File : test.py

class BaseView(object):
    def __init__(self, driver):
        self.driver = driver

    # 寻找元素
    def find_element(self, *args, **kwargs):
        return self.driver.find_element(*args, **kwargs)

    # 寻找元素列表
    def find_elements(self, *args, **kwargs):
        return self.driver.find_elements(*args, **kwargs)

    # 获取屏幕尺寸
    def get_window_size(self):
        return self.driver.get_window_size()

    # 滑动
    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

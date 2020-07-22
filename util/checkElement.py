# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2020/3/20 16:07
# @Author       : tongmu
# @File         : RunTestCase.py

class CheckElement(object):

    @staticmethod
    def is_element_exist(source, element):
        if element in source:
            return True
        else:
            return False

if __name__ == '__main__':
    pass

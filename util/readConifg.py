#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/8 17:02
# @Author : Carpe diem
# @File : readConifg.py

import configparser  # 专门读取配置文件的类


class ReadConfig:
    def read_config(self, conf_file, section, option):
        cf = configparser.ConfigParser()
        cf.read(conf_file, encoding='utf-8')
        # section 片段 option 选项
        value = cf.get(section, option)
        return value


if __name__ == '__main__':
    pass
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/23 14:33
# @Author : Carpe diem
# @File : getExceldata.py

import xlrd
import xlwt
from datetime import date,datetime
arrayNum = 6
tables = []
newTables = []

def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'D:\test.xlsx')
    # 获取所有sheet
    sheet_name = workbook.sheet_names()[0]

    # 根据sheet索引或者名称获取sheet内容
    sheet = workbook.sheet_by_index(0) # sheet索引从0开始
    # sheet = workbook.sheet_by_name('Sheet1')

    #print (workboot.sheets()[0])
    # sheet的名称，行数，列数
    print (sheet.name,sheet.nrows,sheet.ncols)

    # 获取整行和整列的值（数组）
    #rows = sheet.row_values(1) # 获取第2行内容
    cols = sheet.col_values(0) # 获取第3列内容
    print (cols)


    print (len(tables))
    #print (tables)
    #print (tables[5])
if __name__ == '__main__':
    # 读取Excel
    read_excel();
    print ('读取成功')

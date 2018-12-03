# coding=utf-8

import xlrd
import os
from xlutils.copy import copy


def base_dir(filename=None):
    return os.path.join(os.path.dirname(r'C:\Users\Administrator\Desktop\name3.xlsx'), filename)


'''文件操作'''
# work=xlrd.open_workbook(base_dir('name3.xlsx'))
# # sheet=work.sheet_by_index(0)
# sheet=work.sheet_by_name('Sheet1')
#
# #查看多少行
# print(sheet.nrows)
#
# #获取单元格内容(行,列)
# print(sheet.cell_value(4,0))


'''excel文件内容修改'''

work = xlrd.open_workbook(base_dir('name3.xlsx'))
print(work)
old_content = copy(work)
ws = old_content.get_sheet(0)
ws.write(2, 3, '社区')
old_content.save(base_dir('name3.xls'))

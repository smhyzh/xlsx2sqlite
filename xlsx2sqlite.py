#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Author:smh

from openpyxl import load_workbook

from xlsxheader import XlsxHeader


class XlsxToSqlite():
    '''
    '''
    def __init__(self,work_book):
        '''
        '''
        self._wb = work_book

    def convertToSqlite(self,table_label,sqlite_db_path=None):
        '''
        '''
        if table_label not in self._wb.sheetnames:
            raise ValueError('table_label:{} not found.'.format(table_label))
        ws = self._wb[table_label]

        xhdr = XlsxHeader(ws)
        try:
            item_index = xhdr.getTableItems()
        except RuntimeError:
            print('not found table items.\nconvert to sqlite failed!')
        
        items_list = [ item.value for item in xhdr.getLine(item_index)]
        print(items_list)


if __name__ == "__main__":
    test_path = 'test.xlsx'
    wb = load_workbook(test_path)
    test_label = 'Sheet1'
#     ws = wb[test_label]
#     xhdr = XlsxHeader(ws)
#     for index in range(1,10):
#         item_list = xhdr.getLine(index)
#         for item in item_list:
#             print(item.value,end='\t')
#         print('')
#     index = xhdr.getTableItems()
#     print('items:{}'.format(index))
#     item_list = xhdr.getLine(index)
#     for item in item_list:
#         print(item.value,end='\t')
#     print('') 
    myxl = XlsxToSqlite(wb)
    myxl.convertToSqlite(test_label)

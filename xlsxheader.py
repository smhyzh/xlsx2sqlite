#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Author:smh

class XlsxHeader():
    '''Find the table header of a xlsx worksheet.
    1.table header include table title and table items.
    2.table title shoule be a merge cell and length equal with max_column.
    3.table items not include merge cell.
    4.If find a not merge row has the same length with max_column,use it as table items.
    '''
    def __init__(self,work_sheet, forcase_line=10):
        '''
        '''
        self._ws = work_sheet
        if self._ws.max_row < forcase_line:
            self._forcase_row = self._ws.max_row
        else:
            self._forcase_row = forcase_line
        
    def getLine(self,index):
        '''Return the row data specified by Index.
        index:the row position. Start by 1.
        '''
        if index < 0 :
            raise IndexError('index out of range.')
        return self._ws[index]

    def countValidItem(self,line_data):
        '''Count the number of valide item in a row.
        line_data:the data of line,get by getLine().
        '''
        count = 0
        for item in line_data:
            if item.value:
                count+=1
        return count

    def getTableItems(self):
        '''Find the first row which have same length with max_column not merged to be table items.
        '''
        for row in range(1,self._forcase_row+1):
            if self.countValidItem(self.getLine(row)) == self._ws.max_column:
                return row
        raise RuntimeError('Not found the table items.')

#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Author:smh

import sqlite3

class DataBaseOption():
    '''
    We only needs to implement two database operation functions:
    1.create table.
    2.insert a row into database table.
    '''
    def __init__(self,connect):
        self._conn = connect

    def runSQL(self,SQL_String,*args):
        '''Run an SQL statement and commit it .
        '''
        self._conn.execute(SQL_String,*args)
        self._conn.commit()

    def constructHeaderSQL(self,table_name,items_list):
        '''Construct the SQL of items with table items list.
        table_name:the table name of sheet.May be the laeble of sheet.
        items_list:the list of the table items.
        '''
        self._table_name = table_name
        self._items_list = items_list

        SQL_String = ' CREATE TABLE IF NOT EXISTS {} '.format(self._table_name)

        temp_str = '( '
        for item in self._items_list:
            temp_str += ''' {} , '''.format(item)
        temp_str = temp_str[:-2] + ')'
        SQL_String += temp_str
        return SQL_String

    def dropTableSQL(self,table_name):
        '''Drop table from database.
        '''
        SQL_String = ' DROP TABLE {} '.format(table_name)
        return SQL_String
    
    def getCurHeader(self):
        '''We template store the table name and itmes list for recent use.
        '''
        return self._table_name,self._items_list

    def insertRowSQL(self,row_data,table_name=None):
        '''
        '''
        if not table_name:
            table_name = self._table_name
        
        SQL_String = ' INSERT INTO {} VALUES '.format(table_name)
        temp_str = '( ' + ' ? ,'*len(row_data)
        SQL_String += temp_str[:-1]+')'
        return SQL_String


class MyDateBase():
    '''
    '''
    def __init__(self,db_path):
        '''
        '''
        self._db_path = db_path

    def getConnect(self):
        '''Create Connect to database.
        '''
        self._conn = sqlite3.connect(self._db_path)
        self._db_opt = DataBaseOption(self._conn)
        return self._db_opt

    def closeConnect(self):
        '''Close current connect.
        '''
        self._conn.close()


    def __enter__(self):
        #create connect to sqlite.
        return self.getConnect()

    def __exit__(self,*args,**kwargs):
        #close connect.
        self.closeConnect()


if __name__ == "__main__":
    # tdbopt = DataBaseOption(None)
    # sql_str = tdbopt.constructHeaderSQL('test_table',['A','B','C'])
    # print(sql_str)
    # sql_str = tdbopt.insertRowSQL(['A','B','C'])
    # print(sql_str)
    mdbs = MyDateBase('test.db')
    with mdbs as mdb:
        sql_str = mdb.constructHeaderSQL('test_table',['A','B','C','D'])
        print(sql_str)
        mdb.runSQL(sql_str)
        row_data = [1,2,3,4]
        sql_str = mdb.insertRowSQL(row_data)
        print(sql_str)
        mdb.runSQL(sql_str,row_data)
        

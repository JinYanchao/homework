#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  : Jin Yanchao
@Email   : yanchao.jin@outlook.com
@Time    : 2019/5/8 13:29
"""
import os
import json
import pymysql


class Sql(object):

    def sql_connect(self):
        file_path = os.path.join(os.path.abspath('.'), 'database.json')
        if os.path.isfile(file_path):
            with open(file_path, 'r') as load_f:
                load_dicts = json.load(load_f)
                if len(load_dicts) == 5:
                    host = load_dicts['host']
                    user = load_dicts['user']
                    password = load_dicts['password']
                    database = load_dicts['database']
                    port = load_dicts['port']
                    try:
                        db = pymysql.connect(host, user, password, database, port)
                        return db
                    except pymysql.DatabaseError:
                        return

    def ins_data(self, dbsql, values):
        database = self.sql_connect()
        cursor = database.cursor()
        try:
            cursor.execute(dbsql, values)
            database.commit()
        except pymysql.DatabaseError:
            database.rollback()
        database.close()

    def sel_data(self, dbsql):
        database = self.sql_connect()
        cursor = database.cursor()
        try:
            cursor.execute(dbsql)
            results = cursor.fetchall()
            database.close()
            return results
        except pymysql.DatabaseError:
            database.rollback()
        database.close()

    def refresh(self, dbsql):
        database = self.sql_connect()
        cursor = database.cursor()
        try:
            cursor.execute(dbsql)
            database.commit()
        except pymysql.DatabaseError:
            database.rollback()
        database.close()

    def create_table(self):
        database = self.sql_connect()
        cursor = database.cursor()
        dbsql = 'create table if not exists h_email (`id`  int NOT NULL AUTO_INCREMENT ,' \
                '`sender`  varchar(50) NULL ,' \
                '`receiver`  varchar(50) NULL ,' \
                '`subject`  varchar(20) NULL ,' \
                '`context`  varchar(1000) NULL ,' \
                '`p_date`  varchar(20) NULL ,' \
                'PRIMARY KEY (`id`))'
        try:
            cursor.execute(dbsql)
            database.commit()
        except pymysql.DatabaseError:
            database.rollback()
        database.close()

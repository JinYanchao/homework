#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  : Jin Yanchao
@Email   : yanchao.jin@outlook.com
@Time    : 2019/5/7 16:59
"""
from view import home, drafts, inbox
from models import sql

if __name__ == '__main__':
    # sql.create_table() # 创建数据表
    obj_home = home.Home()

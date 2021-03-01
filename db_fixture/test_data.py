#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 18:55
# @Author  : Gavin


from db_fixture.mysql_db import DB
import sys
import time
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# 定义过去时间
past_time = time.strftime(
    "%Y-%m-%d %H:%M:%S",
    time.localtime(
        time.time() -
        100000))
# 定义将来时间
future_time = time.strftime(
    "%Y-%m-%d %H:%M:%S",
    time.localtime(
        time.time() + 10000))

# 创建测试数据
datas = {
    # 登录用户表数据
    'login_user': [
        {'id': 1, 'grant_type': 'xrm', 'username': r'CRM\\Administrator',
            'password': 'p@ssw0Rd@123!'}, {'id': 2, 'grant_type': 'xrm', 'username': 'CRM\\Administrator',
                                           'password': 'p@ssw0R'}
    ]
}

# 测试数据插入表


def init_data():
    DB().init_data(datas)

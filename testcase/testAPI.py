#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/25 18:29
# @Author  : Gavin
'''
1 .测试数据为多个字典的list类型
2.测试类前加修饰@ddt.ddt
3.case前加修饰@ddt.data()
4.运行后用例会自动加载成三个单独的用例
'''

import ddt
import requests
import unittest
from lib.writeexcel import WriteExcel
from lib.sendrequests import SendRequests
from lib.readexcel import ReadExcel
from config import setting
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

testData = ReadExcel(setting.SOURCE_FILE, "Sheet1").read_data()


@ddt.ddt
class Demo_API(unittest.TestCase):
    """CBS登录"""

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    @ddt.data(*testData)
    def test_api(self, data):
        # 获取ID字段数值，截取结尾数字并去掉开头0
        rowNum = int(data['ID'].split("_")[2])
        datas = {
            "grant_type": "xrm",
            "username": r"CRM\Administrator",
            "password": "p@ssw0Rd@123!"
        }
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 "
                          "Safari/537.36"}
        print("******* 正在执行用例 ->{0} *********".format(data['ID']))
        print("请求方式: {0}，请求URL: {1}".format(data['method'], data['url']))
        print("请求参数: {0}".format(data['params']))
        print(
            "post请求body类型为：{0} ,body内容为：{1}".format(
                data['type'],
                data['body']))
        # 发送请求
        #re = SendRequests().sendRequests(self.s, data)
        re=self.s.request(data['method'],
                url=data['url'],
                headers=header,
                params=None,
                data=datas,
                verify=False)
        # 获取服务端返回的值
        #print('=======header============= %s' % data['headers'])
        #print("============%s" % re.text)
        #self.result = re.json()
        self.result = re
        #print("页面返回信息：%s" % re.content.decode("utf-8"))

        # 获取excel表格数据的状态码和消息
        readData_code = int(data["status_code"])
        readData_msg = data["msg"]
        print("=======readData_code={0}=======result['status_code']={1}".format(int(data["status_code"]),int(self.result.status_code)))
        if int(readData_code) == int(self.result.status_code) :
            OK_data = "PASS"
            print("用例测试结果:  {0}---->{1}".format(data['ID'], OK_data))
            WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1, OK_data)
        if int(readData_code) != int(self.result.status_code) :
            NOT_data = "FAIL"
            print("用例测试结果:  {0}---->{1}", format(data['ID'], NOT_data))
            WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1, NOT_data)
        self.assertEqual(
            int(self.result.status_code),
            int(readData_code),
            "返回实际结果是->:%s" %
            int(self.result.status_code))


if __name__ == '__main__':
    unittest.main()

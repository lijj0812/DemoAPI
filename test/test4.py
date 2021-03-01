#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time    : 2021/2/9 10:20
# @Author  : Gavin
import random

tellist = ['186', '187', '188', '189']
tele = random.choice(tellist) + ''.join(random.sample('0123456789', 8))
print(tele)
#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time    : 2021/2/5 16:50
# @Author  : Gavin
import random
import string

i=''.join(random.sample(string.ascii_letters + string.digits, 8))
tele='189'+''.join(random.sample('0123456789',8))
print(tele)
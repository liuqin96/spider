#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 11:14
# @Author  : SmallStrong
# @Des     : 
# @File    : config.py
# @Software: PyCharm

import random

HOST = "https://juejin.im/tag/"
CHROME_DRIVER_PATH = "./driver/chromedriver"  # chromedriver完整路径，path是重点
DELAY = 0.5 + random.random()
NUM_RETRIES = 5
NS = 'juejin'
TAG_HOST = "https://gold-tag-ms.juejin.im/v1/tags/type/new/page/"

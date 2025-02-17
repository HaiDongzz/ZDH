#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 14:07
# @Author  : HD
# @File    : getconf.py
# @Description : 读取config配置


import os
from configparser import ConfigParser

from common.getfiledir import CONFDIR


class Config(ConfigParser):

    def __init__(self):
        self.conf_name = os.path.join(CONFDIR, 'base.ini')
        super().__init__()
        super().read(self.conf_name, encoding='utf-8')

    def save_data(self, section, option, value):
        super().set(section=section, option=option, value=value)
        super().write(fp=open(self.conf_name, 'w'))

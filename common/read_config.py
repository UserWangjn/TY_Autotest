# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 15:15
# @Author  : Rock
# @File    : read_config.py
# @describe: 读取配置文件

import os
import configparser


class ReadIni(object):
    # 构造函数
    def __init__(self, file_name=None, node=None):
        # 获取当前目录的绝对路径
        cur_path = os.path.abspath(__file__)
        # 获取config.ini的绝对路径
        config_path = os.path.join(os.path.abspath(os.path.dirname(cur_path) + os.path.sep + '../config'), 'config.ini')
        if file_name is None:
            file_name = config_path

        if node is None:
            self.node = 'CORE_URL'
        else:
            self.node = node
        # self.conf是load_ini方法返回的ConfigParser配置文件的操作句柄
        self.conf = self.load_ini(file_name)

    # 加载文件
    @staticmethod
    def load_ini(file_name):
        conf = configparser.ConfigParser()
        conf.read(file_name)
        return conf

    # 获取Value值
    def get_value(self, key):
        # self.conf操作句柄.get可以获得入参的配置结果
        data = self.conf.get(self.node, key)
        return data


if __name__ == '__main__':
    # read = ReadIni()
    # read = ReadIni(node='HTTP')
    read = ReadIni(node='CORE_URL')
    # print(read.get_value('base_url'))
    print(read.get_value('current_url'))

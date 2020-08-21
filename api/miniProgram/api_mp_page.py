# coding=utf-8
# @Author: wjn
from config import choice_environment


class MpPage():      # case需修改

    # @property
    def mp_page(self):      # case需修改
        '''小程序打开接口'''
        domain = choice_environment.current_url
        api = '/mp-page'      # case需修改
        url = str(domain) + api
        return url
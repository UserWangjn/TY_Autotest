# coding=utf-8
# @Author: wjn
from config import choice_environment


class MpApp():

    # @property
    def mp_app(self):
        '''小程序打开接口'''
        domain = choice_environment.current_url
        api = '/mp-app'
        url = str(domain) + api
        return url
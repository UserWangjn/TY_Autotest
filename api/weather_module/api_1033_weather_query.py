# coding=utf-8
# @Author: wjn
from config import choice_environment
import datetime
import time


class Api1033WeatherQuery():

    # @property
    def api_weather_query(self):
        '''查询天气接口'''
        domain = choice_environment.current_url
        api = '/simpleWeather/query'
        url = str(domain) + api
        return url
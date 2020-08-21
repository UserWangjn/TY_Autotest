# coding=utf-8
# @Author: wjn
from api.browser.api_browser_action import BrowserAction  # case需修改
from common.util import TYRequest
import unittest
from common.get_value import GetValue
from common.get_log import LogInfo
import json
import time


class TestBrowserActionPf(unittest.TestCase, GetValue, LogInfo):  # case需修改

    @classmethod
    @LogInfo.get_error
    def setUpClass(cls) -> None:
        cls.log.info('TestBrowserActionPf测试用例开始执行')  # case需修改
        api = BrowserAction()  # case需修改
        cls.url = api.browser_action()  # case需修改
        cls.log.info('URL获取成功, URL:' + cls.url)
        cls.request = TYRequest()

    @LogInfo.get_error
    def setUp(self):
        pass

    @LogInfo.get_error
    def test_browser_action_pf(self):  # case需修改
        body = 'c{"optCustomParam":{}}\np{"type":"pf","subType":"","state":"finish","data":{"ns":1594886879075,"f":7,"qs":18,"rs":32,"re":36,"os":3304,"oe":3304,"oi":3304,"oc":3313,"ls":3313,"le":3313,"tus":41,"tue":41,"cs":7,"ce":7,"ds":7,"de":7,"sl":0,"je":0,"sh":1080,"sw":1920,"ressize":true,"fp":262,"__fp":1,"dr":3304,"fs":262,"trflag":"0011","type":"pf","body":{"tr":true,"tt":"Document","charset":"UTF-8","err":[],"res":[{"o":78.54500000030384,"rt":"script","n":"http://apm3brsdev.tingyun.com/js/_SywbofZdkc.js","f":78.54500000030384,"ds":0,"de":0,"cs":0,"ce":0,"sl":0,"qs":0,"rs":0,"re":262.21500000247033,"ts":0,"es":0},{"o":79.01000000128988,"rt":"script","n":"https://cdn.bootcdn.net/ajax/libs/jquery/3.5.1/jquery.min.js","f":79.01000000128988,"ds":79.01000000128988,"de":79.01000000128988,"cs":79.01000000128988,"ce":79.01000000128988,"sl":0,"qs":85.64000000114902,"rs":164.04000000329688,"re":167.57000000143307,"ts":31707,"es":30941},{"o":79.31500000267988,"rt":"script","n":"https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js","f":79.31500000267988,"ds":79.31500000267988,"de":79.31500000267988,"cs":79.31500000267988,"ce":79.31500000267988,"sl":0,"qs":85.8250000019325,"rs":102.98000000329921,"re":104.9700000003213,"ts":5306,"es":4760}],"bizId_param":{},"opt_param":{},"request_param":{}},"state":"finish"}}'  # case需修改
        res = self.request.getInterfaceRes_need_token(url=self.url, body=str(body))
        self.log.debug(res.status_code)
        self.assertEqual(res.status_code, 200, msg='接口返回错误码，code={}'.format(str(res.status_code)))
        self.assertIn('+0800', res.text, msg='接口返回错误信息，code={}'.format(str(res.text)))

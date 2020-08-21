# coding=utf-8
# @Author: wjn
from api.browser.api_browser_action import BrowserAction  # case需修改
from common.util import TYRequest
import unittest
from common.get_value import GetValue
from common.get_log import LogInfo
import json
import time


class TestBrowserActionAjax(unittest.TestCase, GetValue, LogInfo):  # case需修改

    @classmethod
    @LogInfo.get_error
    def setUpClass(cls) -> None:
        cls.log.info('TestBrowserActionAjax测试用例开始执行')  # case需修改
        api = BrowserAction()  # case需修改
        cls.url = api.browser_action()  # case需修改
        cls.log.info('URL获取成功, URL:' + cls.url)
        cls.request = TYRequest()

    @LogInfo.get_error
    def setUp(self):
        pass

    @LogInfo.get_error
    def test_browser_action_ajax_success(self):  # case需修改
        body = 'c{"optCustomParam":{}}\na{"type":"ajax","subType":null,"start":1594277604425,"end":1594277608445,"duration":4020,"data":{"type":"ajax","id":0,"cid":1,"method":"POST","url":"http://localhost:8089/shop/list","state":"finish","ignore":false,"jserror":false,"start":1594277604427,"end":1594277607434,"du":3007,"cb":1000,"status":200,"err":0,"rec":317,"send":14,"bizId_param":{},"opt_param":{},"request_param":{},"opt_custom_param":{},"hasServerHeader":true,"s_id":"DXLxFK1c6us#Mz_EJ2Jjbb4","s_tname":"Transaction/SpringController/shop/list","s_tid":"92ce19fe6f55b9b0","s_rid":"92ce19fe6f55b9b0","s_duration":2565,"startSpeOffset":5,"items":[]}}'
        res = self.request.getInterfaceRes_no_token(url=self.url, body=str(body))
        self.log.debug(res.status_code)
        self.assertEqual(res.status_code, 200, msg='接口返回错误码，code={}'.format(str(res.status_code)))
        self.assertIn('+0800', res.text, msg='接口返回错误信息，code={}'.format(str(res.text)))

    @LogInfo.get_error
    def test_browser_action_ajax_fail(self):  # case需修改
        body = 'c{"optCustomParam":{}}\ne{"type":"event","subType":"click","start":1594952237068,"end":1594952237129,"duration":61,"data":{"type":"event","id":"btn2","nodeName":"BUTTON","className":"","title":"","value":"","text":"send ajax(jQuery)","path":"html > body > button:nth-child(2)#btn2","eventHandlerType":"addEventListener","state":"finish","items":[{"type":"ajax","id":2,"cid":5,"method":"GET","url":"https://reportalpha1.tingyun.com/demo-server/test/custom-request1?timeout=100","state":"finish","ignore":false,"jserror":false,"start":1594952237070,"end":1594952237126,"du":56,"cb":0,"status":403,"err":0,"rec":159,"send":0,"bizId_param":{},"opt_param":{},"request_param":{},"opt_custom_param":{},"hasServerHeader":false,"items":[]}]}}'
        res = self.request.getInterfaceRes_no_token(url=self.url, body=str(body))
        self.log.debug(res.status_code)
        self.assertEqual(res.status_code, 200, msg='接口返回错误码，code={}'.format(str(res.status_code)))
        self.assertIn('+0800', res.text, msg='接口返回错误信息，code={}'.format(str(res.text)))
# coding=utf-8
# @Author: wjn
from api.browser.api_browser_spe import BrowserSpe  # case需修改
from common.util import TYRequest
import unittest
from common.get_value import GetValue
from common.get_log import LogInfo
import random


class TestBrowserSpe(unittest.TestCase, GetValue, LogInfo):  # case需修改

    @classmethod
    @LogInfo.get_error
    def setUpClass(cls) -> None:
        cls.log.info('TestBrowserSpe')  # case需修改
        api = BrowserSpe()  # case需修改
        cls.url = api.browser_spe()  # case需修改
        cls.log.info('URL获取成功, URL:' + cls.url)
        cls.request = TYRequest()

    @LogInfo.get_error
    def setUp(self):
        pass

    @LogInfo.get_error
    def test_browser_spe_success(self):  # case需修改
        opr_name = ['login', 'logout', 'opr_test', 'add_shopping_list', 'pay', 'delete_list']
        body = '{"key":"' + random.choice(
            opr_name) + '","start":1594279331493,"duration":2760,"status":0,"type":"auto","xhrs":[{"type":"ajax","id":1,"cid":3,"method":"get","url":"https://reportalpha1.tingyun.com/demo-server/test/custom-request?timeout=100","ignore":false,"jserror":false,"start":1594279331494,"end":1594279332251,"du":757,"cb":1000,"status":200,"err":0,"rec":12,"send":14,"bizId_param":{},"opt_param":{},"request_param":{},"opt_custom_param":{},"hasServerHeader":false,"startSpeOffset":1}]}'
        res = self.request.getInterfaceRes_no_token(url=self.url, body=str(body))
        self.log.debug(res.status_code)
        self.assertEqual(res.status_code, 200, msg='接口返回错误码，code={}'.format(str(res.status_code)))
        self.assertIn('+0800', res.text, msg='接口返回错误信息，code={}'.format(str(res.text)))

    @LogInfo.get_error
    def test_browser_spe_ajax_fail(self):  # case需修改
        opr_name=['login','logout','opr_test','add_shopping_list','pay','delete_list']
        body = '{"key":"' + random.choice(
            opr_name) + '","start":1594901129944,"duration":1210,"status":0,"type":"auto","xhrs":[{"type":"ajax","id":1,"cid":3,"method":"get","url":"https://reportalpha1.tingyun.com/demo-server/test/custom-request1?timeout=100","ignore":false,"jserror":false,"start":1594901129945,"end":1594901130150,"du":205,"cb":1000,"status":404,"err":0,"rec":159,"send":14,"bizId_param":{},"opt_param":{},"request_param":{},"opt_custom_param":{},"hasServerHeader":false,"startSpeOffset":1}]}'
        res = self.request.getInterfaceRes_no_token(url=self.url, body=str(body))
        self.log.debug(res.status_code)
        self.assertEqual(res.status_code, 200, msg='接口返回错误码，code={}'.format(str(res.status_code)))
        self.assertIn('+0800', res.text, msg='接口返回错误信息，code={}'.format(str(res.text)))

    @LogInfo.get_error
    def test_browser_spe_oprt(self):  # case需修改
        opr_name = ['login', 'logout', 'opr_test', 'add_shopping_list', 'pay', 'delete_list']
        body = '{"key":"' + random.choice(
            opr_name) + '","start":1594951404830,"duration":4023,"status":1,"type":"auto","xhrs":[{"type":"ajax","id":0,"cid":1,"method":"POST","url":"http://localhost:8089/shop/list","ignore":false,"jserror":false,"start":1594951404831,"end":1594951407840,"du":3009,"cb":999,"status":200,"err":0,"rec":317,"send":14,"bizId_param":{},"opt_param":{},"request_param":{},"opt_custom_param":{},"hasServerHeader":false,"startSpeOffset":1}]}'
        res = self.request.getInterfaceRes_no_token(url=self.url, body=str(body))
        self.log.debug(res.status_code)
        self.assertEqual(res.status_code, 200, msg='接口返回错误码，code={}'.format(str(res.status_code)))
        self.assertIn('+0800', res.text, msg='接口返回错误信息，code={}'.format(str(res.text)))

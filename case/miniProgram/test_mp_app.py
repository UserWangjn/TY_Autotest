# coding=utf-8
# @Author: wjn
from api.miniProgram.api_mp_app import MpApp      # case需修改
from common.util import TYRequest
import unittest
from common.get_value import GetValue
from common.get_log import LogInfo
import json
import time


class TestMpApp(unittest.TestCase, GetValue, LogInfo):

    @classmethod
    @LogInfo.get_error
    def setUpClass(cls) -> None:
        cls.log.info('Mp-App测试用例开始执行')
        api = MpApp()      # case需修改
        cls.url = api.mp_app()      # case需修改
        cls.log.info('URL获取成功, URL:' + cls.url)
        cls.request = TYRequest()

    @LogInfo.get_error
    def setUp(self):
        pass

    @LogInfo.get_error
    def test_mp_app_login(self):      # case需修改

        body = {
            "uid": "wjn_user",
            "sid": "16d03f96-f4f6-4eb6-8760-d65ac0fc59fa",
            "v": "1.3.7",
            "at": "wx",
            "networkType": "wifi",
            "system": {
                "model": "Nexus 6",
                "pixelRatio": 3.5,
                "windowWidth": 412,
                "windowHeight": 610,
                "system": "Android 5.0",
                "language": "zh_CN",
                "version": "7.0.4",
                "screenWidth": 412,
                "screenHeight": 732,
                "SDKVersion": "2.11.1",
                "brand": "devtools",
                "fontSizeSetting": 16,
                "benchmarkLevel": 1,
                "batteryLevel": 100,
                "statusBarHeight": 20,
                "safeArea": {
                    "right": 412,
                    "bottom": 732,
                    "left": 0,
                    "top": 20,
                    "width": 412,
                    "height": 712
                },
                "deviceOrientation": "portrait",
                "platform": "devtools",
                "devicePixelRatio": 3.5
            },
            "openPath": "pages/index/index",
            "query": {},
            "scene": 1001,
            "key": "k9Kx3pjmk68",
            "launch": True,  # True登录/False退出
            "launchOptions": {
                "path": "pages/index/index",
                "query": {},
                "scene": 1001,
                "referrerInfo": {}
            }
        }      # case需修改
        headers = {}
        res = self.request.getInterfaceRes_no_token(url=self.url, body=str(body))
        self.log.debug(res.status_code)
        self.assertEqual(res.status_code, 200, msg='接口返回错误码，code={}'.format(str(res.status_code)))
        self.assertIn('+0800', res.text, msg='接口返回错误信息，code={}'.format(str(res.text)))



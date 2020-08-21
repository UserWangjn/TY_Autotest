# coding=utf-8
# @Author: wjn
from api.miniProgram.api_mp_page import MpPage  # case需修改
from common.util import TYRequest
import unittest
from common.get_value import GetValue
from common.get_log import LogInfo
import json
import time


class TestMpPage(unittest.TestCase, GetValue, LogInfo):

    @classmethod
    @LogInfo.get_error
    def setUpClass(cls) -> None:
        cls.log.info('Mp-Page测试用例开始执行')
        api = MpPage()  # case需修改
        cls.url = api.mp_page()  # case需修改
        cls.log.info('URL获取成功, URL:' + cls.url)
        cls.request = TYRequest()

    @LogInfo.get_error
    def setUp(self):
        pass

    @LogInfo.get_error
    def test_mp_page_jserr(self):  # case需修改
        body = {
            "path": "pages/cptest/cptest",
            "pageEvent": {
                "onLoad": 1594693548482,
                "onShow": 1594693548486,
                "onReady": 1594693548504,
                "onHide": 1594693558260
            },
            "errs": [{
                "time": 1594693551445,
                "stack": "thirdScriptError\njserror; [Component] Event Handler Error @ pages/cptest/cptest#(anonymous)\nError: jserror\n    at Ue.triggerJsError (http://127.0.0.1:58224/appservice/pages/cptest/cptest.js:36:13)\n    at Ue.triggerJsError (http://127.0.0.1:58224/appservice/agent/tingyun-mp-agent-private-1.3.7.js:329:13)\n    at Object.r.safeCallback (http://127.0.0.1:58224/appservice/__dev__/WAService.js:2:1698459)\n    at http://127.0.0.1:58224/appservice/__dev__/WAService.js:2:1829230\n    at s (http://127.0.0.1:58224/appservice/__dev__/WAService.js:2:1838577)\n    at http://127.0.0.1:58224/appservice/__dev__/WAService.js:2:1829155\n    at r (http://127.0.0.1:58224/appservice/__dev__/WAService.js:2:1775480)\n    at http://127.0.0.1:58224/appservice/__dev__/WAService.js:2:1775602\n    at http://127.0.0.1:58224/appservice/__dev__/WAService.js:2:834724\n    at o (http://127.0.0.1:58224/appservice/__dev__/asdebug.js:1:28054)"
            }],
            "fromPath": "pages/index/index",
            "actions": [{
                "id": 1,
                "name": "triggerJsError",
                "type": "event",
                "start": 1594693551442,
                "end": 1594693551442,
                "duration": 0,
                "path": "pages/cptest/cptest",
                "prevPath": "pages/index/index",
                "data": {
                    "target": {
                        "offsetLeft": 0,
                        "offsetTop": 265,
                        "id": "",
                        "x": 289,
                        "y": 292
                    },
                    "dataset": {
                        "methodName": "triggerJsError"
                    }
                }
            }],
            "uid": "wjn_user",
            "sid": "99124abb-ac99-4a8c-a749-b7ef4356699c",
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
            "metric": {
                "jsError": True,
                "netError": False,
                "stuck": False,
                "firstLoad": 27
            },
            "setData": {
                "threshold": 1001,
                "setDataTrace": True,
                "setDataTraceHint": True,
                "setDataTimeInterval": [500, 1200],
                "max": 25,
                "requestBridge": [],
                "data": [{
                    "count": 1,
                    "grade": {
                        "good": {
                            "count": 1
                        },
                        "normal": {
                            "count": 0
                        },
                        "bad": {
                            "count": 0
                        }
                    },
                    "traces": [],
                    "timestamp": 1594693548484
                }]
            },
            "routeTrack": [{
                "timestamp": 1594693453576,
                "route": "pages/index/index"
            }, {
                "timestamp": 1594693548486,
                "route": "pages/cptest/cptest"
            }]
        }  # case需修改
        headers = {}
        res = self.request.getInterfaceRes_no_token(url=self.url, body=str(body))
        self.log.debug(res.status_code)
        self.assertEqual(res.status_code, 200, msg='接口返回错误码，code={}'.format(str(res.status_code)))
        self.assertIn('+0800', res.text, msg='接口返回错误信息，code={}'.format(str(res.text)))

    @LogInfo.get_error
    def test_mp_page_request_get(self):  # case需修改
        body = {
            "path": "pages/cptest/cptest",
            "pageEvent": {
                "onLoad": 1594695630141,
                "onShow": 1594695630145,
                "onReady": 1594695630172,
                "onHide": 1594695637853
            },
            "errs": [],
            "fromPath": "pages/index/index",
            "actions": [{
                "id": 1,
                "name": "sendToServer",
                "type": "event",
                "start": 1594695633493,
                "end": 1594695633561,
                "duration": 68,
                "path": "pages/cptest/cptest",
                "prevPath": "pages/index/index",
                "requests": [{
                    "url": "https://reportalpha1.tingyun.com/demo-server/api/index?city=undefined&counts=undefined&start=undefined",
                    "requestId": 1,
                    "recordFirstLoad": False,
                    "type": "request",
                    "method": "GET",
                    "start": 1594695633493,
                    "end": 1594695633556,
                    "cbTime": 0,
                    "duration": 63,
                    "send": 0,
                    "rec": 2558,
                    "statusCode": 200,
                    "failMessage": "",
                    "cid": 2,
                    "custom": {
                        "code": 1,
                        "status": False
                    }
                }, {
                    "url": "https://reportalpha1.tingyun.com/demo-server/api/moviesDetail",
                    "requestId": 2,
                    "recordFirstLoad": False,
                    "type": "request",
                    "method": "GET",
                    "start": 1594695633498,
                    "end": 1594695633561,
                    "cbTime": 0,
                    "duration": 63,
                    "send": 0,
                    "rec": 2951,
                    "statusCode": 200,
                    "failMessage": "",
                    "cid": 3,
                    "custom": {
                        "code": 1,
                        "status": False
                    }
                }],
                "data": {
                    "target": {
                        "offsetLeft": 0,
                        "offsetTop": 311,
                        "id": "sendrequest",
                        "x": 263,
                        "y": 351
                    },
                    "dataset": {
                        "methodName": "sendToServer"
                    }
                }
            }],
            "uid": "wjn_user",
            "sid": "63bcb30c-6923-45e3-bcec-e0cde0fa9517",
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
            "metric": {
                "jsError": False,
                "netError": False,
                "stuck": False,
                "firstLoad": 42
            },
            "setData": {
                "threshold": 1001,
                "setDataTrace": True,
                "setDataTraceHint": True,
                "setDataTimeInterval": [500, 1200],
                "max": 40,
                "requestBridge": [],
                "data": [{
                    "count": 1,
                    "grade": {
                        "good": {
                            "count": 1
                        },
                        "normal": {
                            "count": 0
                        },
                        "bad": {
                            "count": 0
                        }
                    },
                    "traces": [],
                    "timestamp": 1594695630143
                }]
            },
            "reqStat": [{
                "count": 2,
                "timestamp": 1594695633493
            }],
            "routeTrack": [{
                "timestamp": 1594695623886,
                "route": "pages/index/index"
            }, {
                "timestamp": 1594695630145,
                "route": "pages/cptest/cptest"
            }]
        }  # case需修改
        res = self.request.getInterfaceRes_no_token(url=self.url, body=str(body))
        self.log.debug(res.status_code)
        self.assertEqual(res.status_code, 200, msg='接口返回错误码，code={}'.format(str(res.status_code)))
        self.assertIn('+0800', res.text, msg='接口返回错误信息，code={}'.format(str(res.text)))


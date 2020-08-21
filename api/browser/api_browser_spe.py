# coding=utf-8
# @Author: wjn
from config import choice_environment
import random


class BrowserSpe():  # case需修改

    # @property
    def browser_spe(self):  # case需修改
        '''小程序打开接口'''
        queryString = {}
        queryString['pvid'] = '64f1f345-192f-4752-8064-a43846f66db7'  # 每次页面加载生成
        queryString['ref'] = 'http%3A%2F%2F127.0.0.1%3A8080%2Findex_143.html'  # 页面url
        queryString['referrer'] = ''  # document.referrer
        queryString['v'] = '3.1.4'  # 数据协议版本
        queryString['av'] = '3.1.4'  # 探针版本
        queryString['did'] = 'dd33864f-3e95-40f7-992f-30edba5cbbc1'  # 用户id
        queryString['sid'] = '67f76517-a42c-4e73-a7ef-11c8ca8bf529'  # sessionId
        queryString['__s'] = 1594886879348  # 会话开始时间
        queryString['ps'] = 1
        queryString['id'] = 'zm_K-IIie_E'  # 账号id加密值
        queryString['key'] = 'MbVbeLGiVew'  # 应用id加密值，根据实际key进行修改
        queryString['sh'] = 1080  # 屏幕高
        queryString['sw'] = 1920  # 屏幕宽
        queryString['__r'] = 1594886882401  # 上传数据时的时间戳
        domain = choice_environment.current_url
        api = '/spe?pvid={0}&ref={1}&referrer={2}&v={3}&av={4}&did={5}&sid={6}&__s={7}&ps={8}&id={9}&key={10}&sh={11}&sw={12}&__r={13}'.format(
            queryString['pvid'], queryString['ref'], queryString['referrer'], queryString['v'], queryString['av'],
            queryString['did'], queryString['sid'], queryString['__s'], queryString['ps'], queryString['id'],
            queryString['key'], queryString['sh'], queryString['sw'], queryString['__r'])
        url = str(domain) + api
        return url


if __name__ == '__main__':

    opr_name = ['login', 'logout', 'opr_test', 'add_shopping_list', 'pay', 'delete_list']
    body = '{"key":"'+random.choice(opr_name)+'","start":1594279331493,"duration":2760,"status":0,"type":"auto","xhrs":[{"type":"ajax","id":1,"cid":3,"method":"get","url":"https://reportalpha1.tingyun.com/demo-server/test/custom-request?timeout=100","ignore":false,"jserror":false,"start":1594279331494,"end":1594279332251,"du":757,"cb":1000,"status":200,"err":0,"rec":12,"send":14,"bizId_param":{},"opt_param":{},"request_param":{},"opt_custom_param":{},"hasServerHeader":false,"startSpeOffset":1}]}'

    print(body)


# coding=utf-8
# @Author: wjn
from config import choice_environment


class BrowserAction():  # case需修改

    # @property
    def browser_action(self):  # case需修改
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
        api = '/action?pvid={0}&ref={1}&referrer={2}&v={3}&av={4}&did={5}&sid={6}&__s={7}&ps={8}&id={9}&key={10}&sh={11}&sw={12}&__r={13}'.format(
            queryString['pvid'], queryString['ref'], queryString['referrer'], queryString['v'], queryString['av'],
            queryString['did'], queryString['sid'], queryString['__s'], queryString['ps'], queryString['id'],
            queryString['key'], queryString['sh'], queryString['sw'], queryString['__r'])
        url = str(domain) + api
        return url


if __name__ == '__main__':
    brs_handle = BrowserAction()
    brs_api = brs_handle.browser_action()
    print(brs_api)

    body = 'c{"optCustomParam":{}}\np{"type":"pf","subType":"","state":"finish","data":{"ns":1594886879075,"f":7,"qs":18,"rs":32,"re":36,"os":3304,"oe":3304,"oi":3304,"oc":3313,"ls":3313,"le":3313,"tus":41,"tue":41,"cs":7,"ce":7,"ds":7,"de":7,"sl":0,"je":0,"sh":1080,"sw":1920,"ressize":true,"fp":262,"__fp":1,"dr":3304,"fs":262,"trflag":"0011","type":"pf","body":{"tr":true,"tt":"Document","charset":"UTF-8","err":[],"res":[{"o":78.54500000030384,"rt":"script","n":"http://apm3brsdev.tingyun.com/js/_SywbofZdkc.js","f":78.54500000030384,"ds":0,"de":0,"cs":0,"ce":0,"sl":0,"qs":0,"rs":0,"re":262.21500000247033,"ts":0,"es":0},{"o":79.01000000128988,"rt":"script","n":"https://cdn.bootcdn.net/ajax/libs/jquery/3.5.1/jquery.min.js","f":79.01000000128988,"ds":79.01000000128988,"de":79.01000000128988,"cs":79.01000000128988,"ce":79.01000000128988,"sl":0,"qs":85.64000000114902,"rs":164.04000000329688,"re":167.57000000143307,"ts":31707,"es":30941},{"o":79.31500000267988,"rt":"script","n":"https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js","f":79.31500000267988,"ds":79.31500000267988,"de":79.31500000267988,"cs":79.31500000267988,"ce":79.31500000267988,"sl":0,"qs":85.8250000019325,"rs":102.98000000329921,"re":104.9700000003213,"ts":5306,"es":4760}],"bizId_param":{},"opt_param":{},"request_param":{}},"state":"finish"}}'

    print(body)

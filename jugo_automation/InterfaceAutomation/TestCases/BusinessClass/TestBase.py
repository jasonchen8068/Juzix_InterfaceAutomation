# -*- coding:utf-8 -*-
__author__ = 'jasonchen'
from LogPrint import Log
from Session import Session
class Test(Session):

    headers = {'Content-Type': 'application/json;charset=UTF-8', 'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}

    def __init__(self, url, para):
        Session.__init__(self)
        self._url = url
        self._para = para
        pass

    def check_para(self, para):
        if type(para) != list:
            try:
                para = list(para)
            except:
                Log.warn("read para error")
                raise ValueError

    def Test_success_check(self, _res):

        assert _res['body']['result'] == 0
        assert _res['body']['errMsg'] == ''

    def Test_failure_check(self):
        pass
# -*- coding:utf-8 -*-
__author__ = 'jasonchen'
from TestBase import Test

class SendSmsCode(Test):
    def __init__(self, url, para, mobile):
        Test.__init__(self, url, para)
        self._mobile = mobile
        self.res = self.Test_SendSmsCode()

    def Test_SendSmsCode(self):
        # 1-cookies
        # 2-headers
        # 3-session
        sess = self.start_session()
        # 4-send request
        # handle para evaluation
        paradict = {}
        if len(self._para) > 0:
            self.check_para(self._para)
            paradict[self._para[0]] = self._mobile
            paradict[self._para[1]] = True

        res = self.visit_url(sessiondata=sess, url=self._url, method='post', params=paradict, headers=self.headers,
                             bodytype='json')
        # print res
        return res

    # assert method

    def Test_failure_check(self):

        assert self.res['body']['errMsg'] == '手机号未注册'


class ValidSmsCode(Test):
    def __init__(self, url, para, mobile, smscode):
        Test.__init__(self, url, para)
        self._mobile = mobile
        self._smscode = smscode
        self.res = self.Test_ValidSmsCode()

    def Test_ValidSmsCode(self):
        # 1-cookies
        # 2-headers
        # 3-session
        sess = self.start_session()
        # 4-send request
        # handle para evaluation
        paradict = {}
        if len(self._para) > 0:
            self.check_para(self._para)
            paradict[self._para[0]] = self._mobile
            paradict[self._para[1]] = self._smscode

        res = self.visit_url(sessiondata=sess, url=self._url, method='post', params=paradict, headers=self.headers,
                             bodytype='json')
        return res

    # assert method

    def Test_failure_check(self):
        assert self.res['body']['errMsg'] == '验证码错误'


class GetCollectInfo(Test):

    def __init__(self, url, para):
        Test.__init__(self, url, para)
        self.res = self.Test_GetCollectInfo()

    def Test_GetCollectInfo(self):
        # 1-cookies
        # 2-headers
        # 3-session
        sess = self.start_session()
        # 4-send request
        # handle para evaluation
        paradict = {}
        if len(self._para) > 0:
            self.check_para(self._para)

        res = self.visit_url(sessiondata=sess, url=self._url, method='post', params=paradict, headers=self.headers,
                             bodytype='json')
        return res

    # assert method

class GetCalculatedTrend(Test):

    def __init__(self, url, para):
        Test.__init__(self, url, para)
        self.res = self.Test_GetCalculatedTrend()

    def Test_GetCalculatedTrend(self):
        # 1-cookies
        # 2-headers
        # 3-session
        sess = self.start_session()
        # 4-send request
        # handle para evaluation
        paradict = {}
        if len(self._para) > 0:
            self.check_para(self._para)

        res = self.visit_url(sessiondata=sess, url=self._url, method='post', params=paradict, headers=self.headers,
                             bodytype='json')
        return res

    # assert method


class Favorited(Test):

    def __init__(self, sess, url, para, userid, statisticsid, favorited):
        Test.__init__(self, url, para)
        self._sess = sess
        self._userid = userid
        self._statisticsid = statisticsid
        self._favorited = favorited
        self.res = self.Test_Favorited()

    def Test_Favorited(self):
        # 1-cookies
        # 2-headers
        # 3-session
        sess = self._sess
        # 4-send request
        # handle para evaluation
        paradict = {}
        if len(self._para) > 0:
            self.check_para(self._para)
            paradict[self._para[0]] = self._userid
            paradict[self._para[1]] = self._statisticsid
            paradict[self._para[2]] = self._favorited

        res = self.visit_url(sessiondata=sess, url=self._url, method='post', params=paradict, headers=self.headers,
                             bodytype='json')
        return res

    # assert method

class QueryFileRel(Test):

    def __init__(self, sess, url, para, ownertype, ownerid):
        Test.__init__(self, url, para)
        self._sess = sess
        self._ownertype = ownertype
        self._ownerid = ownerid
        self.res = self.Test_QueryFileRel()

    def Test_QueryFileRel(self):

        paradict = {}
        if len(self._para) > 0:
            self.check_para(self._para)
            paradict[self._para[0]] = self._ownertype
            paradict[self._para[1]] = self._ownerid

        res = self.visit_url(sessiondata=self._sess, url=self._url, method='post', params=paradict, headers=self.headers,
                             bodytype='json')
        return res

    # assert method
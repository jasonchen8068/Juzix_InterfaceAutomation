# -*- coding:utf-8 -*-
__author__ = 'jasonchen'
from Method import MD5
from TestBase import Test

class Login(Test):
    def __init__(self, url, para, username, passwd):
        Test.__init__(self, url, para)
        self._username = username
        self._passwd = passwd
        self.res = self.Test_login(self._username, self._passwd)

    def Test_login(self, username, passwd):
        # 1-cookies
        # 2-headers Test.headers
        # 3-session
        sess = self.start_session()
        # 4-send request
        # get captchacode
        passwd = MD5.MD5().MD5encodePassword(passwd)
        # handle para evaluation
        paradict = {}
        if len(self._para) > 0:
            self.check_para(self._para)
            paradict[self._para[0]] = username
            paradict[self._para[1]] = passwd
            paradict[self._para[2]] = False
            paradict[self._para[3]] = '6666'
            paradict[self._para[4]] = 'win10'

        res = self.visit_url(sessiondata=sess, url=self._url, method='post', params=paradict, headers=self.headers, bodytype='json')
        # print res
        return res

    def get_login_session(self):
        return self.res

    # assert method
    # success check extends Test.Test_success_check

    def Test_login_failure_check(self):

        assert  self.res['body']['errMsg'] == '用户名/密码错误'

class Logout(Test):
    def __init__(self, url, para, loginurl, loginpara, username, passwd):
        Test.__init__(self, url, para)
        self._sess = Login(loginurl, loginpara, username, passwd).get_login_session()
        self.res = self.Test_Logout()

    def Test_Logout(self):
        # 1-cookies
        # 2-headers Test.headers
        # 3-session self._sess
        # 4-send requests
        # handle para evaluation
        paradict = {}
        if len(self._para) > 0:
            self.check_para(self._para)
        res = self.visit_url(sessiondata=self._sess, url=self._url, method='post', params=paradict, headers=self.headers, bodytype='json')
        # print res
        return res


class FindPasswordValid(Test):
    def __init__(self, url, para, mobile, validcode):
        Test.__init__(self, url, para)
        self._mobile = mobile
        self._validcode = validcode
        self.res = self.Test_FindPasswordValid()

    def Test_FindPasswordValid(self):
        # 1-cookies
        # 2-headers Test.headers
        # 3-session
        sess = self.start_session()
        # 4-send request
        # handle para evaluation
        paradict = {}
        if len(self._para) > 0:
            self.check_para(self._para)
            paradict[self._para[0]] = self._mobile
            paradict[self._para[1]] = self._validcode

        res = self.visit_url(sessiondata=sess, url=self._url, method='post', params=paradict, headers=self.headers, bodytype='json')
        # print res
        return res

    def Test_failure_check(self):
        assert self.res['body']['errMsg'] == '验证码错误！'

class FindPasswordSet(Test):

    def __init__(self, url, para, userid, passwd, mobile, validcode):
        Test.__init__(self, url, para)
        self._userid = userid
        self._passwd = passwd
        self._mobile = mobile
        self._validcode = validcode
        self.res = self.Test_FindPasswordSet()

    def Test_FindPasswordSet(self):
        # 1-cookies
        # 2-headers Test.headers
        # 3-session
        sess = self.start_session()
        # 4-send request
        # handle para evaluation
        paradict = {}
        if len(self._para) > 0:
            self.check_para(self._para)
            paradict[self._para[0]] = self._userid
            paradict[self._para[1]] = self._passwd
            paradict[self._para[2]] = self._mobile
            paradict[self._para[3]] = self._validcode

        res = self.visit_url(sessiondata=sess, url=self._url, method='post', params=paradict, headers=self.headers, bodytype='json')
        # print res
        return res

    def Test_failure_nouser_check(self):
        assert self.res['body']['errMsg'] == '用户不存在！'


class LockOrUnlock(Test):
    def __init__(self, sess, url, para, userid, operation):
        Test.__init__(self, url, para)
        self._sess = sess
        self._userid = userid
        self.operation = operation
        self.res = self.Test_LockOrUnlock()

    def Test_LockOrUnlock(self):
        # 1-cookies
        # 2-headers Test.headers
        # 3-session
        # 4-send request
        # handle para evaluation
        paradict = {}
        if len(self._para) > 0:
            self.check_para(self._para)
            paradict[self._para[0]] = self._userid
            paradict[self._para[1]] = self.operation

        res = self.visit_url(sessiondata=self._sess, url=self._url, method='post', params=paradict, headers=self.headers, bodytype='json')
        # print res
        return res

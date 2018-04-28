# -*- coding:utf-8 -*-
import unittest
from MyTools import MyTools
from LoadConfig import LoadConfig
from BusinessClass.CommonInterface import Favorited
from UserInerface import Login
from LogPrint import Log

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        LC = LoadConfig()
        domain = LC.read_domain()
        interface = LC.read_interface('favorited')
        self.url = MyTools.montage_url(domain, interface[0])
        self.para = interface[1]
        # interface need login session
        interface2 = LC.read_interface('login')
        self.loginurl = MyTools.montage_url(domain, interface2[0])
        self.loginpara = interface2[1]
        # print self.para
        Log.info("favorited Test Start")

    # test favorited
    def test001(self):
        Log.info("favorited test001")
        loginsess = Login(self.loginurl, self.loginpara, 'chenjinsong', '11111111').get_login_session()
        F1 = Favorited(loginsess, self.url, self.para, 22, 15, True)
        F1.Test_success_check(F1.res)

    # test cancle favorited
    def test002(self):
        Log.info("favorited test002")
        loginsess = Login(self.loginurl, self.loginpara, 'chenjinsong', '11111111').get_login_session()
        F1 = Favorited(loginsess, self.url, self.para, 22, 15, False)
        F1.Test_success_check(F1.res)

    @classmethod
    def tearDownClass(self):
        Log.info("favorited Test End")

if __name__ == '__main__':
    unittest.main()

# -*- coding:utf-8 -*-
import unittest
from MyTools import MyTools
from LoadConfig import LoadConfig
from UserInterface import Login
from LogPrint import Log

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        LC = LoadConfig()
        domain = LC.read_domain()
        interface = LC.read_interface('login')
        self.url = MyTools.montage_url(domain, interface[0])
        self.para = interface[1]
        # print self.para
        Log.info("login Test Start")

    def test001(self):
        # success case
        Log.info("login test001")
        Login1 = Login(self.url, self.para, 'chenjinsong', '11111111')
        Login1.Test_success_check(Login1.res)

    def test002(self):
        # failure case
        Log.info("login test002")
        Login2 = Login(self.url, self.para, 'chenjinsong', '11111112')
        Login2.Test_login_failure_check()

    @classmethod
    def tearDownClass(self):
        Log.info("login Test End")

if __name__ == '__main__':
    unittest.main()
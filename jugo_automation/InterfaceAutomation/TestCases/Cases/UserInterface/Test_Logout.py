# -*- coding:utf-8 -*-
import unittest
from MyTools import MyTools
from LoadConfig import LoadConfig
from UserInterface import Logout
from LogPrint import Log

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        LC = LoadConfig()
        domain = LC.read_domain()
        interface = LC.read_interface('logout')
        self.url = MyTools.montage_url(domain, interface[0])
        self.para = interface[1]
        # interface needs login
        interface2 = LC.read_interface('login')
        self.loginurl = MyTools.montage_url(domain, interface2[0])
        self.loginpara = interface2[1]
        Log.info("logout Test Start")

    def test001(self):
        # success case
        Log.info("logout test001")
        Logout1 = Logout(url=self.url, para=self.para, loginurl=self.loginurl, loginpara=self.loginpara, username='chenjinsong', passwd='11111111')
        Logout1.Test_success_check(Logout1.res)

    @classmethod
    def tearDownClass(self):
        Log.info("logout Test End")

if __name__ == '__main__':
    unittest.main()
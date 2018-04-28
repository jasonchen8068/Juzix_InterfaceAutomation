# -*- coding:utf-8 -*-
import unittest
from LoadConfig import LoadConfig
from MyTools import MyTools
from LogPrint import Log
from BusinessClass.CommonInterface import SendSmsCode, ValidSmsCode
from time import sleep

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        LC = LoadConfig()
        domain = LC.read_domain()
        interface = LC.read_interface('sendsmscode')
        self.url = MyTools.montage_url(domain, interface[0])
        self.para = interface[1]
        interface2 = LC.read_interface('validsmscode')
        self.url2 = MyTools.montage_url(domain, interface2[0])
        self.para2 = interface2[1]
        Log.info("sendsmscode/validsmscode Test Start")

    # success send and success valid
    def test001(self):
        Send1 = SendSmsCode(self.url, self.para, '17612151210')
        Send1.Test_success_check(Send1.res)
        Send2 = ValidSmsCode(self.url2, self.para2, '17612151210', '666666')
        Send2.Test_success_check(Send2.res)
        # wait for sending smscode
        sleep(2)

    # success send and fail valid
    def test002(self):
        Log.info("sendsmscode/validsmscode Test002")
        Send1 = SendSmsCode(self.url, self.para, '17612151210')
        Send1.Test_success_check(Send1.res)
        Send2 = ValidSmsCode(self.url2, self.para2, '17612151210', '666667')
        Send2.Test_failure_check()

    # check invalid mobile
    def test003(self):
        Log.info("sendsmscode/validsmscode Test003")
        Send1 = SendSmsCode(self.url, self.para, '17612151211')
        Send1.Test_failure_check()

    @classmethod
    def tearDownClass(self):
        Log.info("sendsmscode/validsmscode Test End")
        pass

if __name__ == '__main__':
    unittest.main()
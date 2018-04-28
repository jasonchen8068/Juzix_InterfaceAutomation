# -*- coding:utf-8 -*-
import unittest
from MyTools import MyTools
from LoadConfig import LoadConfig
from UserInterface import FindPasswordSet,FindPasswordValid
from LogPrint import Log
from time import sleep


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        LC = LoadConfig()
        domain = LC.read_domain()
        interface = LC.read_interface('findpasswordset')
        self.url = MyTools.montage_url(domain, interface[0])
        self.para = interface[1]
        # interface needs to call interface findpasswordvalid
        interface2 = LC.read_interface('findpasswordvalid')
        self.validurl = MyTools.montage_url(domain, interface2[0])
        self.validpara = interface2[1]
        Log.info("findpasswordset Test Start")

    # success case userid = 34 loginname = forchanepasswd mobile = 18252023049
    def test001(self):
        Log.info("findpasswordset test001")
        Valid1 = FindPasswordValid(self.validurl, self.validpara, '18252023049', '666666')
        Valid1.Test_success_check(Valid1.res)
        sleep(2)
        # generate passwd
        passwd = MyTools.generate_passwd_int8()
        Set1 = FindPasswordSet(self.url, self.para, 34, passwd, '18252023049', '666666')
        Set1.Test_success_check(Set1.res)
        sleep(1)

    # failure case userid = 34 use 35 errMsg:用户不存在！
    def test002(self):
        Log.info("findpasswordset test002")
        Valid1 = FindPasswordValid(self.validurl, self.validpara, '18252023049', '666666')
        Valid1.Test_success_check(Valid1.res)
        sleep(2)
        # generate passwd
        passwd = MyTools.generate_passwd_int8()
        Set1 = FindPasswordSet(self.url, self.para, 35, passwd, '18252023049', '666666')
        Set1.Test_failure_nouser_check()
        sleep(1)

    @classmethod
    def tearDownClass(self):
        Log.info("findpasswordset Test End")

if __name__ == '__main__':
    unittest.main()
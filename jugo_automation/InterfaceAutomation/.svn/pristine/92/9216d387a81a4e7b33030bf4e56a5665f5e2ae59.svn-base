# -*- coding:utf-8 -*-
import unittest
from MyTools import MyTools
from LoadConfig import LoadConfig
from UserInterface import FindPasswordValid
from LogPrint import Log

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        LC = LoadConfig()
        domain = LC.read_domain()
        interface = LC.read_interface('findpasswordvalid')
        self.url = MyTools.montage_url(domain, interface[0])
        self.para = interface[1]
        Log.info("findpasswordvalid Test Start")

    def test001(self):
        # success case
        Log.info("findpasswordvalid test001")
        F1 = FindPasswordValid(self.url, self.para, '17612151210', '666666')
        F1.Test_success_check(F1.res)

    def test002(self):
        # success case
        Log.info("findpasswordvalid test002")
        F1 = FindPasswordValid(self.url, self.para, '17612151210', '666667')
        F1.Test_failure_check()

    @classmethod
    def tearDownClass(self):
        Log.info("findpasswordvalid Test End")

if __name__ == '__main__':
    unittest.main()
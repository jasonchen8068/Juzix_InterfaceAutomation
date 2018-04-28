# -*- coding:utf-8 -*-
import unittest
from MyTools import MyTools
from LoadConfig import LoadConfig
from BusinessClass.CommonInterface import GetCollectInfo
from LogPrint import Log

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        LC = LoadConfig()
        domain = LC.read_domain()
        interface = LC.read_interface('getcollectinfo')
        self.url = MyTools.montage_url(domain, interface[0])
        self.para = interface[1]
        # print self.para
        Log.info("getcollectinfo Test Start")

    def test001(self):
        # success case
        Log.info("getcollectinfo test001")
        Get1 = GetCollectInfo(self.url, self.para)
        Get1.Test_success_check(Get1.res)

    # def test002(self):
    #     # failure case
    #     Log.info("getcollectinfo test002")
    #     Get1 = GetCollectInfo(self.url, self.para)
    #     Get1.Test_failure_check()

    @classmethod
    def tearDownClass(self):
        Log.info("getcollectinfo Test End")

if __name__ == '__main__':
    unittest.main()
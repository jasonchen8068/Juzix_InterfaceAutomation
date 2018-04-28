# -*- coding:utf-8 -*-
import unittest
from MyTools import MyTools
from LoadConfig import LoadConfig
from BusinessClass.CommonInterface import GetCalculatedTrend
from LogPrint import Log

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        LC = LoadConfig()
        domain = LC.read_domain()
        interface = LC.read_interface('getcalculatedtrend')
        self.url = MyTools.montage_url(domain, interface[0])
        self.para = interface[1]
        # print self.para
        Log.info("getcalculatedtrend Test Start")

    def test001(self):
        # success case
        Log.info("getcalculatedtrend test001")
        Get1 = GetCalculatedTrend(self.url, self.para)
        Get1.Test_success_check(Get1.res)

    # def test002(self):
    #     # failure case
    #     Log.info("getcollectinfo test002")
    #     Get1 = GetCollectInfo(self.url, self.para)
    #     Get1.Test_failure_check()

    @classmethod
    def tearDownClass(self):
        Log.info("getcalculatedtrend Test End")

if __name__ == '__main__':
    unittest.main()
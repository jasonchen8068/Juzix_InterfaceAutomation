# -*- coding:utf-8 -*-
import unittest
from MyTools import MyTools
from LoadConfig import LoadConfig
from UserInterface import LockOrUnlock,Login
from LogPrint import Log
from time import sleep
from SelectFromMysql import SelectFromMysql as SQL


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        LC = LoadConfig()
        domain = LC.read_domain()
        interface = LC.read_interface('lockorunlock')
        self.url = MyTools.montage_url(domain, interface[0])
        self.para = interface[1]
        # interface needs login
        interface2 = LC.read_interface('login')
        self.loginurl = MyTools.montage_url(domain, interface2[0])
        self.loginpara = interface2[1]
        self.Sql = SQL()
        Log.info("lockorunlock Test Start")

    # 测试冻结 (operation=2) userid=22
    def test001(self):
        Log.info("lockorunlock test001")
        # 执行sql设置用户状态为解冻状态
        sql = 'update mpc.sec_user set status = 1 where id = 22'
        self.Sql.insert_update_mysql(sql)
        loginsess = Login(self.loginurl, self.loginpara, 'chenjinsong', '11111111').get_login_session()
        F1 = LockOrUnlock(sess=loginsess, url=self.url, para=self.para, userid=22, operation=2)
        F1.Test_success_check(F1.res)

    # 测试解冻 (operation=1) userid=22
    def test002(self):
        Log.info("lockorunlock test002")
        # 执行sql设置用户状态为冻结状态
        sql = 'update mpc.sec_user set status = 2 where id = 22'
        self.Sql.insert_update_mysql(sql)
        loginsess = Login(self.loginurl, self.loginpara, 'chenjinsong', '11111111').get_login_session()
        F1 = LockOrUnlock(sess=loginsess, url=self.url, para=self.para, userid=22, operation=1)
        F1.Test_success_check(F1.res)

    @classmethod
    def tearDownClass(self):
        Log.info("lockorunlock Test End")

if __name__ == '__main__':
    unittest.main()
import unittest
from LoadData import LoadData
from UserInerface import Login
from LogPrint import Log

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.LD = LoadData()
        self.domain = self.LD.read_domain()
        self.uil = self.LD.read_interface_by_name('login')
        self.url = self.LD.montage_url(self.domain, self.uil)
        Log.info("login Test Start")
        # print self.url

    def test001(self):
        # success case
        Login1 = Login(self.url, 'chenjinsong', '11111111')
        if Login1.Test_login_success():
            Log.info("test001 pass")
        else:
            Log.info("test001 fail")
            raise AssertionError

    def test002(self):
        # failure case
        Login2 = Login(self.url, 'chenjinsong', '11111112')
        if Login2.Test_login_false():
            Log.info("test002 pass")
        else:
            Log.info("test002 fail")
            raise AssertionError

    def tearDown(self):
        Log.info("login Test End")

if __name__ == '__main__':
    unittest.main()

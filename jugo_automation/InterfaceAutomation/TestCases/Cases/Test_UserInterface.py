import unittest
from LoadData import LoadData
from UserInerface import *

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.LD = LoadData()
        self.domain = self.LD.read_domain()
        self.uil = self.LD.read_interface_by_name('login')
        self.url = self.LD.montage_url(self.domain, self.uil)
        print self.url

    def test_something(self):

        Test_login('chenjinsong', '11111111', self.url)



if __name__ == '__main__':
    unittest.main()

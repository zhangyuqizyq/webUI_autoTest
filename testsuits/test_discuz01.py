import unittest
from testsuits.base_testcase import BaseTestCase
from pageobjects.discuz01 import Discuz01

class Discuz01Test(BaseTestCase):
    def test_discuz01(self):
        discuz01=Discuz01(self.driver)
        discuz01.user_login("zhangyuqi")
        discuz01.enter_moreng("come on!!!","I will be a doctor!","you can do it!")
        discuz01.user_logout()


if __name__ =='__main__':
    unittest.main()
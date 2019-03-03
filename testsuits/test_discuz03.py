import unittest
from testsuits.base_testcase import BaseTestCase
from pageobjects.discuz03 import Discuz03

class Discuz03Test(BaseTestCase):

    def test_discuz03(self):
        discuz03=Discuz03(self.driver)
        discuz03.user_login("zhangyuqi")
        discuz03.find_tiezi("haotest","haotesthaotest","haotest")
        discuz03.asser()
        discuz03.user_logout()
if __name__ == '__main__':
    unittest.main()
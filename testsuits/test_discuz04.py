import unittest
from testsuits.base_testcase import BaseTestCase
from pageobjects.discuz04 import Discuz04
from pageobjects.discuz01 import Discuz01
from pageobjects.discuz02 import Discuz02
class Discuz04Test(BaseTestCase):

    def test_discuz04(self):
        discuz01=Discuz01(self.driver)
        discuz02=Discuz02(self.driver)
        discuz04=Discuz04(self.driver)
        discuz01.user_login("admin")
        discuz04.moreng("投票","toupiaotoupiao")
        discuz04.toupiao("title","A","AA","AAA")
        discuz02.admin_logout()


if __name__ =='__main__':
    unittest.main()
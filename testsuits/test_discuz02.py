import unittest
from testsuits.base_testcase import BaseTestCase
from pageobjects.discuz02 import Discuz02
from pageobjects.discuz01 import Discuz01
class Discuz02Test(BaseTestCase):
    def test_discuz02(self):
        discuz02=Discuz02(self.driver)
        discuz02.admin_login("admin")
        discuz02.delete()
        discuz02.manage_bankuai("admin")
        discuz02.admin_logout()
        discuz02.admin_login("zhangyuqi")
        discuz02.new_bankuai("smile!","hahahaahahaha!","good!")
if __name__ == '__main__':
    unittest.main()
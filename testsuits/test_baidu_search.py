import unittest
from selenium import webdriver
import os
from testsuits.base_testcase import BaseTestCase
from pageobjects.baidu_homepage import HomePage

class BaiduSearch(BaseTestCase):
    def test_baidu_search(self):

        home_page=HomePage(self.driver)
        home_page.search("zyq")

if __name__ =='__main__':
    unittest.main()






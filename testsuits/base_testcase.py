from selenium import webdriver
import unittest
from framework.browser_engine import BrowserEngine
class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.browser=BrowserEngine()
        self.browser.open_browser()
        self.driver=self.browser.driver

    def tearDown(self):
        self.driver.quit()


from framework.base import BasePage
from selenium.webdriver.common.by import By
from pageobjects.discuz01 import Discuz01
import time
import unittest

class Discuz03(BasePage):

    def user_login(self,content):
        self.current_window()
        self.discuz01=Discuz01(self.driver)
        self.discuz01.user_login(content)

    # 帖子搜索
    moreng_button_search_loc=(By.CSS_SELECTOR,"#category_1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > h2 > a")
    fatie_button_search_loc=(By.XPATH,"//*[@id='newspecial']/img")
    fatie_content_input_search_loc=(By.NAME,"subject")
    fatie_content2_input_search_loc=(By.XPATH,"//body[@spellcheck='false']")
    fabiaotiezi_button_search_loc=(By.NAME,"topicsubmit")
    find_input_search_loc=(By.CSS_SELECTOR,"#scbar_txt")
    find_button_search_loc=(By.CSS_SELECTOR,"#scbar_btn")

    def find_tiezi(self,content,content1,content2):
        time.sleep(5)
        self.click(*self.moreng_button_search_loc)
        self.click(*self.fatie_button_search_loc)
        self.sendkeys(content,*self.fatie_content_input_search_loc)
        self.frame()
        time.sleep(10)
        self.sendkeys(content1,*self.fatie_content2_input_search_loc)
        self.current_window()
        self.click(*self.fabiaotiezi_button_search_loc)
        self.current_window()
        time.sleep(5)
        self.sendkeys(content2,*self.find_input_search_loc)
        self.click(*self.find_button_search_loc)

    def asser(self):
        self.change_window(1)
        time.sleep(3)
        self.content=(By.XPATH,"//a/strong/font")
        title=self.find_element(*self.content)
        unittest.TestCase().assertEqual(self.text(title),"haotest")
        time.sleep(3)
        self.change_window(0)

    def user_logout(self):
        self.current_window()
        self.discuz01=Discuz01(self.driver)
        self.discuz01.user_logout()

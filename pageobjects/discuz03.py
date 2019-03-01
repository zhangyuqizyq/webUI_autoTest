from framework.base import BasePage
from selenium.webdriver.common.by import By
from pageobjects.discuz01 import Discuz01
import time

class Discuz03(BasePage):

    def user_login(self,content):
        self.current_window()
        self.discuz01=Discuz01(self.driver)
        self.discuz01.user_login(content)

    # 帖子搜索
    find_input_search_loc=(By.CSS_SELECTOR,"#scbar_txt")
    find_button_search_loc=(By.CSS_SELECTOR,"#scbar_btn")


    def find_tiezi(self,content):
        self.current_window()
        time.sleep(5)
        self.sendkeys(content,*self.find_input_search_loc)
        self.click(*self.find_button_search_loc)

    # tuichu_button_search_loc=(By.CSS_SELECTOR,"#toptb > div.y > a:nth-child(5)")
    def asser(self):
        self.change_window(1)
        time.sleep(3)
        self.content=(By.XPATH,"//a/strong/font")
        title=self.find_element(*self.content)
        print(self.text(title))
        time.sleep(5)
        self.change_window(0)
        # self.close()

    def user_logout(self):
        self.current_window()
        self.discuz01 = Discuz01(self.driver)
        self.discuz01.user_logout()

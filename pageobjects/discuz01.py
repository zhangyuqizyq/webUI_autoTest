from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
import unittest
class Discuz01(BasePage):

        #登录属性
        username_input_search_loc=(By.NAME,"username")
        password_input_search_loc=(By.NAME,"password")
        login_button_search_loc=(By.TAG_NAME,"em")
        # login_name_input_search_loc=(By.CSS_SELECTOR,"#um > p:nth-child(2) > strong > a")

        def user_login(self,content):
            self.sendkeys(content,*self.username_input_search_loc)
            self.sendkeys(content,*self.password_input_search_loc)
            self.click(*self.login_button_search_loc)
            # title=self.find_element(*self.login_name_input_search_loc)
            # unittest.TestCase().assertIn(self.text(title),"zhangyuqi")

        # 默认板块发帖 回帖属性
        moreng_button_search_loc=(By.CSS_SELECTOR,"#category_1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > h2 > a")
        fatie_button_search_loc=(By.XPATH,"//*[@id='newspecial']/img")
        fatie_content_input_search_loc=(By.NAME,"subject")
        fatie_content2_input_search_loc=(By.XPATH,"//body[@spellcheck='false']")
        fabiaotiezi_button_search_loc=(By.NAME,"topicsubmit")
        huifu_button_search_loc=(By.CSS_SELECTOR,".fastre")
        huifu_content_input_search_loc=(By.CSS_SELECTOR,"#postmessage")
        huifu_title_button_search_loc=(By.XPATH,"//button/span")

        def enter_moreng(self,content1,content2,content3):
            self.current_window()
            time.sleep(5)
            self.click(*self.moreng_button_search_loc)
            self.click(*self.fatie_button_search_loc)
            self.sendkeys(content1,*self.fatie_content_input_search_loc)
            self.frame()
            time.sleep(10)
            self.sendkeys(content2,*self.fatie_content2_input_search_loc)
            self.current_window()
            self.click(*self.fabiaotiezi_button_search_loc)
            self.click(*self.huifu_button_search_loc)
            self.driver.switch_to.window(self.driver.current_window_handle)
            self.sendkeys(content3,*self.huifu_content_input_search_loc)
            self.click(*self.huifu_title_button_search_loc)


        #退出
        logout_input_search_loc=(By.XPATH,"//*[@id='um']/p[1]/a[5]")
        # page=(By.CSS_SELECTOR,"#toptb")

        def user_logout(self):
            # exit=self.find_element(*self.logout_input_search_loc)
            # logout_assert=self.find_element(*self.login_name_input_search_loc)
            # unittest.TestCase().assertIn(self.text(exit),self.text(logout_assert))
            self.current_window()
            self.click(*self.logout_input_search_loc)



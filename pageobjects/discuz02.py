from framework.base import BasePage
from selenium.webdriver.common.by import By
from pageobjects.discuz01 import Discuz01
import time
import unittest
class Discuz02(BasePage):

    # login_name_input_search_loc=(By.CSS_SELECTOR, "#um > p:nth-child(2) > strong > a")

    def admin_login(self,content):
        self.current_window()
        self.discuz01=Discuz01(self.driver)
        self.discuz01.user_login(content)
        # title=self.find_element(*self.login_name_input_search_loc)
        # unittest.TestCase().assertIn(self.text(title),"admin")

    #删除帖子属性
    duigou_button_search_loc=(By.XPATH,"(//tr/td[@class='o']/input)[1]")
    delete_button_search_loc=(By.XPATH,"//*[@id='mdly']/p[1]/strong[1]/a")
    fatie_content_input_search_loc=(By.NAME,"subject")
    sure_button_search_loc=(By.CSS_SELECTOR,"#modsubmit > span")

    def delete(self):
        self.current_window()
        time.sleep(5)
        self.click(*self.discuz01.moreng_button_search_loc)
        time.sleep(10)
        self.click(*self.duigou_button_search_loc)
        self.click(*self.delete_button_search_loc)
        self.click(*self.sure_button_search_loc)


    #进入板块管理  创建新的板块属性
    gaunlizhongxin_button_search_loc=(By.XPATH,"//*[@id='um']/p[1]/a[6]")
    # man_password_input_search_loc=(By.CSS_SELECTOR,"#loginform > p:nth-child(6) > input")
    # man_submit_input_search_loc=(By.CSS_SELECTOR,"#loginform > p.loginnofloat > input")
    luntan_button_search_loc=(By.CSS_SELECTOR,"#header_forum")
    add_bankuai_button_search_loc=(By.XPATH,"//*[@id='cpform']/table/tbody[3]/tr/td[2]/div/a")
    shunxu_input_search_loc=(By.NAME,"neworder[1][]")
    name_input_search_loc=(By.NAME,"neworder[1][]")
    submit_button_search_loc=(By.NAME,"editsubmit")


    def manage_bankuai(self,content1):
        self.change_window(1)
        self.click(*self.gaunlizhongxin_button_search_loc)
        self.change_window(1)
        # self.sendkeys(content1,*self.fatie_content_input_search_loc)
        # self.click(*self.man_submit_input_search_loc)
        # self.current_window()
        time.sleep(3)
        self.click(*self.luntan_button_search_loc)
        self.frame()
        self.click(*self.add_bankuai_button_search_loc)
        time.sleep(10)
        self.click(*self.submit_button_search_loc)
        self.change_window(0)


    #管理员退出属性
    admin_logout_input_search_loc=(By.CSS_SELECTOR,"#um > p:nth-child(2) > a:nth-child(18)")

    def admin_logout(self):
        self.current_window()
        self.click(*self.admin_logout_input_search_loc)
        time.sleep(3)

    #在新的板块下发帖
    newbankuai_button_search_loc=(By.CSS_SELECTOR,"#category_1 > table > tbody > tr:nth-child(2) > td:nth-child(2) > h2 > a")
    fanhui_button_search_loc=(By.CSS_SELECTOR,"#pt > div > a:nth-child(3)")
    def new_bankuai(self,content1,content2,content3):
        self.current_window()
        time.sleep(10)
        self.click(*self.discuz01.fatie_button_search_loc)
        self.sendkeys(content1,*self.fatie_content_input_search_loc)
        self.frame()
        self.sendkeys(content2,*self.discuz01.fatie_content2_input_search_loc)
        self.current_window()
        self.click(*self.discuz01.fabiaotiezi_button_search_loc)
        self.click(*self.discuz01.huifu_button_search_loc)
        self.driver.switch_to.window(self.driver.current_window_handle)
        self.sendkeys(content3,*self.discuz01.huifu_content_input_search_loc)
        self.click(*self.discuz01.huifu_title_button_search_loc)

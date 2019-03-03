from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
import unittest

class Discuz04(BasePage):
    moreng_button_search_loc=(By.XPATH,"//*[@id='category_1']/table/tbody/tr[1]/td[2]/h2/a")
    fatie_button_search_loc=(By.XPATH,"//*[@id='newspecial']/img")
    fatie_content_input_search_loc=(By.NAME,"subject")
    fatie_content2_input_search_loc=(By.XPATH,"//body[@spellcheck='false']")
    fabiaotiezi_button_search_loc=(By.NAME,"topicsubmit")


    def moreng(self,content1,content2):
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

    #投票属性
    toupiao_button_search_loc=(By.CSS_SELECTOR,"#newspecial_menu > li.poll > a")
    name_input_search_loc=(By.XPATH,"//*[@id='subject']")
    xuanxiang1_input_search_loc=(By.CSS_SELECTOR,"#pollm_c_1 > p:nth-child(1) > input")
    xuanxiang2_input_search_loc=(By.CSS_SELECTOR,"#pollm_c_1 > p:nth-child(2) > input")
    xuanxiang3_input_search_loc=(By.CSS_SELECTOR,"#pollm_c_1 > p:nth-child(3) > input")

    faqitoupiao_button_search_loc=(By.CSS_SELECTOR,"#postsubmit > span")
    cirle_button_button_search_loc=(By.CSS_SELECTOR,"#option_1")
    submit_button_search_loc=(By.CSS_SELECTOR,"#pollsubmit > span")
    title__button_search_loc=(By.CSS_SELECTOR,"#thread_subject")
    first_button_search_loc=(By.CSS_SELECTOR,"#poll > div.pcht > table > tbody > tr:nth-child(1) > td.pvt > label")
    first_bili__button_search_loc=(By.CSS_SELECTOR,"#poll > div.pcht > table > tbody > tr:nth-child(2) > td:nth-child(2)")
    second_button_search_loc=(By.CSS_SELECTOR,"#poll > div.pcht > table > tbody > tr:nth-child(3) > td.pvt > label")
    second_bili_button_search_loc=(By.CSS_SELECTOR,"#poll > div.pcht > table > tbody > tr:nth-child(4) > td:nth-child(2)")
    third_button_search_loc=(By.CSS_SELECTOR,"#poll > div.pcht > table > tbody > tr:nth-child(5) > td.pvt > label")
    third_bili_button_search_loc=(By.CSS_SELECTOR,"#poll > div.pcht > table > tbody > tr:nth-child(6) > td:nth-child(2)")


    def toupiao(self,content1,content2,content3,content4):
        time.sleep(5)
        self.move_to(*self.fatie_button_search_loc)
        self.click(*self.toupiao_button_search_loc)
        time.sleep(3)
        self.sendkeys(content1,*self.name_input_search_loc)
        time.sleep(3)
        self.sendkeys(content2,*self.xuanxiang1_input_search_loc)
        self.sendkeys(content3,*self.xuanxiang2_input_search_loc)
        self.sendkeys(content4,*self.xuanxiang3_input_search_loc)
        self.click(*self.faqitoupiao_button_search_loc)
        self.click(*self.cirle_button_button_search_loc)
        self.click(*self.submit_button_search_loc)
        self.current_window()


        title=self.find_element(*self.title__button_search_loc)
        xuanxiang1=self.find_element(*self.first_button_search_loc)
        xuanxiang2=self.find_element(*self.second_button_search_loc)
        xuanxiang3=self.find_element(*self.third_button_search_loc)

        bili1=self.find_element(*self.first_bili__button_search_loc)
        bili2=self.find_element(*self.second_bili_button_search_loc)
        bili3=self.find_element(*self.third_bili_button_search_loc)

        print("主题名称为:",self.text(title))
        print("第一个选项名称为:",self.text(xuanxiang1))
        print("第二个选项名称为:",self.text(xuanxiang2))
        print("第三个选项名称为:",self.text(xuanxiang3))
        print("第一个比例为:",self.text(bili1))
        print("第二个比例为:",self.text(bili2))
        print("第三个比例为:",self.text(bili3))


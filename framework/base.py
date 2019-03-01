import os.path
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains

logger=Logger(logger="BasePage").getlog()
class BasePage(object):

    def __init__(self,driver):
        self.driver=driver

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def open_url(self,url):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

    def close(self):
        self.driver.close()

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            logger.info("找到页面元素%s",loc)
            return self.driver.find_element(*loc)
        except Exception as e:
            logger.error("%s页面中未能找到%s元素"%(self,loc))


    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            logger.info("找到页面元素%s",loc)
            return self.driver.find_elements(*loc)
        except Exception as e:
            logger.error("%s页面中未能找到%s元素"%(self,loc))



    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        el.clear()
        try:
           el.send_keys(text)
           logger.info("输入内容%s",text)
        except Exception as e:
            logger.error("Failed to type in input box with %s"%e)

    def get_window_img(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("End take screenshot and save to folder:/screen")
        except Exception as e:
            self.get_window_img()
            logger.error("Failed to take screenshot! %s"%e)

    def current_window(self):
        try:
            self.driver.switch_to.window(self.driver.current_window_handle)
            logger.info("successful")
        except Exception as e:
            logger.error("Failed %s" % e)

    def change_window(self,num):
        try:
            self.driver.switch_to.window(self.driver.window_handles[num])
            logger.info("successful")
        except Exception as e:
            logger.error("Failed %s" % e)

    def text(self,content):
        try:
            el=content.text
            logger.info("successful")
            return el

        except Exception as e:
            logger.error("Failed %s" % e)

    def frame(self):
        try:
            self.driver.frame=self.driver.switch_to.frame(0)
            logger.info("successful")
        except Exception as e:
            logger.error("Failed %s" % e)

    def clear(self,*loc):
        el=self.find_element(*loc)
        el.clear()

    def move_to(self,*loc):
        el=self.find_element(*loc)
        ActionChains(self.driver).move_to_element(el).perform()

    def click(self,*loc):
        el=self.find_element(*loc)
        el.click()



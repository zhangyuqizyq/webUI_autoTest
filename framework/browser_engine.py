import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger=Logger(logger="BrowserEngine").getlog()
class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath('.'))
    chrome_driver_path=dir+"/tools/chromedriver.exe"
    ie_driver_path=dir+"/tools/IEDriverServer.exe"
    firefox_driver_path=dir+"tools/geckodriver.exe"
    def open_browser(self):
        self.config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+ "/config/config.ini"
        self.config.read(file_path)
        self.browser=self.config.get("browserType","browserName")
        logger.info("you had select %s browser"%self.browser)
        self.url=self.config.get("testServer","URL")
        logger.info("The test server url is %s"%self.url)

        if self.browser=="Firefox":
            self.driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info("Staring Firefox browser")
        if self.browser=="Chrome":
            self.driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Staring Chrome browser")
        if self.browser=="IE":
            self.driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info("Staring IE browser")

        self.driver.get(self.url)
        logger.info("Open url %s" %self.url)
        self.driver.maximize_window()
        logger.info("Maxmize the current window")
        self.driver.implicitly_wait(20)
        logger.info("Set implicitly wait 10 seconds")
        return self.driver

    def quit_browser(self):
        logger.info("Now,Close and quit the browser")
        self.driver.quit()
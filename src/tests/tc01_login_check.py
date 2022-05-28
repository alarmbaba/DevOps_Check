import sys
sys.path.append("/Users/koushikchakraborty/Documents/selenium/src")

import unittest
import time
from selenium import webdriver
from pages.home_page import home_page
from pages.login_page import login_page
import HtmlTestRunner


class Test_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Safari(executable_path="/usr/bin/safaridriver")
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://demo.guru99.com/")
        cls.driver.maximize_window()
        return super().setUpClass()

    def testCaseLogin(self):
        driver = self.driver
        home = home_page(driver)
        home.click_dropdown()
        home.click_login_link()
        time.sleep(10)
    
    def testCaseLogin2(self):
        driver = self.driver
        login = login_page(driver)
        login.enter_email("mngr410996")
        login.enter_password("zArEvam")
        login.click_login()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        return super().tearDownClass()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner("../report/run1.html"))
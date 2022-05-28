from selenium import webdriver
from selenium.webdriver.common.by import By


#driver = webdriver.Safari(executable_path="/usr/bin/safaridriver")
#driver.get("https://demo.guru99.com/")
class home_page():

    def __init__(self, driver) -> None:
        self.driver = driver
        self.title = "guru99 Bank Home Page"
        self.dropdown_css = "#navbar-brand-centered > ul > li:nth-child(1)"
        self.login_css = "#navbar-brand-centered > ul > li.dropdown.open > ul > li:nth-child(11) > a"

    def click_dropdown(self):
        self.driver.find_element(By.CSS_SELECTOR, self.dropdown_css).click()

    def click_login_link(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_css).click()

        
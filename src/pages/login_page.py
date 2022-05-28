from selenium import webdriver
from selenium.webdriver.common.by import By


class login_page():

    def __init__(self, driver) -> None:
        self.driver = driver
        self.login_id = "email"
        self.passwd_id = "passwd"
        self.login_id = "SubmitLogin"

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.login_id).send_keys(email)
    
    def enter_password(self, passwd):
        self.driver.find_element(By.ID, self.passwd_id).send_keys(passwd)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_id).click()
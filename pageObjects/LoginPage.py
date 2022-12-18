from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "user-name"
    texbox_password_id = "password"
    btn_login_id = "login-button"

    def __init__(self, driver):
        self.driver = driver;

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.texbox_password_id).clear()
        self.driver.find_element(By.ID,self.texbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.btn_login_id).click()

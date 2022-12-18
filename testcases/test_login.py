import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    baseURL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Google":
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import readConfig
from utilities.customerLogger import LogGen


class Test_001_Login:
    baseURL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    logger = LogGen.loggen()

    # baseURL = readConfig.getApplicationURL()
    # username = readConfig.getUsername()
    # password = readConfig.getPassword()

    def test_homePageTitle(self, setup):
        self.logger.info("**************************Test_001_Login started*************************")
        # self.logger.info("**************************Ver started*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        # self.driver.close()
        if actual_title == "Swag Labs":
            assert True
            self.logger.info("Title is matching..Hence test is PASSED")
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/loginTest.png")
            self.driver.close()
            self.logger.error("Title test failed.Capturing screenshot")
            assert False

    def test_login(self, setup):
        self.logger.info("******************Started executing test_login***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******************test_login PASSED***************")
        self.driver.close()
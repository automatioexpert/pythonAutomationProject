import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities import XLUtils
from utilities.readProperties import readConfig
from utilities.customerLogger import LogGen
import openpyxl


class Test_002_DDT_Login:
    path = ".//TestData/TestData.xlsx"
    baseURL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("******************Started executing test_login_ddt***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Total no of rows: " , self.rows)
        self.colums = XLUtils.getColumnCount(self.path, 'Sheet1')
        print("Total no of columns: " ,self.colums)

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            # self.exp=XLUtils.readData(self.path,'Sheet1',r,3)
            print(self.user)
            print(self.password)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            self.logger.info("******************test_login_ddt PASSED***************")
            #self.driver.close()
            print("Closed the browser after test completion")

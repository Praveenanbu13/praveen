import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import loginpage
from pageObjects.AddToCart import Product
from pageObjects.CheckOut import checkout
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGeneration
from selenium.webdriver.common.by import By

class Test_01_Login:
    baseURL = ReadConfig.ApplicationURL()
    username = ReadConfig.Username()
    password = ReadConfig.Password()
    Fname = ReadConfig.Firstname()
    Lname = ReadConfig.Lastname()
    Pincode = ReadConfig.Pcode()
    logger = LogGeneration.loggen()


    # def test_homepageTitle(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     act_title = self.driver.title
    #     self.lp = loginpage(self.driver)
    #     self.lp.setUserName(self.username)
    #     # self.driver.close()

    def test_Login(self, setup):
        self.logger.info("********** Test_01_Login ***********")
        self.logger.info("*********** Verifying Login Page *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(1)
        self.lp = loginpage(self.driver)
        self.lp.setUserName(self.username)
        time.sleep(1)
        self.lp.setPassword(self.password)
        time.sleep(1)
        self.lp.clickLogin()
        self.ad = Product(self.driver)
        self.ad.clickAdd1()
        time.sleep(1)
        self.ad.ClickAdd2()
        time.sleep(1)
        self.ad.ClickCart()
        time.sleep(1)
        self.driver.save_screenshot(".\\Screenshots\\"+"test_Login.png")
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_Log.png")
        self.co = checkout(self.driver)
        self.co.ClickCheckout()
        time.sleep(1)
        self.co.textboxFname(self.Fname)
        time.sleep(1)
        self.co.textboxLname(self.Lname)
        time.sleep(1)
        self.co.textboxPincode(self.Pincode)
        time.sleep(1)
        self.co.ClickContinue()





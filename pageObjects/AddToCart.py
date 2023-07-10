from selenium import webdriver
from selenium.webdriver.common.by import By


class Product:
    button_Addbutton01_id = "add-to-cart-sauce-labs-backpack"
    button_Addbutton02_id = "add-to-cart-sauce-labs-bike-light"
    button_AddCart_Xpath = "//*[@id='shopping_cart_container']/a"


    def __init__(self, driver):
        self.driver = driver

    def clickAdd1(self):
        self.driver.find_element(By.ID, self.button_Addbutton01_id).click()

    def ClickAdd2(self):
        self.driver.find_element(By.ID, self.button_Addbutton02_id).click()

    def ClickCart(self):
        self.driver.find_element(By.XPATH, self.button_AddCart_Xpath).click()



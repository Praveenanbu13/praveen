from selenium import webdriver
from selenium.webdriver.common.by import By

class checkout:
    button_Checkout_id = "checkout"
    textbox_Firstname = "first-name"
    textbox_Lastname = "last-name"
    textbox_Pincode = "postal-code"
    textbox_click_pincode = "//*[@data-test='postalCode']"
    button_continue = "//input[@class='submit-button btn btn_primary cart_button btn_action']"


    def __init__(self, driver):
        self.driver = driver

    def ClickCheckout(self):
        self.driver.find_element(By.ID, self.button_Checkout_id).click()

    def textboxFname(self, Fname):
        self.driver.find_element(By.ID, self.textbox_Firstname).send_keys(Fname)

    def textboxLname(self, Lname):
        self.driver.find_element(By.ID, self.textbox_Lastname).send_keys(Lname)

    def textboxPincode(self, Pincode):
        self.driver.find_element(By.ID, self.textbox_Pincode).send_keys(Pincode)

    def ClickContinue(self):
        self.driver.find_element(By.XPATH, self.button_continue).click()
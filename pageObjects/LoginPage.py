from selenium import webdriver
from selenium.webdriver.common.by import By


class loginpage:
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_loginbutton_id = "login-button"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
        # self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.button_loginbutton_id).click()

    # def clickLogout(self):
    #     self.driver.find_element_by_link_text(self.link_logout_linktext).click()


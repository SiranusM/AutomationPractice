from locators.signinpagelocators import SignInPageLocators 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class SignInPage(BasePage):
      
    def enter_create_account_email_addres(self, email):
        email_element = self.driver.find_element(*SignInPageLocators.EMAIL_ADDRESS_TEXT_INPUT)
        email_element.clear()
        email_element.send_keys(email)

    def click_create_account_button(self):
        create_account_button_element = self.driver.find_element(*SignInPageLocators.CREATE_ACCOUNT_BUTTON)
        create_account_button_element.click()

    def check_if_account_create_error_is_visible(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.visibility_of_element_located((By.ID, 'create_account_error')))
            return True
        except:
            return False

    def enter_sign_in_email(self, email):
        email_input_element = self.driver.find_element(*SignInPageLocators.SIGN_IN_EMAIL_TEXT_INPUT)
        email_input_element.send_keys(email)

    def enter_sign_in_password(self, password):
        password_input_element = self.driver.find_element(*SignInPageLocators.SIGN_IN_PASSWORD_TEXT_INPUT)
        password_input_element.send_keys(password)   

    def click_sign_in_button(self):
        sign_in_button_element = self.driver.find_element(*SignInPageLocators.SIGN_IN_BUTTON)    
        sign_in_button_element.click()

    def get_page_title(self):
        return self.driver.title    
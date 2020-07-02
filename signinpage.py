from locators.signinpagelocators import SignInPageLocators 
import random
import string
import time
from selenium import webdriver

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class SignInPage(BasePage):
      
    def enter_create_account_email_addres(self, email):
        element = self.driver.find_element(*SignInPageLocators.EMAIL_ADDRESS_TEXT_INPUT)
        element.clear()
        element.send_keys(email)

    def click_create_account_button(self):
        element = self.driver.find_element(*SignInPageLocators.CREATE_ACCOUNT_BUTTON)
        element.click()

    def check_if_account_create_error_is_visible(self):
        try:
            time.sleep(6)
            self.driver.find_element(*SignInPageLocators.CREATE_ACCOUNT_ERROR)
            return True
        except:
            return False

    def enter_sign_in_email(self, email):
        element = self.driver.find_element(*SignInPageLocators.SIGN_IN_EMAIL_TEXT_INPUT)
        element.send_keys(email)

    def enter_sign_in_password(self, password):
        element = self.driver.find_element(*SignInPageLocators.SIGN_IN_PASSWORD_TEXT_INPUT)
        element.send_keys(password)   

    def click_sign_in_button(self):
        element = self.driver.find_element(*SignInPageLocators.SIGN_IN_BUTTON)    
        element.click()

    def get_page_title(self):
        return self.driver.title    

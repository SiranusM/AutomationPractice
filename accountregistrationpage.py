from locators.registrationpagelocators import RegistrationPageLocators 
from selenium.webdriver.support.ui import Select
import time

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class AccountRegistrationPage(BasePage):

    def fill_in_account_registration_form(self):
        time.sleep(5)
        element = self.driver.find_element(*RegistrationPageLocators.FIRSTNAME_TEXT_INPUT)
        element.send_keys('firstname')
        element = self.driver.find_element(*RegistrationPageLocators.LASTNAME_TEX_INPUT)
        element.send_keys('lastname')
        element = self.driver.find_element(*RegistrationPageLocators.PASSWORD_TEXT_INPUT)
        element.send_keys('password')
        element = self.driver.find_element(*RegistrationPageLocators.ADDRESS_TEXT_INPUT)
        element.send_keys('address')
        element = self.driver.find_element(*RegistrationPageLocators.CITY_TEXT_INPUT)
        element.send_keys('city')
        element = self.driver.find_element(*RegistrationPageLocators.STATE_DROPDOWN)
        element.click()

        select = Select(self.driver.find_element(*RegistrationPageLocators.STATE_DROPDOWN))
        select.select_by_visible_text('Alaska')

        element = self.driver.find_element(*RegistrationPageLocators.POSTAL_CODE_TEXT_INPUT)
        element.send_keys('12345')
        element = self.driver.find_element(*RegistrationPageLocators.PHONE_NUMBER_TEXT_INPUT)
        element.send_keys('123456789')
        element = self.driver.find_element(*RegistrationPageLocators.ALIAS_TEXT_INPUT)
        element.clear()
        element.send_keys('testalias')

    def click_regiser_button(self):
        element = self.driver.find_element(*RegistrationPageLocators.REGISTER_ACCOUNT_BUTTON)
        element.click()
     
    def get_page_title(self):
        return self.driver.title
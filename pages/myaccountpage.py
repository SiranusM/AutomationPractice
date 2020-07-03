from locators.myaccountpagelocators import MyAccountPageLocators 
from selenium.webdriver import ActionChains

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MyAccountPage(BasePage):
    def open_summer_dresses_catalog(self):
       
        actions = ActionChains(self.driver)
        dresses_menu_element = self.driver.find_element(*MyAccountPageLocators.DRESSES_MENU_ELEMENT)
        actions.move_to_element(dresses_menu_element).perform()

        summer_dresses_element = self.driver.find_element(*MyAccountPageLocators.SUMMER_DRESSES_ELEMENT)
        summer_dresses_element.click()
from locators.mainpagelocators import MainPageLocators 

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    def click_sign_in_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_IN_BUTTON)
        element.click()
from locators.mainpagelocators import MainPageLocators 
from selenium.webdriver.common.by import By
import random

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    def click_sign_in_button(self):
        login_element = self.driver.find_element(*MainPageLocators.LOGIN_IN_BUTTON)
        login_element.click()

    def select_dress(self):
        products_grid = self.driver.find_element(*MainPageLocators.PRODUCTS_GRID)
        
        products_list = []
        try:
            product_elements = products_grid.find_elements(By.CSS_SELECTOR, '.ajax_block_product') 
            for product in product_elements:
                products_list.append(product)
            products_list[0].click()
        except:
            raise ValueError('Items list is empty, nothing to select')
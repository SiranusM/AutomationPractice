from locators.productpagelocators import ProductPageLocators 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class ProductPage(BasePage):

    def select_dress_quantity(self, quantity):
        quantity_element = self.driver.find_element(*ProductPageLocators.PRODUCT_QUANTITY_INPUT)
        quantity_element.clear()
        quantity_element.send_keys(quantity)
    
    def select_dress_size(self, size):
        pick_size_element = self.driver.find_element(*ProductPageLocators.PRODUCT_SIZE_DROPDOWN)
        pick_size_element.click()
        size_elements = pick_size_element.find_elements(By.TAG_NAME, 'option') 

        available_sizes = []
        size_elements_list = []

        for size_el in size_elements:
            size_elements_list.append(size_el)
            value = size_el.get_attribute('text')
            available_sizes.append(value)
            if value == size:
                size_el.click()
                break

        if not available_sizes.count(size):
            raise ValueError(f'Size {size} is no longer in stock or does not exit')

    def select_dress_color(self, color):
        pick_color_element = self.driver.find_element(*ProductPageLocators.PRODUCT_COLOR_LIST)
        color_elements = pick_color_element.find_elements(By.TAG_NAME, 'a')
        available_colors =[]
        color_elements_list = []

        for color_el in color_elements:
            color_elements_list.append(color_el)
            value = color_el.get_attribute('title')
            available_colors.append(value)
            if value == color:
                color_el.click()
        
        if not available_colors.count(color):
            raise ValueError(f'Color { color } is no longer in stock or does not exit')

    def add_to_cart(self):  
        add_to_cart_element = self.driver.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_element.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, 'layer_cart')))
        
    def proceed_to_checkout(self):
        proceed_to_checkout_element = self.driver.find_element(*ProductPageLocators.PROCEED_TO_CHECKOUT_BUTTON_IN_MODAL)
        proceed_to_checkout_element.click()
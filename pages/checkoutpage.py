from locators.checkoutpagelocators import CheckoutPageLocators 
from selenium.webdriver.common.by import By
import json
import time

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class CheckoutPage(BasePage):
    def click_proceed_to_checkout_in_summary_section(self):
        element = self.driver.find_element(*CheckoutPageLocators.PROCEED_TO_CHECKOUT_BUTTON_IN_SUMMARY)
        element.click()

    def click_proceed_to_checkout_in_address_section(self):
        element = self.driver.find_element(*CheckoutPageLocators.PROCEED_TO_CHECKOUT_BUTTON_IN_ADDRESS)
        element.click()

    def agree_terms_of_servive(self):
        element = self.driver.find_element(*CheckoutPageLocators.TERMS_OF_SERVICE_CHECKBOX)
        element.click()

    def click_proceed_to_checkout_in_shipping_section(self):
        element = self.driver.find_element(*CheckoutPageLocators.PROCEED_TO_CHECKOUT_BUTTON_IN_SHIPPING)
        element.click()

    def select_paymenent_type_bank_wire(self):
        element = self.driver.find_element(*CheckoutPageLocators.PAYMENT_BY_BANK_LINK)
        element.click()

    def click_confirm_order(self):
        element = self.driver.find_element(*CheckoutPageLocators.CONFIRM_ORDER_BUTTON)
        element.click()

    def get_cart_products_quantity(self):
        element = self.driver.find_element(*CheckoutPageLocators.CART_ORDERS_QUANTITY_ELEMENT)
        return element.text
     
    

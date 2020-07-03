from selenium.webdriver.common.by import By

class CheckoutPageLocators(object):
    TERMS_OF_SERVICE_CHECKBOX = (By.ID, 'cgv')
    PROCEED_TO_CHECKOUT_BUTTON_IN_SUMMARY = (By.XPATH, '//*[@id="center_column"]/p[2]/a[1]')
    PROCEED_TO_CHECKOUT_BUTTON_IN_ADDRESS = (By.XPATH, '//*[@name="processAddress"]')
    PROCEED_TO_CHECKOUT_BUTTON_IN_SHIPPING = (By.XPATH, '//*[@name="processCarrier"]')
    PAYMENT_BY_BANK_LINK = (By.CLASS_NAME, 'bankwire')
    CONFIRM_ORDER_BUTTON = (By.XPATH, '//*[@id="cart_navigation"]/button/span')
    CART_ORDERS_QUANTITY_ELEMENT = (By.CSS_SELECTOR, '.ajax_cart_quantity')
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_IN_BUTTON = (By.CLASS_NAME, 'login')
    PRODUCTS_GRID = (By.CSS_SELECTOR, '.product_list.grid.row')
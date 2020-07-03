from selenium.webdriver.common.by import By

class MyAccountPageLocators(object):
    DRESSES_MENU_ELEMENT = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a')
    SUMMER_DRESSES_ELEMENT = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/ul/li[3]/a')
    #SUMMER_DRESSES_ELEMENT = (By.XPATH, '//*[@id="block_top_menu"]//*[@title="Summer Dresses"]')
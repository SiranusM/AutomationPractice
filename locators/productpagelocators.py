from selenium.webdriver.common.by import By

class ProductPageLocators():
    PRODUCT_QUANTITY_INPUT = (By.ID, 'quantity_wanted')
    PRODUCT_SIZE_DROPDOWN = (By.ID, 'group_1')
    PRODUCT_COLOR_LIST = (By.ID, 'color_to_pick_list')
    ADD_TO_CART_BUTTON = (By.ID, 'add_to_cart')
    PROCEED_TO_CHECKOUT_BUTTON_IN_MODAL = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')
from selenium.webdriver.common.by import By

class RegistrationPageLocators(object):
    FIRSTNAME_TEXT_INPUT = (By.ID, 'customer_firstname')
    LASTNAME_TEX_INPUT = (By.ID, 'customer_lastname')
    PASSWORD_TEXT_INPUT = (By.ID, 'passwd')
    ADDRESS_TEXT_INPUT = (By.ID, 'address1')
    CITY_TEXT_INPUT = (By.ID, 'city')
    STATE_DROPDOWN = (By.ID, 'id_state')
    STATE_OPTION = (By.TAG_NAME, 'option')
    POSTAL_CODE_TEXT_INPUT = (By.ID, 'postcode')
    COUNTRY_DROPDOWN = ()
    PHONE_NUMBER_TEXT_INPUT = (By.ID, 'phone_mobile') 
    ALIAS_TEXT_INPUT = (By.ID, 'alias')
    REGISTER_ACCOUNT_BUTTON = (By.ID, 'submitAccount')

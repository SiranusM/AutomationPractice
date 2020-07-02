from selenium.webdriver.common.by import By

class SignInPageLocators(object):
    EMAIL_ADDRESS_TEXT_INPUT = (By.ID, 'email_create')
    CREATE_ACCOUNT_BUTTON = (By.ID, 'SubmitCreate')
    CREATE_ACCOUNT_ERROR = (By.ID, 'create_account_error')
    SIGN_IN_EMAIL_TEXT_INPUT = (By.ID, 'email')
    SIGN_IN_PASSWORD_TEXT_INPUT = (By.ID, 'passwd')
    SIGN_IN_BUTTON = (By.ID, 'SubmitLogin')
    
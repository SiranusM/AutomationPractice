from selenium import webdriver
import unittest
import mainpage
import signinpage
import accountregistrationpage
import random
import string

class CreateAccount(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()
    
    def test_create_account(self):
        main_page = mainpage.MainPage(self.driver)
        main_page.click_sign_in_button()

        letters = string.ascii_lowercase
        email_address = ''.join(random.choice(letters) for i in range(15)) + '@testmail.mail'

        sign_in_page = signinpage.SignInPage(self.driver)
        sign_in_page.enter_create_account_email_addres(email_address)
        sign_in_page.click_create_account_button() 

        registration_page = accountregistrationpage.AccountRegistrationPage(self.driver)
        registration_page.fill_in_account_registration_form()
        registration_page.click_regiser_button()

        self.assertEqual('My account - My Store', registration_page.get_page_title())

    def test_already_registered_email_validation(self):
        main_page = mainpage.MainPage(self.driver)
        main_page.click_sign_in_button()
        
        sign_in_page = signinpage.SignInPage(self.driver)
        sign_in_page.enter_create_account_email_addres('test@test.test')
        sign_in_page.click_create_account_button() 

        self.assertTrue(sign_in_page.check_if_account_create_error_is_visible(), 'Email validation failed')

    def tearDown(self):
        self.driver.close()
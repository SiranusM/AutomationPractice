from selenium import webdriver
import unittest
import pages.mainpage
import pages.signinpage
import pages.accountregistrationpage
import random
import string
from dotenv import load_dotenv
load_dotenv()
import os

class CreateAccount(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(os.getenv('BASE_URL'))
        self.driver.maximize_window()
    
    def test_create_account(self):
        """ Test creates a new user account and asserts if user is in correct page after registration. """

        main_page = pages.mainpage.MainPage(self.driver)
        main_page.click_sign_in_button()

        letters = string.ascii_lowercase
        email_address = ''.join(random.choice(letters) for i in range(15)) + '@testmail.mail'

        sign_in_page = pages.signinpage.SignInPage(self.driver)
        sign_in_page.enter_create_account_email_addres(email_address)
        sign_in_page.click_create_account_button() 

        registration_page = pages.accountregistrationpage.AccountRegistrationPage(self.driver)
        registration_page.fill_in_account_registration_form()
        registration_page.click_regiser_button()

        self.assertEqual('My account - My Store', registration_page.get_page_title(), 'User is not in My account page')

    def test_already_registered_email_validation(self):
        """ Test checks is user is not able to register the same email twice and asserts if email validation message is received. """

        main_page = pages.mainpage.MainPage(self.driver)
        main_page.click_sign_in_button()
        
        sign_in_page = pages.signinpage.SignInPage(self.driver)
        sign_in_page.enter_create_account_email_addres('test@test.test')
        sign_in_page.click_create_account_button() 

        self.assertTrue(sign_in_page.check_if_account_create_error_is_visible(), 'Email validation failed')

    def tearDown(self):
        self.driver.close()
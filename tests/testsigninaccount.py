from selenium import webdriver
import unittest
import pages.mainpage
import pages.signinpage
from dotenv import load_dotenv
load_dotenv()
import os

class SigInAccount(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(os.getenv('BASE_URL'))
        self.driver.maximize_window()

    def test_sign_in_account(self):
        """ Test signs in already created user and asserts if user appears in correct page. """

        main_page = pages.mainpage.MainPage(self.driver)
        main_page.click_sign_in_button()

        sign_in_page = pages.signinpage.SignInPage(self.driver)
        email = os.getenv('EMAIL')
        sign_in_page.enter_sign_in_email(email)
        password = os.getenv('PASSWORD')
        sign_in_page.enter_sign_in_password(password)
        sign_in_page.click_sign_in_button()

        self.assertEqual('My account - My Store', sign_in_page.get_page_title(), 'User is not in My account page')

    def tearDown(self):
        self.driver.close() 
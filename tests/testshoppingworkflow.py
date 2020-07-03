from selenium import webdriver
import unittest
import pages.mainpage
import pages.signinpage
import pages.myaccountpage
import pages.productpage
import pages.checkoutpage
from dotenv import load_dotenv
load_dotenv()
import os

class ShoppingWorkFlow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(os.getenv('BASE_URL'))
        self.driver.maximize_window()
        main_page = pages.mainpage.MainPage(self.driver)
        main_page.click_sign_in_button()

        sign_in_page = pages.signinpage.SignInPage(self.driver)
        email = os.getenv('EMAIL')
        sign_in_page.enter_sign_in_email(email)
        password = os.getenv('PASSWORD')
        sign_in_page.enter_sign_in_password(password)
        sign_in_page.click_sign_in_button()

    def test_shopping_work_flow(self):
        """ Test goes through the whole flow to select and order an item. Then it checks if items cart is empty. """

        my_account_page = pages.myaccountpage.MyAccountPage(self.driver)
        my_account_page.open_summer_dresses_catalog()

        main_page = pages.mainpage.MainPage(self.driver)
        main_page.select_dress()

        product_page = pages.productpage.ProductPage(self.driver)
        product_page.select_dress_quantity('2')
        product_page.select_dress_size('M')
        product_page.select_dress_color('Blue')
        product_page.add_to_cart()
        product_page.proceed_to_checkout()

        checkout_page = pages.checkoutpage.CheckoutPage(self.driver)
        checkout_page.click_proceed_to_checkout_in_summary_section()
        checkout_page.click_proceed_to_checkout_in_address_section()
        checkout_page.agree_terms_of_servive()
        checkout_page.click_proceed_to_checkout_in_shipping_section()
        checkout_page.select_paymenent_type_bank_wire()
        checkout_page.click_confirm_order()
        
        self.assertEqual(checkout_page.get_cart_products_quantity(), '')
    
    def tearDown(self):
        self.driver.close()
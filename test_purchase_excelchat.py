import unittest
from selenium import webdriver
from driver_wrapper import DriverWrapper
from pages.login import Login
from pages.pricing import Pricing
from pages.home import Home
from clean_up import CleanUp
import time
from config.main_config import Url, AskerAccount


class PurchaseExcelchat(unittest.TestCase):
    def setUp(self):
        # Set up state
        CleanUp().terminate_subscription()

        # Init
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # Launch Asker
        self.driver.get(str(Url.ASKER_URL.value))

    def login(self, email, password):
        login_page = Login(self.driver)
        assert login_page.is_login_modal_present(), "Login modal is visible"
        login_page.login(email, password)

    def purchase(self, default_card):
        purchase_page = Pricing(self.driver)
        assert purchase_page.is_purchase_modal_present(), "Purchase modal is visible"
        purchase_page.purchase(default_card)
        purchase_page.wait_for_finishing()

    def test_purchase_successful(self):
        home_page = Home(self.driver)

        # Invoke Login Modal
        home_page.click_login_modal_button()

        # Login
        self.login(AskerAccount.EMAIL.value, AskerAccount.PASSWORD.value)
        assert home_page.is_session_balance_present(), "Session balanced is visible"

        # Invoke Purchase Modal
        home_page.click_pricing_nav_link()
        home_page.click_unlimited_session_option()

        # Purchase
        self.purchase(AskerAccount.DEFAULT_CARD.value)
        assert home_page.is_session_balance_unlimited(), "Session balanced is unlimited"

        time.sleep(2)


if __name__ == "__main__":
    unittest.main()

import unittest
from selenium import webdriver
from driver_wrapper import DriverWrapper
from pages.login import Login
from pages.pricing import Pricing
from pages.home import Home
from clean_up import CleanUp
import time
from config.main import Url, AskerAccount


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
        Login(self.driver).login(email, password)

    def purchase(self, default_card):
        Pricing(self.driver).purchase(default_card)

    def test_purchase_successful(self):
        home_page = Home(self.driver)

        # Invoke Login Modal
        home_page.click_login_modal_button()

        # Login
        self.login(AskerAccount.EMAIL.value, AskerAccount.PASSWORD.value)
        assert home_page.is_session_balance_found(), "Session balanced is visible"

        # Invoke Purchase Modal
        home_page.click_unlimited_session_option()

        # Purchase
        self.purchase(AskerAccount.DEFAULT_CARD.value)

        time.sleep(2)


if __name__ == "__main__":
    unittest.main()

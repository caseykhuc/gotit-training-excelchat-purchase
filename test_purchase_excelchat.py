import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from driver_wrapper import DriverWrapper
from pages.login import Login
from pages.pricing import Pricing
from pages.admin import Admin
from clean_up import CleanUp
from selenium.webdriver.support import expected_conditions as EC
import time
from config.main import Url


class PurchaseExcelchat(unittest.TestCase):
    def setUp(self):
        # Clean up
        CleanUp().terminate_subscription()

        # Init
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # Launch Asker
        self.driver.get(str(Url.ASKER_URL.value))

    _session_balance = {"locator": "test-session-balance-header-button", "by": By.ID}
    _unlimited_session_balance = {
        "locator": '//*[@id="test-session-balance-header-button"]/strong[text()="unlimited"]',
        "by": By.XPATH,
    }

    def login(self, email, password):
        login_page = Login(self.driver)

        login_page.click_login_modal_button()
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login_submit_button()
        login_page.driver.wait_for_element(login_page._login_modal, invisible=True)
        self.assertTrue(login_page.driver.wait_for_element(self._session_balance))

    def purchase(self, default_card="1881"):
        pricing_page = Pricing(self.driver)

        pricing_page.click_pricing_nav_link()
        self.assertIsNotNone(pricing_page.click_unlimited_session_option())
        if not pricing_page.click_default_card(default_card) is None:
            pricing_page.click_purchase_button()
            self.assertIsNotNone(
                pricing_page.driver.wait_for_element(
                    self._unlimited_session_balance, timeout=20
                )
            )
        else:
            pass

    def test(self):
        # Login
        self.login("trang+02@gotitapp.co", "1234aA")

        self.purchase()

        time.sleep(2)


if __name__ == "__main__":
    unittest.main()

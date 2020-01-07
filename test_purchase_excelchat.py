import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from driver_wrapper import DriverWrapper
from pages.login import Login
from pages.pricing import Pricing
from selenium.webdriver.support import expected_conditions as EC
import time


class PurchaseExcelchat(unittest.TestCase):
    def setUp(self):
        base_url = "https://www.got-it.tech/solutions/excel-chat"
        self.driver = webdriver.Chrome()
           
        # Launch
        self.driver.maximize_window()
        self.driver.get(base_url)

    _session_balance = {
        "locator": "test-session-balance-header-button", 
        "by": By.ID
    }
    _unlimited_session_balance = {
        "locator": '//*[@id="test-session-balance-header-button"]/strong[text()="unlimited"]',
        "by": By.XPATH
    }

    def login(self, email, password):
        login_page = Login(self.driver)

        try: 
            #self.driver.find_element(By.ID, "test-login-button").click()
            login_page.click_element(login_page._login_modal_button)
            self.assertIsNotNone(
                login_page.wait_for_element(login_page._login_modal)
            )
            login_page.enter_email(email)
            login_page.enter_password(password)
            login_page.click_login_submit_button()
            login_page.wait_for_element(login_page._login_modal, invisible=True)
            self.assertTrue(
                login_page.wait_for_element(self._session_balance)
            )
            return True
        except:
            return False

    def purchase(self, default_card="1881"):
        pricing_page = Pricing(self.driver)

        try:
            pricing_page.click_pricing_nav_link()
            self.assertIsNotNone(
                pricing_page.click_unlimited_session_option()
            )
            if not pricing_page.click_default_card(default_card) is None:
                pricing_page.click_purchase_button()
                self.assertIsNotNone(
                    pricing_page.wait_for_element(
                        self._unlimited_session_balance, timeout=20)
                )
            else:
                pass
            return True
        except Exception as e:
            print(e)
            return False

    def test(self):
        # Login
        login_result = self.login("trang+99@gotitapp.co", "1234aA")
        self.assertTrue(login_result)

        purchase_result = self.purchase()
        self.assertTrue(purchase_result)

        time.sleep(2)


if __name__ == '__main__':
    unittest.main()

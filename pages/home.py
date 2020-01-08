from driver_wrapper import DriverWrapper
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest


class Home:
    def __init__(self, driver):
        self.driver = DriverWrapper(driver)

    # Locators
    # Login
    _login_modal_button = {"locator": "test-login-button", "by": By.ID}

    # Pricing
    _pricing_nav_link = {"locator": "pricing-navlink-landing", "by": By.ID}
    _session_options = {
        "locator": "div.gi-coverPricing-Inner div.gi-pricingItem",
        "by": By.CLASS_NAME,
    }
    _unlimited_session_option = {
        "locator": '//div[text()="Unlimited Sessions"]/parent::div/div[@class="gi-pricingItem-Button"]',
        "by": By.XPATH,
    }

    # Session Balance
    _session_balance = {"locator": "test-session-balance-header-button", "by": By.ID}

    def click_login_modal_button(self):
        self.driver.click_element(self._login_modal_button)

    def is_session_balance_present(self):
        return self.driver.is_present_element(self._session_balance)

    def is_session_balance_unlimited(self):
        return "unlimited" in self.driver.wait_for_element(self._session_balance).text

    def click_pricing_nav_link(self):
        return self.driver.click_element(self._pricing_nav_link)

    def click_unlimited_session_option(self):
        self.driver.click_element(self._unlimited_session_option)

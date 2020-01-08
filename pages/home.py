from driver_wrapper import DriverWrapper
from selenium.webdriver.common.by import By
import unittest


class Home:
    def __init__(self, driver):
        self.driver = DriverWrapper(driver)

    # Locators
    # Login
    _login_modal_button = {"locator": "test-login-button", "by": By.ID}
    _login_modal = {"locator": "modal-login", "by": By.ID}

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
    _unlimited_session_balance = {
        "locator": '//*[@id="test-session-balance-header-button"]/strong[text()="unlimited"]',
        "by": By.XPATH,
    }

    def click_login_modal_button(self):
        self.driver.click_element(self._login_modal_button)
        assert self.driver.wait_for_element(self._login_modal), "Login modal is visible"

    def is_session_balance_found(self):
        self.driver.wait_for_element(self._session_balance)
        return True

    def click_pricing_nav_link(self):
        return self.driver.click_element(self._pricing_nav_link)

    def click_unlimited_session_option(self):
        return self.driver.click_element(self._unlimited_session_option)


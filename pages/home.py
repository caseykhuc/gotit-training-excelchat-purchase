from driver_wrapper import DriverWrapper
from selenium.webdriver.common.by import By
import unittest


class Home:
    def __init__(self, driver):
        self.driver = DriverWrapper(driver)

    # Locators
    _session_balance = {"locator": "test-session-balance-header-button", "by": By.ID}
    _unlimited_session_balance = {
        "locator": '//*[@id="test-session-balance-header-button"]/strong[text()="unlimited"]',
        "by": By.XPATH,
    }
    _terminate_subscription_button = {
        "locator": "terminateSubscriptionButton",
        "by": By.ID,
    }
    _sign_in_admin = {
        "locator": "div.col-md-4.landing-main button.btn-google",
        "by": By.CSS_SELECTOR,
    }
    _email_field = {
        "locator": "input[name='identifier']",
        "by": By.CSS_SELECTOR,
    }
    _next_button = {"locator": "identifierNext", "by": By.ID}
    _password_field = {
        "locator": "input[name='password']",
        "by": By.CSS_SELECTOR,
    }
    _password_next_button = {"locator": "passwordNext", "by": By.ID}
    _admin_menu = {"locator": "hi-menu", "by": By.CLASS_NAME}
    _confirm_terminate_button = {
        "locator": "div.modal.fade.in button.btn.btn-primary",
        "by": By.CSS_SELECTOR,
    }

    def click_sign_in_admin(self, email, password):
        sign_in = self.driver.click_element(self._sign_in_admin)
        self.driver.switch_tab(1)
        self.driver.send_keys(email, self._email_field).send_keys()
        self.driver.click_element(self._next_button)
        self.driver.send_keys(password, self._password_field)
        self.driver.click_element(self._password_next_button)
        self.driver.switch_tab()
        self.driver.wait_for_element(self._admin_menu, timeout=15)

    def click_terminate_subscription_button(self):
        self.driver.click_element(self._terminate_subscription_button)
        self.driver.click_element(self._confirm_terminate_button)

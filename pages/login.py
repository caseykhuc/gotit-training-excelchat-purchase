from driver_wrapper import DriverWrapper
from selenium.webdriver.common.by import By
import unittest

class Login(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_modal = {"locator": "modal-login", "by": By.ID}
    _login_modal_button = {"locator": "test-login-button", "by": By.ID}
    _email_field = {"locator": "input[name='email']", "by": By.CSS_SELECTOR}
    _password_field = {"locator": "input[name='password']", "by": By.CSS_SELECTOR}
    _login_submit_button = {"locator": "button#login-button", "by": By.CSS_SELECTOR}
    
    def click_login_modal_button(self):
        self.click_element(
            self._login_modal_button
        )

    def enter_email(self, email):
        self.send_keys(
            email, 
            self._email_field
        )

    def enter_password(self, password):
        self.send_keys(
            password, self._password_field,
        )

    def click_login_submit_button(self):
        self.click_element(
            self._login_submit_button
        )
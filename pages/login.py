from driver_wrapper import DriverWrapper
from selenium.webdriver.common.by import By
import unittest


class Login:
    def __init__(self, driver):
        self.driver = DriverWrapper(driver)

    # Locators
    _login_modal = {"locator": "modal-login", "by": By.ID}
    _email_field = {"locator": "input[name='email']", "by": By.CSS_SELECTOR}
    _password_field = {"locator": "input[name='password']", "by": By.CSS_SELECTOR}
    _login_submit_button = {"locator": "button#login-button", "by": By.CSS_SELECTOR}

    def enter_email(self, email):
        self.driver.send_keys(email, Login._email_field)

    def enter_password(self, password):
        self.driver.send_keys(
            password, Login._password_field,
        )

    def click_login_submit_button(self):
        self.driver.click_element(Login._login_submit_button)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_submit_button()

    def is_login_modal_present(self):
        return self.driver.is_present_element(Login._login_modal)

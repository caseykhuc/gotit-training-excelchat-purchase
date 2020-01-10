from pages.common.base_modal import BaseModal
from selenium.webdriver.common.by import By


class Locators:
    LOGIN_MODAL = {"locator": "modal-login", "by": By.ID}
    EMAIL_FIELD = {"locator": "input[name='email']", "by": By.CSS_SELECTOR}
    PASSWORD_FIELD = {"locator": "input[name='password']", "by": By.CSS_SELECTOR}
    LOGIN_SUBMIT_BUTTON = {"locator": "button#login-button", "by": By.CSS_SELECTOR}


class Login(BaseModal):
    def enter_email(self, email):
        self.driver.send_keys(email, Locators.EMAIL_FIELD)

    def enter_password(self, password):
        self.driver.send_keys(
            password, Locators.PASSWORD_FIELD,
        )

    def click_login_submit_button(self):
        self.driver.click_element(Locators.LOGIN_SUBMIT_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_submit_button()

    def is_present(self):
        return self.driver.is_present_element(Locators.LOGIN_MODAL)

from pages.common.base_page import BasePage
from locators import LoginModalLocators as Locators


class Login(BasePage):
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

    def is_login_modal_present(self):
        return self.driver.is_present_element(Locators.LOGIN_MODAL)

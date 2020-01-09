from pages.common.base_page import BasePage
from utility.locators import HomePageLocators as Locators


class Home(BasePage):
    def click_login_modal_button(self):
        self.driver.click_element(Locators.LOGIN_MODAL_BUTTON)

    def is_session_balance_present(self):
        return self.driver.is_present_element(Locators.SESSION_BALANCE)

    def contains_text_session_balance(self, text):
        return self.driver.contains_text_element(text, Locators.SESSION_BALANCE)

    def click_pricing_nav_link(self):
        return self.driver.click_element(Locators.PRICING_NAV_LINK)

    def click_unlimited_session_option(self):
        self.driver.click_element(Locators.UNLIMITED_SESSION_OPTION)

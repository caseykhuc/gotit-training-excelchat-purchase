from pages.common.base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:
    # Login
    LOGIN_MODAL_BUTTON = {"locator": "test-login-button", "by": By.ID}

    # Purchase
    PRICING_NAV_LINK = {"locator": "pricing-navlink-landing", "by": By.ID}
    SESSIONS_OPTIONS = {
        "locator": "div.gi-coverPricing-Inner div.gi-pricingItem",
        "by": By.CLASS_NAME,
    }
    UNLIMITED_SESSION_OPTION = {
        "locator": '//div[text()="Unlimited Sessions"]/parent::div/div[@class="gi-pricingItem-Button"]',
        "by": By.XPATH,
    }

    # Session Balance
    SESSION_BALANCE = {"locator": "test-session-balance-header-button", "by": By.ID}


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

    def is_present(self):
        pass

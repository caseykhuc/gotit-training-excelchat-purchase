from driver_wrapper import DriverWrapper
from selenium.webdriver.common.by import By
import unittest


class Pricing:
    def __init__(self, driver):
        self.driver = DriverWrapper(driver)

    # Locators
    _pricing_nav_link = {"locator": "pricing-navlink-landing", "by": By.ID}
    _session_options = {
        "locator": "div.gi-coverPricing-Inner div.gi-pricingItem",
        "by": By.CLASS_NAME,
    }
    _unlimited_session_option = {
        "locator": '//div[text()="Unlimited Sessions"]/parent::div/div[@class="gi-pricingItem-Button"]',
        "by": By.XPATH,
    }
    _default_card = {
        "locator": '//div[@data-braintree-id="methods"]//div[contains(text(), "{default_card}")]',
        "by": By.XPATH,
    }
    _purchase_button = {
        "locator": "div#modal-payment-subscription-engine div.modal-footer button.gi-Button",
        "by": By.CSS_SELECTOR,
    }

    def click_pricing_nav_link(self):
        return self.driver.click_element(self._pricing_nav_link)

    def click_unlimited_session_option(self):
        return self.driver.click_element(self._unlimited_session_option)

    def click_default_card(self, default_card):
        self._default_card["locator"] = self._default_card["locator"].format(
            default_card=default_card
        )
        return self.driver.click_element(self._default_card)

    def click_purchase_button(self):
        return self.driver.click_element(self._purchase_button)

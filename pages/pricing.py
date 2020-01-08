from driver_wrapper import DriverWrapper
from selenium.webdriver.common.by import By
import unittest


class Pricing:
    def __init__(self, driver):
        self.driver = DriverWrapper(driver)

    # Locators
    _purchase_modal = {"locator": "modal-payment-subscription-engine", "by": By.ID}
    _default_card = {
        "locator": '//div[@data-braintree-id="methods"]//div[contains(text(), "{default_card}")]',
        "by": By.XPATH,
    }
    _purchase_button = {
        "locator": "div#modal-payment-subscription-engine div.modal-footer button.gi-Button",
        "by": By.CSS_SELECTOR,
    }

    def click_default_card(self, default_card):
        self._default_card["locator"] = Pricing._default_card["locator"].format(
            default_card=default_card
        )
        return self.driver.click_element(Pricing._default_card)

    def click_purchase_button(self):
        return self.driver.click_element(Pricing._purchase_button)

    def purchase(self, default_card):
        self.click_default_card(default_card)
        self.click_purchase_button()

    def is_purchase_modal_present(self):
        return self.driver.is_present_element(Pricing._purchase_modal)

    def wait_for_finishing(self):
        self.driver.wait_for_element(
            Pricing._purchase_modal, invisible=True, timeout=30
        )

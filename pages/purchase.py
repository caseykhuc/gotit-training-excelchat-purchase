from pages.common.base_page import BasePage
from locators import PurchaseModalLocators as Locators


class Purchase(BasePage):
    _DEFAULT_CARD_TIMEOUT = 20
    _FINISHING_TIMEOUT = 60

    def click_default_card(self, default_card):
        DEFAULT_CARD = Locators.DEFAULT_CARD
        DEFAULT_CARD["locator"] = Locators.DEFAULT_CARD["locator"].format(
            default_card=default_card
        )
        return self.driver.click_element(
            DEFAULT_CARD, timeout=Purchase._DEFAULT_CARD_TIMEOUT
        )

    def click_purchase_button(self):
        return self.driver.click_element(Locators.PURCHASE_BUTTON)

    def purchase(self, default_card):
        self.click_default_card(default_card)
        self.click_purchase_button()

    def is_purchase_modal_present(self):
        return self.driver.is_present_element(Locators.PURCHASE_MODAL)

    def wait_for_finishing(self):
        self.driver.wait_for_element(
            Locators.PURCHASE_MODAL, invisible=True, timeout=Purchase._FINISHING_TIMEOUT
        )

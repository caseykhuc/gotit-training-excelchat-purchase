from driver_wrapper import DriverWrapper
from selenium.webdriver.common.by import By
import unittest

class Pricing(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _pricing_nav_link = {"locator": "pricing-navlink-landing", "by": By.ID}
    _session_options = {"locator": "div.gi-coverPricing-Inner div.gi-pricingItem", "by": By.CLASS_NAME}
    _unlimited_session_option = {
        "locator": '//div[text()="Unlimited Sessions"]/parent::div/div[@class="gi-pricingItem-Button"]',
        "by": By.XPATH
    }

    _email_field = {"locator": "input[name='email']", "by": By.CSS_SELECTOR}
    _password_field = {"locator": "input[name='password']", "by": By.CSS_SELECTOR}
    _login_submit_button = {"locator": "button#login-button", "by": By.CSS_SELECTOR}

    def click_pricing_nav_link(self):
        self.click_element(
            self._pricing_nav_link
        )

    def click_unlimited_session_option(self):
        self.click_element(
            self._unlimited_session_option
        )

   
        """ # Navigate to Pricing page
        driver.find_element(By.ID, 'pricing-navlink-landing').click()

        # Invoke payment modal
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "gi-coverPricing-Inner")))
        unlimited_sessions_option = driver.find_element(By.CSS_SELECTOR, "div.gi-coverPricing-Inner div.gi-pricingItem")\
            .find_element(By.XPATH, '//div[text()="Unlimited Sessions"]/parent::div')
        unlimited_sessions_option.find_element(By.CSS_SELECTOR, "div.gi-pricingItem-Button").click()

        # Handle payment method
        payment_modal = wait.until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, 'div.modal-content'
            )))
        try:
            methods = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.braintree-loaded div.braintree-method'))
            )
            methods.find_element(By.XPATH, '//div[contains(text(), "1881")]').click()

        except NoSuchElementException:
            payment_modal.find_element(
                By.XPATH, '//span[text()="Choose another way to pay"]'
            ).click()
            payment_modal.find_element(By.CSS_SELECTOR, 'div.braintree-option__card').click()
        finally:
            payment_modal.find_element(By.CSS_SELECTOR, 'div.modal-footer button.gi-Button').click()
            # assert something """
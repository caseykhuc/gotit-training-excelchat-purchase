import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from driver_wrapper import DriverWrapper
from pages.login import Login
from pages.pricing import Pricing
from selenium.webdriver.support import expected_conditions as EC
import time


class PurchaseExcelchat(unittest.TestCase):
    def setUp(self):
        base_url = "https://www.got-it.tech/solutions/excel-chat"
        self.driver = webdriver.Chrome()
           
        # Launch
        self.driver.maximize_window()
        self.driver.get(base_url)

    _session_balance = {"locator": "test-session-balance-header-button", "by": By.ID}

    def login(self, email, password):
        login_page = Login(self.driver)

        try: 
            #self.driver.find_element(By.ID, "test-login-button").click()
            login_page.click_element(login_page._login_modal_button)
            login_page.wait_for_element(login_page._login_modal)
            login_page.enter_email(email)
            login_page.enter_password(password)
            login_page.click_login_submit_button()
            login_page.wait_for_element(login_page._login_modal, invisible=True)
            self.assertTrue(
                login_page.wait_for_element(
                    self._session_balance
                    ))
            return True
        except:
            return False

    def purchase(self, default_card="1881"):
        pricing_page = Pricing(self.driver)

        try:
            pricing_page.click_pricing_nav_link()
            pricing_page.click_unlimited_session_option()
            return True
        except:
            return False

    def test(self):
        # Login
        login_result = self.login("trang+99@gotitapp.co", "1234aA")
        self.assertTrue(login_result)

        purchase_result = self.purchase()
        self.assertTrue(purchase_result)

        """driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Navigate to Pricing page
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
            # assert something"""

        time.sleep(2)


if __name__ == '__main__':
    unittest.main()

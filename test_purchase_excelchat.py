import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from driver_wrapper import DriverWrapper
from pages.log_in import LogIn
from selenium.webdriver.support import expected_conditions as EC
import time


class PurchaseExcelchat(unittest.TestCase):
    def setUp(self):
        base_url = "https://www.got-it.tech/solutions/excel-chat"
        self.driver = webdriver.Chrome()
           
        # Launch
        self.driver.maximize_window()
        self.driver.get(base_url)

    def test(self):
        # Login
        login_page = LogIn(self.driver)
        self.assertTrue(login_page.login("trang+99@gotitapp.co", "1234aA"))

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

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()

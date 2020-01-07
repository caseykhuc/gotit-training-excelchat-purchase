from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By

class DriverWrapper:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10, pollFrequency=0.5, invisible=False):
        element = None
        try:
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            if invisible:
                element = wait.until_not(EC.visibility_of_element_located((locator['by'], locator['locator'])))    
            else:
                element = wait.until(EC.visibility_of_element_located((locator['by'], locator['locator'])))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element
    
    def click_element(self, locator):
        try:
            element = self.get_element(locator)
            element.click()
        except:
            print_stack()

    def send_keys(self, data, locator):
        try:
            element = self.get_element(locator)
            element.send_keys(data)
        except:
            print_stack()

    def get_element(self, locator):
        element = None
        try:
            element = self.driver.find_element(locator['by'], locator['locator'])
        except:
            print("Element not found with locator: " + locator)
        return element

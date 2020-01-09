from utility.driver_wrapper import DriverWrapper


class BasePage:
    def __init__(self, driver):
        self.driver = DriverWrapper(driver)

from utility.driver_wrapper import DriverWrapper
from abc import ABC, abstractmethod


class BaseModal(ABC):
    def __init__(self, driver):
        self.driver = DriverWrapper(driver)

    @abstractmethod
    def is_present(self):
        pass

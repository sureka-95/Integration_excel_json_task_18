# features/pages/base_page.py
# import necessary libraries and modules
# import expected_conditions and By from selenium.webdriver
# import WebDriverWait from selenium for waiting for elements
# import custom exceptions for handling errors
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

# BasePage class to encapsulate common functionalities for all pages
class BasePage:
    
    # BasePage constructor to initialize the driver and wait
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

# Method to wait for an element to be present
    def wait_for_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element not found: {locator}")
        
# Method to wait for an element to be clickable
    def wait_for_element_clickable(self, locator):
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise Exception(f"Element not clickable: {locator}")
        
# Method to click an element after scrolling into view
    def click(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

#  method to enter text into an input field
    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

#   method to get text from an element
    def get_text(self, locator):
        return self.wait_for_element(locator).text
    
#   method to check if an element is visible
    def is_element_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

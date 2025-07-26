
#   features/pages/login_page.py
# import necessary libraries and modules
# import custom exceptions for handling login errors
# import expected_conditions and By from selenium.webdriver
# import WebDriverWait from selenium for waiting for elements
# import BasePage class for common page functionalities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException
from features.utils.custom_exceptions import LoginFailedException

# LoginPage class inherits from BasePage for common functionalities
class LoginPage(BasePage):
    # locators for username, password, login button, and error message
    USERNAME_INPUT = (By.XPATH, "//input[@id=':r0:']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id=':r1:']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MSG = (By.XPATH, "//p[contains(@id=, 'helper-text']")

# methods for interacting with the login page
    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)
     
# method to enter password
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)      
       
# method to click the login button
    def click_login(self):
        self.click(self.LOGIN_BUTTON)

# method to get the error message after a failed login attempt
    def get_error_message(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MSG))
            return element.text
        except TimeoutException:
            return LoginFailedException("Error message not found")
 # method to check if the login button is enabled       
    def is_login_button_enabled(self):
        return self.wait_for_element(self.LOGIN_BUTTON).is_enabled()
# methods to check visibility of username and password fields
    def is_username_visible(self):
        return self.wait_for_element(self.USERNAME_INPUT).is_displayed()

    def is_password_visible(self):
        return self.wait_for_element(self.PASSWORD_INPUT).is_displayed()

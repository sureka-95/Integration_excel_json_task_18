# features/pages/dashboard_page.py
# import necessary libraries and modules
# import expected_conditions and By from selenium.webdriver
# import WebDriverWait from selenium for waiting for elements
# import BasePage class for common page functionalities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
# DashboardPage class inherits from BasePage for common functionalities
class DashboardPage(BasePage):
# methods for interacting with the dashboard page
   def click_logout(self):
         profile_icon = WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable((By.XPATH, "//img[@id='profile-click-icon']"))
         )
         profile_icon.click()

         logout_btn = WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Log out']"))
        )
         logout_btn.click()  

           # Wait until we're redirected to login page
         WebDriverWait(self.driver, 10).until(
            EC.url_contains("login")
         )

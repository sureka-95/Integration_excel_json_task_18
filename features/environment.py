# features/environment.py
# import necessary libraries and modules
# import os for environment variables
# import time for sleep functionality
# import selenium webdriver for browser automation
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import NoAlertPresentException, WebDriverException
# from dotenv import load_dotenv for loading environment variables from .env file

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoAlertPresentException, WebDriverException
from dotenv import load_dotenv
import os
import time

# before_scenario and after_scenario hooks for Behave framework
def before_scenario(context, scenario):
    print(f"\n--- Starting Scenario: {scenario.name} ---")
    load_dotenv(override=True)
    print("Loaded from .env:", os.getenv("USERNAME"))

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")  # Run in incognito mode
    options.add_argument("--disable-popup-blocking")  # Disable popup blocking

    # Create WebDriver instance
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(10)  # Implicit wait

    # Optional: wait a moment for potential alerts
    time.sleep(2)


# quitting the driver after each scenario
def after_scenario(context, scenario):
    print(f"--- Ending Scenario: {scenario.name} ---\n")
    if context.driver:
        context.driver.quit()

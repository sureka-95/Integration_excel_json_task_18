# features/steps/login_steps.py
# import necessary libraries and modules
# from behave import given, when, then
# import os for environment variables
# import time for sleep functionality
# import selenium webdriver for browser automation
# import LoginPage and DashboardPage from features/pages
# import custom exceptions from features/utils/custom_exceptions
# import expected_conditions and By from selenium.webdriver
# import WebDriverWait from selenium for waiting for elements

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.login_page import LoginPage
from features.pages.dashboard_page import DashboardPage
from selenium.common.exceptions import TimeoutException
import os
import time

# given step to open the login page
@given('I open the login page')
# method to open the login page
def step_open_login(context):
    context.driver.get("https://v2.zenclass.in/login")# URL of the login page
    context.login_page = LoginPage(context.driver)  # Initialize LoginPage with the driver

# when steps for entering credentials and clicking login  
@when('I enter valid credentials')
# method to enter valid credentials
def step_valid_login(context):
    # Load environment variables for username and password
    # using dotenv to load from .env file
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    # Print the username for debugging
    print("Using username:", username)
    # Enter the username and password using the LoginPage methods
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
# invalid credentials step
@when('I enter invalid credentials')
# method to enter invalid credentials
def step_invalid_login(context):
    # Enter invalid credentials directly
    context.login_page.enter_username("invalid@example.com")
    context.login_page.enter_password("wrongpass")

# when step to click the login button
@when('I click the login button')
# method to click the login button
def step_click_login(context):
    context.login_page.click_login()
    time.sleep(3)
# then step to verify redirection to dashboard
@then('I should be redirected to the dashboard')
#   method to verify redirection to the dashboard
def step_dashboard(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[@class='header-name']"))
    ) # Check for an element that indicates successful login
    # Initialize DashboardPage with the driver
    context.login_page = LoginPage(context.driver)
    context.dashboard_page = DashboardPage(context.driver)
    assert "dashboard" in context.driver.current_url, "Expected to be on the dashboard page"
    # assertion that the URL contains "dashboard"

# then step to verify error message for invalid login
@then('I should see an error message')
# method to verify error message for invalid login
def step_error_message(context):
    #try block to handle potential exceptions
    try:
        error = WebDriverWait(context.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//p[@id=':r1:-helper-text']"))
        )
        assert error.is_displayed()
        # Print the error message for debugging
    except Exception as e:
        print("Error message not found after invalid login.")
        raise e

# then step to verify visibility of username and password fields
@then('I should see username and password input fields')
# method to verify visibility of username and password fields
def step_fields(context):
    # assert username and password fields are visible
    assert context.login_page.is_username_visible()
    assert context.login_page.is_password_visible()

# then step to verify login button is enabled
@then('I should see the login button enabled')
# method to verify login button is enabled
def step_button_enabled(context):
     assert context.login_page.is_login_button_enabled(), "Login button should be enabled"

# given step to ensure user is logged in with valid credentials
@given('I am logged in with valid credentials')
# method to ensure user is logged in with valid credentials
def step_logged_in(context):
    # use the previously defined steps to log in
    step_open_login(context)
    step_valid_login(context)
    step_click_login(context)
    # Wait for the dashboard to load
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[@class='header-name']"))
    )
    context.dashboard_page = DashboardPage(context.driver)

# when step to click the logout button
@when('I click the logout button')
# method to click the logout button
def step_click_logout(context):
    # try and except block to handle potential exceptions
    try:
        context.dashboard_page.click_logout()# use the DashboardPage method to click logout
    except Exception as e:
        print("Logout button click failed.")
        raise e

# then step to verify redirection to login page after logout
@then('I should be redirected to the login page')
# method to verify redirection to login page after logout
def step_back_to_login(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='login-text fw-600 fs-normal']"))
    )
    assert "login" in context.driver.current_url
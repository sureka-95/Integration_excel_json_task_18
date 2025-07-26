# feature: Login functionality for GuviZenClass portal
# contains scenarios for successful and unsuccessful login, field validation, and logout functionality.
# scenarios are defined in Gherkin syntax.
# given, when, then steps are implemented in Python using Selenium WebDriver.

Feature: Login functionality for GuviZenClass portal

  Scenario: Successful Login
    Given I open the login page
    When I enter valid credentials
    And I click the login button
    Then I should be redirected to the dashboard

  Scenario: Unsuccessful Login
    Given I open the login page
    When I enter invalid credentials
    And I click the login button
    Then I should see an error message

  Scenario: Validate Username and Password fields
    Given I open the login page
    Then I should see username and password input fields

  Scenario: Validate Submit Button
    Given I open the login page
    Then I should see the login button enabled

  Scenario: Validate Logout Button Functionality
    Given I am logged in with valid credentials
    When I click the logout button
    Then I should be redirected to the login page

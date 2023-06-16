Feature: About Us Page
  Background:
    Given open the blaze application url

  Scenario: verify about us page
    When click on the login button
    Then login pop up page should display
    When user enter valid credentials
    And click on the login button present on login pop up
    Then user should logged in
    When click on about us link present in home page
    Then about us page should display
    Then click on close button present in about us page
    Then user should direct back to home page


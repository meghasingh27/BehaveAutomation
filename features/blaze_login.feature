


Feature: Login page

  Background:
    Given open the blaze application url

  Scenario: verify login functionality with valid credentials
    When click on the login button
    Then login pop up page should display
    When user enter valid credentials
    And click on the login button present on login pop up
    Then user should logged in


  Scenario: verify login functionality with valid credentials using parameter concept
    When click on the login button
    Then login pop up page should display
    When user enter valid email as "User12Demo34" and valid password as "User@1234"
    And click on the login button present on login pop up
    Then user should logged in


  Scenario Outline: verify login functionality with valid credentials using DDT concept
    When click on the login button
    Then login pop up page should display
    When user enter valid email id as "<email>" and valid password as "<password>"
    And click on the login button present on login pop up
    Then user should logged in
    Examples:
      | email            | password        |
      | User12Demo34     | User@1234       |
      #| User12Demo       | User@12         |


  Scenario: verify login functionality with invalid credentials
    When click on the login button
    Then login pop up page should display
    When user enter invalid credentials
    And click on the login button present on login pop up
    Then user should not be able to login


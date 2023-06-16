


Feature: Contact page

  Background:
    Given open the blaze application url

  Scenario: verify contact page
    #Given open the blaze application url
    When click on the login button
    Then login pop up page should display
    When user enter valid credentials
    And click on the login button present on login pop up
    Then user should logged in
    When click on the contact button
    Then contact pop up should display
    Then user enter all the details
    And click on the send message button
    Then thanks saying pop up should display

@smoke
  Scenario Outline: verify contact page with DDT concept
    #Given open the blaze application url
    When click on the login button
    Then login pop up page should display
    When user enter valid email id as "<email>" and valid password as "<password>"
    And click on the login button present on login pop up
    Then user should logged in
    When click on the contact button
    Then contact pop up should display
    Then user enter all the below details
        | contact_email    | contact_name | message           |
        | demo             | User12Demo34 | Hello store.....  |
        #| demoUser         | UserDemo     | Hello World.....  |
    And click on the send message button
    Then thanks saying pop up should display
      Examples:
      | email            | password        |
      | User12Demo34     | User@1234       |



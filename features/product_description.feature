Feature: Product Description
  Background:
    Given open the blaze application url

    Scenario: Verification of Asus Product under Laptop Category
      When click on the login button
      Then login pop up page should display
      When user enter valid credentials
      And click on the login button present on login pop up
      Then user should logged in
      When click on laptop category
      And click on next button
      Then click on ASUS Full HD item
      Then product description page should display
      And check product description as per requirement
      Then click on add to cart
      Then product added pop page should display product text
      When product added click on cart page
      Then check asus item description on cart page

    @smoke
    Scenario: Verification of placing order of an item
      When click on the login button
      Then login pop up page should display
      When user enter valid credentials
      And click on the login button present on login pop up
      Then user should logged in
      When click on cart page
      Then verify that delete button is visible on the page
      When delete button is visible click on place order
      Then verify place order page
      When user enter valid credentials to place order
      Then click on purchase button
      Then verify that thank you pop is displayed
      Then print the order id and click on ok button
      Then user should direct back to main page


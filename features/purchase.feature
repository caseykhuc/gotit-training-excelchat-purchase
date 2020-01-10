@fixture.browser.chrome
Feature: As a user, I want to purchase the Unlimited subscription

  Scenario: User purchases successfully with a default card
    Given a web browser is at the Asker page

    When I click on the login button
    Then I should see the login modal

    When I login
    Then I should see the session balance info

    When I click on the pricing nav link
    When I click on Unlimited sessions option
    Then I should see the purchase modal

    When I purchase with the default card
    When I wait for the purchase to finish
    Then I should see "unlimited" in session balance info
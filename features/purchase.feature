@fixture.browser.chrome
Feature: Purchase Unlimited Sessions

  Scenario: Success purchase
    Given a web browser is at the Asker page
    When the user clicks on login button
    Then login modal is visible

    When the user logins
    Then session balance info is shown

    When the user clicks on Pricing nav link
    When the user clicks on Unlimited sessions option
    Then purchase modal is visible

    When the user purchase with the default card
    When the user wait for purchase finishes
    Then session balance should be unlimited
from behave import *
from pages.login import Login
from pages.purchase import Purchase
from pages.home import Home

# Invoke Login Modal
@given("a web browser is at the Asker page")
def step_impl(context):
    # Launch Asker
    asker_url = context.config.Url.ASKER_URL
    context.browser.get(asker_url)


@when("I click on the login button")
def step_impl(context):
    Home(context.browser).click_login_modal_button()


@then("I should see the login modal")
def step_impl(context):
    assert Login(context.browser).is_present()


# Login
@when("I login")
def step_impl(context):
    email = context.config.AskerAccount.EMAIL
    password = context.config.AskerAccount.PASSWORD
    Login(context.browser).login(email, password)


@then("I should see the session balance info")
def step_impl(context):
    assert Home(context.browser).is_session_balance_present()


# Invoke Purchase Modal
@when("I click on the pricing nav link")
def step_impl(context):
    Home(context.browser).click_pricing_nav_link()


@when("I click on Unlimited sessions option")
def step_impl(context):
    Home(context.browser).click_unlimited_session_option()


@then("I should see the purchase modal")
def step_impl(context):
    assert Purchase(context.browser).is_present()


# Purchase
@when("I purchase with the default card")
def step_impl(context):
    default_card = context.config.AskerAccount.DEFAULT_CARD
    Purchase(context.browser).purchase(default_card)


@when("I wait for the purchase to finish")
def step_impl(context):
    Purchase(context.browser).wait_for_finishing()


@then('I should see "{text}" in session balance info')
def step_impl(context, text):
    assert Home(context.browser).contains_text_session_balance(text)


from behave import *
from pages.login import Login
from pages.purchase import Purchase
from pages.home import Home

# Invoke Login Modal
@given("a web browser is at the Asker page")
def step_impl(context):
    context.browser.maximize_window()
    # Launch Asker
    asker_url = context.config.Url.ASKER_URL.value
    context.browser.get(asker_url)


@when("the user clicks on login button")
def step_impl(context):
    Home(context.browser).click_login_modal_button()


@then("login modal is visible")
def step_impl(context):
    assert Login(context.browser).is_login_modal_present()


# Login
@when("the user logins")
def step_impl(context):
    email = context.config.AskerAccount.EMAIL.value
    password = context.config.AskerAccount.PASSWORD.value
    Login(context.browser).login(email, password)


@then("session balance info is shown")
def step_impl(context):
    assert Home(context.browser).is_session_balance_present()


# Invoke Purchase Modal
@when("the user clicks on Pricing nav link")
def step_impl(context):
    Home(context.browser).click_pricing_nav_link()


@when("the user clicks on Unlimited sessions option")
def step_impl(context):
    Home(context.browser).click_unlimited_session_option()


@then("purchase modal is visible")
def step_impl(context):
    assert Purchase(context.browser).is_purchase_modal_present()


# Purchase
@when("the user purchase with the default card")
def step_impl(context):
    default_card = context.config.AskerAccount.DEFAULT_CARD.value
    Purchase(context.browser).purchase(default_card)


@when("the user wait for purchase finishes")
def step_impl(context):
    Purchase(context.browser).wait_for_finishing()


@then("session balance should be unlimited")
def step_impl(context):
    assert Home(context.browser).contains_text_session_balance("unlimited")


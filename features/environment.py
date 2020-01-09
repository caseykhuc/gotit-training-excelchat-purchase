from behave.fixture import fixture, use_fixture
from clean_up import CleanUp
from selenium import webdriver

# -- FIXTURE:
@fixture
def selenium_browser_chrome(context):
    context.browser = webdriver.Chrome()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


# -- ENVIRONMENT-HOOKS:
def before_all(context):
    use_fixture(selenium_browser_chrome, context)


def after_scenario(context, scenario):
    if scenario.name == "Success purchase":
        CleanUp().terminate_subscription()

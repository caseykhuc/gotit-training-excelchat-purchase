from behave.fixture import fixture, use_fixture
from behave.model import Scenario
from selenium import webdriver
from utility.clean_up import CleanUp

# -- FIXTURE:
@fixture
def selenium_browser_chrome(context):
    context.browser = webdriver.Chrome()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


@fixture
def selenium_browser_firefox(context):
    context.browser = webdriver.Firefox()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


# -- ENVIRONMENT-HOOKS:
def before_all(context):
    userdata = context.config.userdata
    continue_after_failed = userdata.getbool("runner.continue_after_failed_step", False)
    Scenario.continue_after_failed_step = continue_after_failed


def before_tag(context, tag):
    if tag == "fixture.browser.chrome":
        use_fixture(selenium_browser_chrome, context)
    if tag == "fixture.browser.firefox":
        use_fixture(selenium_browser_firefox, context)


def after_scenario(context, scenario):
    if scenario.name == "Success purchase":
        CleanUp().terminate_subscription()

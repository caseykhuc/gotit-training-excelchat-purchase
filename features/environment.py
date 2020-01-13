from behave.fixture import fixture, use_fixture
from behave.model import Scenario
from selenium import webdriver
from utility.clean_up import CleanUp
import config.dev as CONFIG_DEV
import config.staging as CONFIG_STAGING

# -- FIXTURE:
@fixture
def selenium_browser_chrome(context):
    context.browser = webdriver.Chrome()
    yield context.browser


@fixture
def selenium_browser_firefox(context):
    context.browser = webdriver.Firefox()
    yield context.browser


# -- ENVIRONMENT-HOOKS:
""" 
dev:        behave
staging:    behave -D APP_STATE=staging
"""


def before_all(context):
    userdata = context.config.userdata
    continue_after_failed = userdata.getbool("runner.continue_after_failed_step", False)
    Scenario.continue_after_failed_step = continue_after_failed

    APP_STATE = userdata.get("APP_STATE", "dev")
    if APP_STATE == "dev":
        context.config = CONFIG_DEV
    elif APP_STATE == "staging":
        context.config = CONFIG_STAGING


def before_scenario(context, scenario):
    tags = scenario.feature.tags
    if "fixture.browser.chrome" in tags:
        use_fixture(selenium_browser_chrome, context)
    if "fixture.browser.firefox" in tags:
        use_fixture(selenium_browser_firefox, context)
    context.browser.maximize_window()


def after_scenario(context, scenario):
    if "success" in scenario.tags:
        Url = context.config.Url
        AdminAccount = context.config.AdminAccount
        CleanUp().terminate_subscription(Url, AdminAccount)

    context.browser.quit()

from selenium.webdriver.common.by import By


class HomePageLocators:
    # Login modal
    LOGIN_MODAL_BUTTON = {"locator": "test-login-button", "by": By.ID}

    # Purchase
    PRICING_NAV_LINK = {"locator": "pricing-navlink-landing", "by": By.ID}
    SESSIONS_OPTIONS = {
        "locator": "div.gi-coverPricing-Inner div.gi-pricingItem",
        "by": By.CLASS_NAME,
    }
    UNLIMITED_SESSION_OPTION = {
        "locator": '//div[text()="Unlimited Sessions"]/parent::div/div[@class="gi-pricingItem-Button"]',
        "by": By.XPATH,
    }

    # Session Balance
    SESSION_BALANCE = {"locator": "test-session-balance-header-button", "by": By.ID}


class LoginModalLocators:
    LOGIN_MODAL = {"locator": "modal-login", "by": By.ID}
    EMAIL_FIELD = {"locator": "input[name='email']", "by": By.CSS_SELECTOR}
    PASSWORD_FIELD = {"locator": "input[name='password']", "by": By.CSS_SELECTOR}
    LOGIN_SUBMIT_BUTTON = {"locator": "button#login-button", "by": By.CSS_SELECTOR}


class PurchaseModalLocators:
    PURCHASE_MODAL = {"locator": "modal-payment-subscription-engine", "by": By.ID}
    DEFAULT_CARD = {
        "locator": '//div[@data-braintree-id="methods"]//div[contains(text(), "{default_card}")]',
        "by": By.XPATH,
    }
    PURCHASE_BUTTON = {
        "locator": "div#modal-payment-subscription-engine div.modal-footer button.gi-Button",
        "by": By.CSS_SELECTOR,
    }

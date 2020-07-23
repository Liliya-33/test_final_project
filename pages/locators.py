from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_REGISTER = (By.ID, "id_registration-email")
    PASSWORD_1_REGISTER = (By.ID, "id_registration-password1")
    PASSWORD_2_REGISTER = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators():
    BASKET_BUTTON_ON_PAGE = (By.CLASS_NAME, "btn-group")
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")
    NAME_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    ITEMS_IN_BASKET = (By.CLASS_NAME, ".basket-items")
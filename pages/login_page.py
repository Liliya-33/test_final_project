from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_string = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER)
        email_string.send_keys(email)
        password_1_string = self.browser.find_element(*LoginPageLocators.PASSWORD_1_REGISTER)
        password_1_string.send_keys(password)
        password_2_string = self.browser.find_element(*LoginPageLocators.PASSWORD_2_REGISTER)
        password_2_string.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button_register.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Wrong url_login"
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert "login" in self.browser.current_url, "There is not login in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Form_login not found!"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Form_register not found!"

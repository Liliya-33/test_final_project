from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Not found button"
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_book_price(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert price_book == price_basket, "Prices are not same"

    def should_be_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        book_basket = self.browser.find_element(*ProductPageLocators.NAME_BASKET).text
        assert book_name == book_basket, "Name is not same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
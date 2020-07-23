from .base_page import BasePage
from .locators import ProductPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_EMPTY), "Basket is empty should be present."

    def should_be_not_basket_empty(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEMS_IN_BASKET), "Here should be no items in the list "

from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket is not empty'
    
    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_ABOUT_EMPTY_BASKET), 'Basket is not empty'
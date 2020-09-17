from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_page_url()
        self.should_be_add_to_cart_link()
        self.add_to_cart()
    
    def should_be_product_page_url(self):
        assert "?promo=newYear" in self.browser.current_url, 'opened the wrong page'
        
    def should_be_add_to_cart_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "'add to basket' button is not presented"

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET) #_by_css_selector('.btn-add-to-basket')
        add_to_cart_button.click()
    
    def compare_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME) #_by_css_selector('.col-sm-6 > h1')
        product_name_text = product_name.text
        product_name_added = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED) #_by_xpath('//*[@id="messages"]/div[1]/div/strong')
        product_name_added_text = product_name_added.text

        assert product_name_text == product_name_added_text, "added product name differ by product name on page"
    
    def compare_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE) #_by_css_selector('.col-sm-6 .price_color')
        product_price_text = product_price.text
        product_price_added = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ADDED) #_by_xpath('//*[@id="messages"]/div[3]/div/p[1]/strong')
        product_price_added_text = product_price_added.text
        assert product_price_text == product_price_added_text, "product price wich added to basket id differ by product price"

    def shoul_be_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), 'message about add to basket not found' 

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE),  "Success message is presented, but should not be"
    
    def should_wait_until_element_is_not_present(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE) == True, "elemetn is not dissapeared"
from selenium.webdriver.common.by import By
import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestProductCard:
    def test_button_add_to_basket_is_displayed(self, browser):
        browser.get(link)
        button_add = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
        time.sleep(3)
        assert button_add.is_displayed(), 'The add to cart button is missing'
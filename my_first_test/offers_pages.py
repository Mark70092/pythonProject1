from my_first_test.base_pages import BasePages
from my_first_test.locatorss import OffersPageLocatorss


class OffersPages(BasePages):
    def should_be_offers_page(self):
        self.should_be_offers_link()
        self.should_be_book_form()
        self.should_be_book_3_page()

    def should_be_offers_link(self):
        assert 'offers' in self.browser.current_url, 'wrong url'


    def should_be_book_form(self):
        assert self.element_is_present(*OffersPageLocatorss.BOOK_3_FORM)


    def should_be_book_3_page(self):
        self.browser.find_element(*OffersPageLocatorss.BTN_BOOK3).click()

from my_first_test.base_pages import BasePages
from my_first_test.locatorss import MainPageLocatorss


class MainPages(BasePages):

    def should_be_link_to_offers_page(self):
        assert self.element_is_present(*MainPageLocatorss.LINK_TO_OFFERS_PAGE)

    def go_to_offers_page(self):
        self.browser.find_element(*MainPageLocatorss.LINK_TO_OFFERS_PAGE).click()

    def should_be_link_to_books_page(self):
        assert self.element_is_present(*MainPageLocatorss.LINK_TO_BOOKS_PAGE)

    def go_to_books_page(self):
        self.browser.find_element(*MainPageLocatorss.LINK_TO_BOOKS_PAGE).click()

    def should_be_change_language(self):
        self.browser.find_element(*MainPageLocatorss.CHOOSE_LANGUAGE ).click()
        self.browser.find_element(*MainPageLocatorss.BRT_ENG).click()
        self.browser.find_element(*MainPageLocatorss.EXECUTE_BTN).click()

    def should_be_eng_link(self):
        assert 'en-gb' in self.browser.current_url, 'wrong url'








from selenium.common.exceptions import NoSuchElementException
from my_first_test.locatorss import BasePageLocatorss

class BasePages():

    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open_pages(self):
        self.browser.get(self.link)

    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    def element_books_is_present(self):
        assert self.element_is_present(*BasePageLocatorss.BOOKS_ICON)

    def element_execute_is_present(self):
        assert self.element_is_present(*BasePageLocatorss.EXECUTE_ICON)

    def element_offers_is_present(self):
        assert self.element_is_present(*BasePageLocatorss.OFFERS_ICON)

    def user_find(self):
        assert 'q=books' in self.browser.current_url, 'wrong url'










from my_first_test.base_pages import BasePages
from my_first_test.locatorss import BooksPageLocatorss


class Bookspages(BasePages):
    def should_be_books_page(self):
        self.should_be_books_link()
        self.should_be_search_form()
        self.should_be_search_button()
        self.user_is_looking_for()


    def should_be_books_link(self):
        assert 'books' in self.browser.current_url, 'wrong url'

    def should_be_search_form(self):
        assert self.element_is_present(*BooksPageLocatorss.SEARCH_FORM)

    def should_be_search_button(self):
        assert self.element_is_present(*BooksPageLocatorss.SEARCH_BTN)

    def should_be_move_button(self):
        assert self.element_is_present(*BooksPageLocatorss.MOVE_BTN)

    def user_is_looking_for (self, search='books'):
        search_input = self.browser.find_element(*BooksPageLocatorss.SEARCH_FORM)
        search_input.send_keys(search)
        self.browser.find_element(*BooksPageLocatorss.SEARCH_BTN).click()

    def should_be_hacking_book(self):
        self.browser.find_element(*BooksPageLocatorss.HACKING_BOOK).click()
        assert 'hacking_182' in self.browser.current_url, 'wrong url'
        self.browser.find_element(*BooksPageLocatorss.ADD_BTN).click()
        assert self.element_is_present(*BooksPageLocatorss.PROOF_ADD)


















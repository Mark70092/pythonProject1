import pytest
import time
from my_first_test.main_pages import MainPages
from my_first_test.books_pages import Bookspages
from my_first_test.offers_pages import OffersPages


link = 'http://selenium1py.pythonanywhere.com/ru/'

# Тест проверяет, что пользователь может перейти с главной страницы сайта на страницу с книгами
@pytest.mark.smoke
def test_user_can_go_to_books(browser):
    # создает экземпляр главной страницы - Main Page
    page = MainPages(browser, link)
    # открывает страницу
    page.open_pages()
    # проверяет, что на главной странице присутствует ссылка на страницу книг
    page.should_be_link_to_books_page()
    # переходит на страницу с книгами
    page.go_to_books_page()


def test_user_can_go_to_offers(browser):
    page = MainPages(browser, link)
    # открывает страницу
    page.open_pages()
    # проверяет, что на главной странице присутствует ссылка на страницу товаров
    page.should_be_link_to_offers_page()
    # переходит на страницу с товарами
    page.go_to_offers_page()

def test_user_can_go_to_books_and_search(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/category/books_2/'
    page = Bookspages(browser, link)
    time.sleep(5)
    page.open_pages()
    time.sleep(5)
    page.user_is_looking_for(search='books')
    time.sleep(5)
    page.user_find()
    time.sleep(5)
    page.should_be_hacking_book()

def test_user_can_translate(browser):
    page = MainPages(browser, link)
    time.sleep(5)
    page.open_pages()
    time.sleep(5)
    page.should_be_change_language()
    time.sleep(5)
    page.should_be_eng_link()

def test_user_can_add(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/category/books_2/'
    time.sleep(5)
    page = Bookspages(browser, link)
    time.sleep(5)
    page.open_pages()
    time.sleep(5)
    page.should_be_hacking_book()






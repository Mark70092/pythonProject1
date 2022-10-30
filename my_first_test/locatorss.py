from selenium.webdriver.common.by import By


class MainPageLocatorss():
    LINK_TO_OFFERS_PAGE = (By.XPATH, "//*[@id='browse']/li/ul/li[6]/a")
    LINK_TO_BOOKS_PAGE = (By.XPATH, '//*[@id="browse"]/li/ul/li[4]/a')
    CHOOSE_LANGUAGE = (By.CSS_SELECTOR, '.form-control')
    BRT_ENG = (By.XPATH, "//*[@id='language_selector']/div/select/option[6]")
    EXECUTE_BTN = (By.XPATH, '//*[@id="language_selector"]/button')



class BooksPageLocatorss():
    SEARCH_FORM = (By.CSS_SELECTOR, '#id_q')
    SEARCH_BTN = (By.XPATH, '//*[@id="default"]/header/div[2]/div/div[2]/form/input')
    MOVE_BTN = (By.XPATH, "//*[@id='default']/div[2]/div/div/div/section/div/div/ul/li[3]/a")
    HACKING_BOOK = (By.XPATH, '//*[@id="default"]/div[2]/div/div/div/section/div/ol/li[12]/article/h3/a')
    ADD_BTN = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    PROOF_ADD = (By.XPATH, '//*[@id="messages"]/div[2]/div')


class OffersPageLocatorss():
    BOOK_3_FORM = (By.XPATH, '//*[@id="content_inner"]/ul[1]/li[3]/article/div[1]/a/img')
    BTN_BOOK3 = (By.XPATH, '//*[@id="content_inner"]/ul[1]/li[3]/article/h3/a')


class BasePageLocatorss():
    BOOKS_ICON = (By.XPATH, '//*[@id="browse"]/li/ul/li[4]/a')
    OFFERS_ICON = (By.XPATH, '//*[@id="browse"]/li/ul/li[6]/a')
    EXECUTE_ICON = (By.XPATH, '//*[@id="language_selector"]/button')



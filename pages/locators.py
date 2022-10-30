from selenium.webdriver.common.by import By


class MainPageLocators():
    LINK_TO_PRODUCT_PAGE = (By.XPATH, "//ul[@id='browse']//ul//a")
    LOGIN_BTN = (By.CSS_SELECTOR, '#login_link')
    LINK_TO_OFFERS_PAGE = (By.XPATH, "//*[@id='browse']/li/ul/li[6]/a")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BTN = (By.XPATH, "//form[@id='register_form']//button")

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')
    OFFERS_ICON = (By.XPATH, "//*[@id='browse']/li/ul/li[6]/a")

class OffersPageLocators():
    BOOK_3_FORM = (By.XPATH, '//*[@id="content_inner"]/ul[1]/li[3]/article/div[1]/a/img')
    BTN_BOOK3 = (By.XPATH, '//*[@id="content_inner"]/ul[1]/li[3]/article/h3/a')





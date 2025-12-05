from selenium.webdriver.common.by import By


class BaseLocators:

    MAIN_PAGE_URL = 'https://stellarburgers.education-services.ru/'
    LOGIN_URL = MAIN_PAGE_URL + 'login'
    ORDER_FEED_URL = MAIN_PAGE_URL + 'feed'
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]')

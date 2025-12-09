import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from locators.base_page_locators import BaseLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы сайта')
    def get_page(self, url):
        self.driver.get(url)

    @allure.step('Получаем url страницы')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Поиск элемента на странице')
    def find_element_on_page(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Поиск элементов на странице')
    def find_elements_on_page(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Клик на кнопку')
    def click_on_button(self, locator):
        element = self.find_element_on_page(locator)
        element.click()

    @allure.step('Получение текста элемента {locator}')
    def get_text(self, locator):
        self.wait_for_element_visible(locator)
        element = self.find_element_on_page(locator)
        return element.text

    @allure.step('Ввод данных в поле {locator}')
    def fill_field(self, locator, data):
        element = self.find_element_on_page(locator)
        element.clear()
        element.send_keys(data)

    @allure.step('Нажатие на кнопку "Конструктор"')
    def click_on_constructor_button(self):
        self.click_on_button(BaseLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Нажатие на кнопку "Лента Заказов"')
    def click_on_order_feed_button(self):
        self.click_on_button(BaseLocators.ORDER_FEED_BUTTON)

    @allure.step('Проверка отображения элемента {locator}')
    def is_element_displayed(self, locator):
        element = self.find_element_on_page(locator)
        return element.is_displayed()

    @allure.step('Проверка отображения элементов')
    def are_elements_displayed(self, list_of_locators):
        for locator in list_of_locators:
            if not self.is_element_displayed(locator):
                return False
        return True

    @allure.step('Ожидание исчезновения элемента {locator}')
    def wait_until_element_disappears(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    @allure.step('Ожидание появления элемента {locator} на странице')
    def wait_for_element_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    @allure.step('Перетягивание элемента {element}')
    def drag_and_drop_element(self, element, target):
        action = ActionChains(self.driver)
        element_locator = self.find_element_on_page(element)
        target_point = self.find_element_on_page(target)
        action.drag_and_drop(element_locator, target_point).perform()

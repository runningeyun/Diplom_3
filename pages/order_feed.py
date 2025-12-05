import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from locators.base_page_locators import BaseLocators


class OrderFeed(BasePage):

    @allure.step('Открытие страницы с лентой заказов')
    def get_order_feed_page(self):
        self.get_page(BaseLocators.ORDER_FEED_URL)
        self.wait_for_element_visible(OrderFeedLocators.ORDER_FEED_HEADER)

    @allure.step('Получение текущего количества выполненных заказов за {duration}')
    def get_number_of_orders_created(self, duration):
        if duration == 'total':
            return self.get_text(OrderFeedLocators.TOTAL_ORDERS_VALUE)
        else:
            return self.get_text(OrderFeedLocators.TODAY_ORDERS_VALUE)

    @allure.step('Проверка изменения количества выполненных заказов')
    def is_number_of_orders_increased(self, old_value, new_value):
        if new_value > old_value:
            return True
        else:
            return False

    @allure.step('Получение количества заказов в работе')
    def get_number_of_orders_in_progress(self):
        count_of_elements = len(self.find_elements_on_page(OrderFeedLocators.ORDERS_IN_PROCESS))
        return count_of_elements

    @allure.step('Проверка изменения количества заказов в работе')
    def is_new_order_add_to_progress(self, old_orders, new_orders):
        if old_orders < new_orders:
            return True
        else:
            return False

    @allure.step('Проверка, что переход на страницу с лентой заказов произошел')
    def is_current_url_order_feed(self):
        self.wait_for_element_visible(OrderFeedLocators.ORDER_FEED_HEADER)
        if self.get_url() == BaseLocators.ORDER_FEED_URL:
            return True

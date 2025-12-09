from selenium.webdriver.common.by import By


class OrderFeedLocators:

    ORDER_FEED_HEADER = (By.XPATH, '//h1[text()="Лента заказов"]')
    TOTAL_ORDERS_VALUE = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    TODAY_ORDERS_VALUE = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    ORDERS_IN_PROCESS = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]//li')

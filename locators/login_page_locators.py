from selenium.webdriver.common.by import By


class LoginLocators:

    EMAIL_FIELD_INPUT = (By.XPATH, '//input[@name="name"]')
    PASSWORD_FIELD_INPUT = (By.XPATH, '//input[@name="Пароль"]')
    ENTER_BUTTON = (By.XPATH, '//button[text()="Войти"]')

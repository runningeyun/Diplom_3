from selenium.webdriver.common.by import By


class MainPageLocators:

    INGREDIENTS_HEADER = (By.XPATH, '//h1[text()="Соберите бургер"]')
    FIRST_BUN = (By.CSS_SELECTOR, 'img[alt="Флюоресцентная булка R2-D3"]')
    INGREDIENT_DETAILS_HEADER = (By.XPATH, '//h2[text()="Детали ингредиента"]')

    INGREDIENT_DETAILS = [
        (By.XPATH, '//p[text()="Калории,ккал"]'),
        (By.XPATH, '//p[text()="Белки, г"]'),
        (By.XPATH, '//p[text()="Жиры, г"]'),
        (By.XPATH, '//p[text()="Углеводы, г"]')
        ]

    INGREDIENT_DETAILS_POPUP_CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        "section.Modal_modal_opened__3ISw4.Modal_modal__P3_V5 button.Modal_modal__close__TnseK"
        )

    FIRST_BUN_COUNTER = (
        By.XPATH,
        '//p[text()= "Флюоресцентная булка R2-D3"]/..//p[contains(@class, "counter_counter__num")]'
        )

    CONSTRUCTOR_AREA = (By.XPATH, '//section[contains(@class, "BurgerConstructor")]//ul')
    CREATE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

import allure

from pages.base_page import BasePage
from locators import (
    BUNS_TAB,
    SAUCES_TAB,
    FILLINGS_TAB,
    INGREDIENT_CARDS,
    INGREDIENT_COUNTER_NUMBER,
    MODAL_WINDOW,
    MODAL_CLOSE_BUTTON,
    BURGER_CONSTRUCTOR,
    ORDER_BUTTON,
    ORDER_NUMBER,
    ORDER_SUCCESS_MODAL,
    CONSTRUCTOR_TITLE,
    MODAL_OVERLAY,
    MODAL_LOADING_WINDOW
)


class ConstructorPage(BasePage):

    @allure.step("Перейти в раздел Булки")
    def click_buns(self):
        self.wait_invisibility(MODAL_OVERLAY)
        self.click(BUNS_TAB)

    @allure.step("Перейти в раздел Соусы")
    def click_sauces(self):
        self.wait_invisibility(MODAL_OVERLAY)
        self.click(SAUCES_TAB)

    @allure.step("Перейти в раздел Начинки")
    def click_fillings(self):
        self.wait_invisibility(MODAL_OVERLAY)
        self.click(FILLINGS_TAB)

    @allure.step("Получить список ингредиентов")
    def get_ingredients(self):
        return self.find_all_visible_elements(INGREDIENT_CARDS)

    @allure.step("Открыть детали ингредиента")
    def open_ingredient_details(self, index=0):
        
        ingredients = self.get_ingredients()
        ingredient = ingredients[index]

        self.click_element(ingredient)
        self.wait_visible(MODAL_WINDOW)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click(MODAL_CLOSE_BUTTON)
        self.wait_invisibility(MODAL_WINDOW)
        self.wait_invisibility(MODAL_OVERLAY)

    @allure.step("Проверить отображение модального окна")
    def is_modal_displayed(self):
        return self.is_element_displayed(MODAL_WINDOW)

    @allure.step("Получить счётчик ингредиента")
    def get_ingredient_counter(self, index=0):
        ingredients = self.get_ingredients()

        counters = self.find_child_elements(
            ingredients[index],
            INGREDIENT_COUNTER_NUMBER
        )

        if not counters:
            return 0

        return int(counters[0].text)

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient(self, index=0):
        self.html5_drag_and_drop(
            INGREDIENT_CARDS,
            BURGER_CONSTRUCTOR
        )

    @allure.step("Оформить заказ")
    def create_order(self):
        self.click(ORDER_BUTTON)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        return self.get_text(ORDER_NUMBER).strip()

    @allure.step("Дождаться появления окна успешного заказа")
    def wait_order_success(self):
        self.wait_visible(ORDER_SUCCESS_MODAL)
        self.wait_invisibility(MODAL_LOADING_WINDOW)

    @allure.step("Закрыть окно успешного оформления заказа")
    def close_order_success_modal(self):
        self.wait_clickable(MODAL_CLOSE_BUTTON)
        self.click(MODAL_CLOSE_BUTTON)
        self.wait_invisibility(MODAL_WINDOW)
        self.wait_invisibility(MODAL_OVERLAY)

    @allure.step("Проверить отображение кнопки оформления заказа")
    def is_order_button_displayed(self):
        return self.is_displayed(ORDER_BUTTON)

    @allure.step("Проверить, что открыт конструктор")
    def is_constructor_displayed(self):
        return self.is_element_displayed(CONSTRUCTOR_TITLE)


    @allure.step("Дождаться увеличения счётчика ингредиента")
    def wait_for_ingredient_counter(self, index, initial_counter):
        self.wait.until(
            lambda _: self.get_ingredient_counter(index) > initial_counter
        )
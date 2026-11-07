import allure

from pages.base_page import BasePage
from locators import (
    NAME_INPUT,
    REGISTER_EMAIL_INPUT,
    REGISTER_PASSWORD_INPUT,
    REGISTER_BUTTON,
    LOGIN_FROM_REGISTER_BUTTON,
    PASSWORD_ERROR
)


class RegisterPage(BasePage):

    @allure.step("Зарегистрировать нового пользователя")
    def register(self, name, email, password):
        self.send_keys(NAME_INPUT, name)
        self.send_keys(REGISTER_EMAIL_INPUT, email)
        self.send_keys(REGISTER_PASSWORD_INPUT, password)
        self.click(REGISTER_BUTTON)

    @allure.step("Проверить ошибку некорректного пароля")
    def is_password_error_displayed(self):
        return self.is_displayed(PASSWORD_ERROR)

    @allure.step("Перейти на страницу входа")
    def click_login(self):
        self.click(LOGIN_FROM_REGISTER_BUTTON)

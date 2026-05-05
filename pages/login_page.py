from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        """Ввод имени пользователя"""
        self.input_text(LoginLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Ввод пароля"""
        self.input_text(LoginLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        """Нажатие на кнопку логина"""
        self.click(LoginLocators.LOGIN_BUTTON)

    def click_registration_button(self):
        """Нажатие на кнопку регистрации"""
        self.click(LoginLocators.REGISTRATION_BUTTON)

    def login(self, username, password):
        """Комбинированный метод для логина"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self):
        """Получение сообщения об ошибке"""
        return self.get_text(LoginLocators.ERROR_MESSAGE)

    def get_error_input(self, locator):
        """Получение сообщения об ошибке"""
        return self.find_element(locator)

    def is_login_successful(self):
        """Проверка успешного логина по URL профиля"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/profile")
            )
            return True
        except:
            return False

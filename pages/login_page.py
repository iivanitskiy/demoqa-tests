from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.input_text(LoginLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.input_text(LoginLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(LoginLocators.LOGIN_BUTTON)

    def login(self, username, password):
        """Комбинированный метод для логина"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self):
        return self.get_text(LoginLocators.ERROR_MESSAGE)

    def get_error_input(self, locator):
        return self.find_element(locator)

    def is_login_successful(self):
        return self.is_element_visible(LoginLocators.SUCCESS_ELEMENT)

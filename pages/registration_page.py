from pages.base_page import BasePage
from locators.registration_locators import RegistrationLocators


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_firstname(self, firstname):
        """Ввод имени"""
        self.input_text(RegistrationLocators.FIRSTNAME_INPUT, firstname)
        
    def enter_lastname(self, lastname):
        """Ввод фамилии"""
        self.input_text(RegistrationLocators.LASTNAME_INPUT, lastname)

    def enter_username(self, username):
        """Ввод имени пользователя"""
        self.input_text(RegistrationLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Ввод пароля"""
        self.input_text(RegistrationLocators.PASSWORD_INPUT, password)

    def click_registration_button(self):
        """Нажатие на кнопку регистрации"""
        self.click(RegistrationLocators.REGISTRATION_BUTTON)
        
    def click_login_button(self):
        """Нажатие на кнопку логина"""
        self.click(RegistrationLocators.LOGIN_BUTTON)

    def registration(self, firstname, lastname, username, password):
        """Комбинированный метод для регистрации"""
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_username(username)
        self.enter_password(password)
        self.click_registration_button()

    def get_error_message(self):
        """Получение сообщения об ошибке"""
        return self.get_text(RegistrationLocators.ERROR_MESSAGE)

    def get_error_input(self, locator):
        """Получение сообщения об ошибке"""
        return self.find_element(locator)

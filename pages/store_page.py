from pages.base_page import BasePage
from locators.store_locators import StoreLocators


class StorePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_search_text(self, text):
        """Ввод текста в поле поиска"""
        self.input_text(StoreLocators.SEARCH_INPUT, text)

    def search_button(self):
        """Нажатие на кнопку поиска"""
        self.click(StoreLocators.SEARCH_BUTTON)

    def logout_button(self):
        """Нажатие на кнопку логаута"""
        self.click(StoreLocators.LOGOUT_BUTTON)

    def username_visible(self):
        """Проверка видимости имени пользователя"""
        return self.is_element_visible(StoreLocators.USER_NAME)

    def get_username(self):
        """Получение имени пользователя"""
        return self.get_text(StoreLocators.USER_NAME)

    def get_book(self, locator):
        """Получение книги"""
        return self.find_element(locator)

    def book_link_click(self, locator):
        """Нажатие на ссылку книги"""
        self.click(locator)

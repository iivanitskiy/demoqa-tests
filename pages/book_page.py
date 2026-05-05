from pages.base_page import BasePage
from locators.book_locators import BookLocators


class BookPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def logout_button(self):
        """Нажатие на кнопку логаута"""
        self.click(BookLocators.LOGOUT_BUTTON)

    def username_visible(self):
        """Проверка видимости имени пользователя"""
        return self.is_element_visible(BookLocators.USER_NAME)

    def get_username(self):
        """Получение имени пользователя"""
        return self.get_text(BookLocators.USER_NAME)

    def get_book_title(self, locator):
        """Получение названия книги"""
        return self.find_elements(locator)

    def back_button(self):
        """Нажатие на кнопку возврата в магазин"""
        self.click(BookLocators.BACK_TO_STORE_BUTTON)

    def add_button(self):
        """Нажатие на кнопку добавления в коллекцию"""
        self.click(BookLocators.ADD_TO_COLLECTION_BUTTON)

    def loader_visible(self):
        """Проверка видимости лоадера"""
        return self.is_element_visible(BookLocators.LOADER)

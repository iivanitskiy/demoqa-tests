from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_search_text(self, text):
        """Ввод текста в поле поиска"""
        self.input_text(ProfileLocators.SEARCH_INPUT, text)

    def search_button(self):
        """Нажатие на кнопку поиска"""
        self.click(ProfileLocators.SEARCH_BUTTON)

    def delete_book_button(self):
        """Нажатие на кнопку удаления книги"""
        self.click(ProfileLocators.DELETE_BOOK_BUTTON)

    def delete_all_books_button(self):
        """Нажатие на кнопку удаления всех книг"""
        self.click(ProfileLocators.DELETE_ALL_BOOKS_BUTTON)

    def return_to_store_button(self):
        """Нажатие на кнопку возврата в магазин"""
        self.click(ProfileLocators.STORE_BUTTON)

    def logout_button(self):
        """Нажатие на кнопку логаута"""
        self.click(ProfileLocators.LOGOUT_BUTTON)

    def delete_account_button(self):
        """Нажатие на кнопку удаления аккаунта"""
        self.click(ProfileLocators.DELETE_ACCOUNT_BUTTON)

    def username_visible(self):
        """Проверка видимости имени пользователя"""
        return self.is_element_visible(ProfileLocators.USER_NAME)
    
    def get_username(self):
        """Получение имени пользователя"""
        return self.get_text(ProfileLocators.USER_NAME)
    
    def modal_ok_button(self):
        """Нажатие на кнопку ОК в модальном окне"""
        self.click(ProfileLocators.DELETE_MODAL_OK_BUTTON)

    def modal_cancel_button(self):
        """Нажатие на кнопку Отмена в модальном окне"""
        self.click(ProfileLocators.DELETE_MODAL_CANCEL_BUTTON)

    def get_books_rows(self, locator):
        """Получение списка книг"""
        return self.find_elements_safe(locator)

    def get_book(self, locator):
        """Получение книги"""
        return self.find_element(locator)
    
    def book_link_click(self, locator):
        """Нажатие на ссылку книги"""
        self.click(locator)
    

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.book_locators import BookLocators
from pages.book_page import BookPage


class TestBook:

    @allure.step("Проверка отображения имени пользователя после логина")
    def test_username_displayed(self, base_url, logged_in_driver):
        logged_in_driver.get(f"{base_url}/books?search=9781449325862")

        book_page = BookPage(logged_in_driver)

        assert book_page.username_visible(), "Имя пользователя не отображается"

        username = book_page.get_username()
        assert (
            username == "Ivanovaqa"
        ), f"Ожидалось имя 'Ivanovaqa', получено '{username}'"

    def is_loader_invisible(self, logged_in_driver, timeout=3):
        """Ожидаем исчезновения лоадера"""
        try:
            wait = WebDriverWait(logged_in_driver, timeout)
            wait.until(EC.invisibility_of_element_located(BookLocators.LOADER))
            return True
        except TimeoutException:
            return True

    @allure.step("Проверка отображения названия книги")
    def test_book_title_displayed(self, base_url, logged_in_driver):
        logged_in_driver.get(f"{base_url}/books?search=9781449325862")

        self.is_loader_invisible(logged_in_driver)

        wait = WebDriverWait(logged_in_driver, 10)
        books = wait.until(EC.presence_of_all_elements_located(BookLocators.BOOK_TITLE))

        assert len(books) > 0, "Книги не найдены"
        book_title = books[2].text
        assert (
            book_title == "Git Pocket Guide"
        ), f"Ожидалось 'Git Pocket Guide', получено '{book_title}'"

    @allure.step("Выход из профиля")
    def test_logout(self, base_url, logged_in_driver):
        logged_in_driver.get(f"{base_url}/books?search=9781449325862")
        book_page = BookPage(logged_in_driver)

        book_page.logout_button()

        assert (
            "/login" in logged_in_driver.current_url
        ), f"Ожидался URL с /login, получен {logged_in_driver.current_url}"

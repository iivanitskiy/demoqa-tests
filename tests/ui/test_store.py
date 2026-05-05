from selenium.webdriver.common.by import By
import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.store_locators import StoreLocators
from pages.store_page import StorePage


class TestStore:

    @allure.step("Проверка отображения имени пользователя после логина")
    def test_username_displayed(self, base_url, logged_in_driver):
        logged_in_driver.get(f"{base_url}/books")

        store_page = StorePage(logged_in_driver)

        assert store_page.username_visible(), "Имя пользователя не отображается"

        username = store_page.get_username()
        assert (
            username == "Ivanovaqa"
        ), f"Ожидалось имя 'Ivanovaqa', получено '{username}'"

    @allure.step("Переход на страницу книги")
    def test_go_to_book(self, base_url, logged_in_driver):
        logged_in_driver.get(f"{base_url}/books")
        store_page = StorePage(logged_in_driver)

        store_page.book_link_click(StoreLocators.BOOK)
        assert (
            "https://demoqa.com/books?search=9781449325862"
            in logged_in_driver.current_url
        ), f"Ожидался URL с /books/Git, получен {logged_in_driver.current_url}"

    @allure.step("Поиск книги по названию")
    @pytest.mark.parametrize(
        "search_text",
        [
            ("Git"),
        ],
    )
    def test_search_book(self, base_url, logged_in_driver, search_text):
        logged_in_driver.get(f"{base_url}/books")
        store_page = StorePage(logged_in_driver)

        store_page.enter_search_text(search_text)
        store_page.search_button()
        assert store_page.get_book(StoreLocators.BOOK)

    @allure.step("Выход из профиля")
    def test_logout(self, base_url, logged_in_driver):
        logged_in_driver.get(f"{base_url}/books")
        store_page = StorePage(logged_in_driver)

        store_page.logout_button()

        assert (
            "/login" in logged_in_driver.current_url
        ), f"Ожидался URL с /login, получен {logged_in_driver.current_url}"

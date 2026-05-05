from selenium.webdriver.common.by import By

import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.profile_locators import ProfileLocators
from pages.profile_page import ProfilePage

class TestProfile:

    @allure.step("Проверка отображения имени пользователя после логина")
    def test_username_displayed(self, logged_in_driver):
        """Тест проверяет, что после успешного логина отображается имя пользователя"""
        profile_page = ProfilePage(logged_in_driver)
        
        assert profile_page.username_visible(), "Имя пользователя не отображается"
        
        username = profile_page.get_username()
        assert username == "Ivanovaqa", f"Ожидалось имя 'Ivanovaqa', получено '{username}'"

    @allure.step("Переход на страницу книги")
    def test_go_to_book(self, logged_in_driver):
        profile_page = ProfilePage(logged_in_driver)
        
        profile_page.book_link_click(ProfileLocators.BOOK)
        assert "https://demoqa.com/books?search=9781449325862" in logged_in_driver.current_url, \
            f"Ожидался URL с /books/Git, получен {logged_in_driver.current_url}"

    @allure.step("Поиск книги по названию")
    @pytest.mark.parametrize("search_text", [
        ("Git"),
    ])
    def test_search_book(self, logged_in_driver, search_text):
        profile_page = ProfilePage(logged_in_driver)
        
        profile_page.enter_search_text(search_text)
        profile_page.search_button()
        assert profile_page.get_book(ProfileLocators.BOOK)

    @allure.step("Выход из профиля")
    def test_logout(self, logged_in_driver):
        profile_page = ProfilePage(logged_in_driver)
        
        profile_page.logout_button()
        
        assert "/login" in logged_in_driver.current_url, \
            f"Ожидался URL с /login, получен {logged_in_driver.current_url}"

    @allure.step("Переход в магазин книг")
    def test_go_to_store(self, logged_in_driver):
        profile_page = ProfilePage(logged_in_driver)
        
        profile_page.return_to_store_button()
        
        assert "/books" in logged_in_driver.current_url, \
            f"Ожидался URL с /books, получен {logged_in_driver.current_url}"

    @allure.step("Удаление книги")
    def test_delete_book(self, logged_in_driver):
        profile_page = ProfilePage(logged_in_driver)
        
        book_rows = profile_page.get_books_rows(ProfileLocators.BOOKS_ROWS)
        count = len(book_rows)

        profile_page.delete_book_button()
        profile_page.modal_ok_button()

        wait = WebDriverWait(logged_in_driver, 5)
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        expected_text = "Book deleted."
        assert alert_text == expected_text
        alert.accept()
        assert count - 1 == len(profile_page.get_books_rows(ProfileLocators.BOOKS_ROWS)) , \
            f"Ожидалось удаление книги, получено {len(profile_page.get_books_rows(ProfileLocators.BOOKS_ROWS))}"

    @allure.step("Удаление всех книг")
    def test_delete_all_books(self, logged_in_driver):
        profile_page = ProfilePage(logged_in_driver)
        
        profile_page.delete_all_books_button()
        profile_page.modal_ok_button()

        logged_in_driver.get("https://demoqa.com/profile")
        logged_in_driver.refresh()
        
        book_rows = profile_page.get_books_rows(ProfileLocators.BOOKS_ROWS)      
        assert book_rows == [], f"Ожидалось удаление всех книг, получено {len(book_rows)} книг"

    @allure.step("Удаление учетной записи")
    def test_delete_account(self, logged_in_driver):
        profile_page = ProfilePage(logged_in_driver)
        
        profile_page.delete_account_button()
        profile_page.modal_ok_button()

        assert True

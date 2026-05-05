import allure
import pytest
from api.books_api import BooksApi


@allure.feature("BookStore API")
@allure.story("Поиск книг")
class TestBooksSearchApi:
    @allure.title("Получение всех книг возвращает список")
    def test_get_all_books(self, base_url):
        books_api = BooksApi(base_url)

        all_books = books_api.get_all_books()

        assert isinstance(all_books, list)
        assert len(all_books) > 0

        first_book = all_books[0]
        assert "isbn" in first_book
        assert "title" in first_book
        assert "author" in first_book

    @allure.title("Поиск конкретной книги по ISBN")
    @pytest.mark.parametrize(
        "isbn, expected_title",
        [
            ("9781449325862", "Git Pocket Guide"),
            ("9781491950296", "Programming JavaScript Applications"),
        ],
    )
    def test_find_book_by_isbn(self, base_url, isbn, expected_title):
        books_api = BooksApi(base_url)

        book = books_api.get_book_by_isbn(isbn)

        assert book["isbn"] == isbn
        assert book["title"] == expected_title

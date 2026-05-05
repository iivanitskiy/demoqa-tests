import allure
from api.base_api import BaseApi

class BooksApi(BaseApi):
    """
    API-объект для эндпоинтов BookStore:
    GET /BookStore/v1/Books, POST /BookStore/v1/Books и др.
    """
    def __init__(self, base_url: str):
        super().__init__(base_url)
        self.books_endpoint = "/BookStore/v1/Books"
        self.book_endpoint = "/BookStore/v1/Book"

    @allure.step("Получить список всех книг (GET /BookStore/v1/Books)")
    def get_all_books(self):
        """Возвращает информацию о всех доступных книгах"""
        response = self.get(self.books_endpoint)
        return response.json().get('books', [])

    @allure.step("Найти книгу по ISBN: {isbn}")
    def get_book_by_isbn(self, isbn: str):
        """GET /BookStore/v1/Book?ISBN={isbn} – поиск книги по ISBN"""
        params = {"ISBN": isbn}
        response = self.get(self.book_endpoint, params=params)
        return response.json()

    @allure.step("Добавить книгу в коллекцию пользователя (POST /BookStore/v1/Books)")
    def add_book_to_collection(self, user_uuid: str, isbn: str, token: str):
        """Требует токен"""
        self.set_auth_token(token)
        payload = {
            "userId": user_uuid,
            "collectionOfIsbns": [{"isbn": isbn}]
        }
        response = self.post(self.books_endpoint, json=payload)
        return response.json()

    @allure.step("Удалить книгу из коллекции (DELETE /BookStore/v1/Book)")
    def delete_book_from_collection(self, user_uuid: str, isbn: str, token: str):
        """Требует токен"""
        self.set_auth_token(token)
        payload = {
            "isbn": isbn,
            "userId": user_uuid
        }
        response = self.delete(self.book_endpoint, json=payload)
        return response.status_code
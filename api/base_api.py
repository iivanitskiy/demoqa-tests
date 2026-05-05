import requests
import allure


class BaseApi:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(
            {"Content-Type": "application/json", "Accept": "application/json"}
        )

    def _request(self, method, endpoint, **kwargs):
        """Универсальный метод отправки запроса с логированием"""
        url = f"{self.base_url}{endpoint}"
        with allure.step(f"API {method.upper()} {endpoint}"):
            response = self.session.request(method, url, **kwargs)
            allure.attach(
                response.text,
                name="Response",
                attachment_type=allure.attachment_type.JSON,
            )
            return response

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)

    def set_auth_token(self, token: str):
        """Устанавливает токен авторизации для последующих запросов"""
        self.session.headers.update({"Authorization": f"Bearer {token}"})

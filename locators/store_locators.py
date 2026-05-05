from selenium.webdriver.common.by import By

class StoreLocators:
    LOGOUT_BUTTON = (By.ID, "submit")
    SEARCH_INPUT = (By.ID, "searchBox")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-outline-secondary")
    USER_NAME = (By.ID, "userName-value")
    BOOK = (By.ID, "see-book-Git Pocket Guide")

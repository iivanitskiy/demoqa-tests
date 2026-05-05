from selenium.webdriver.common.by import By

class ProfileLocators:
    LOGOUT_BUTTON = (By.ID, "submit")
    SEARCH_INPUT = (By.ID, "searchBox")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-outline-secondary")
    USER_NAME = (By.ID, "userName-value")
    STORE_BUTTON = (By.ID, "gotoStore") 
    DELETE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Delete Account']")
    DELETE_ALL_BOOKS_BUTTON = (By.XPATH, "//button[text()='Delete All Books']")
    DELETE_BOOK_BUTTON = (By.XPATH, "//span[@title='Delete']")
    DELETE_MODAL_OK_BUTTON = (By.ID, "closeSmallModal-ok")
    DELETE_MODAL_CANCEL_BUTTON = (By.ID, "closeSmallModal-cancel")
    BOOKS_ROWS = (By.XPATH, "//tbody/tr")
    BOOK = (By.ID, "see-book-Git Pocket Guide")

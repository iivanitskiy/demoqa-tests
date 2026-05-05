from selenium.webdriver.common.by import By


class BookLocators:
    LOGOUT_BUTTON = (By.ID, "submit")
    USER_NAME = (By.ID, "userName-value")
    BOOK_TITLE = (By.ID, "userName-value")
    BACK_TO_STORE_BUTTON = (By.ID, "addNewRecordButton"[0])
    ADD_TO_COLLECTION_BUTTON = (By.ID, "addNewRecordButton"[1])
    LOADER = (By.ID, "loader")

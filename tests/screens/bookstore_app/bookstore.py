from selenium.webdriver.common.by import By


class Bookstore:

    def __init__(self, driver):
        self.driver = driver

    SEARCHBAR_INPUT = (By.ID, 'searchBox')
    LOGOUT_BTN = (By.ID, 'submit')
    BACK_TO_BOOK_BTN = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div[1]/button')
    # Added xPath
    # instead of id because 'BACK_TO_BOOK_BTN' and 'ADD_TO_COLLECTION_BTN' has the same id
    ADD_TO_COLLECTION_BTN = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div[2]/button')
    BOOK_ID = (By.ID, 'see-book-Learning JavaScript Design Patterns')
    GO_TO_BOOK_BTN = (By.ID, 'gotoStore')
    DELETE_ACCOUNT_BTN = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/button')
    DELETE_ALL_BOOKS_BTN = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[3]/button')
    OK_MODAL_BTN = (By.ID, 'closeSmallModal-ok')
    CANCEL_MODAL_BTN = (By.ID, 'closeSmallModal-cancel')
    DELETE_BOOK_BTN = (By.XPATH, '//*[@id="delete-record-undefined"]/svg/path')
    PROFILE_SIDE_BTN = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[6]/div/ul/li[3]')
    BOOKSTORE_SIDE_BTN = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[6]/div/ul/li[2]')

    def get_searchbar_input(self):
        return self.driver.find_element(*self.SEARCHBAR_INPUT)

    def get_logout_btn(self):
        return self.driver.find_element(*self.LOGOUT_BTN)

    def get_back_to_book_btn(self):
        return self.driver.find_element(*self.BACK_TO_BOOK_BTN)

    def get_add_to_collection_btn(self):
        return self.driver.find_element(*self.ADD_TO_COLLECTION_BTN)

    def get_book_id(self):
        return self.driver.find_element(*self.BOOK_ID)

    def get_alert(self):
        return self.driver.switch_to.alert

    def click_logout_btn(self):
        self.get_logout_btn().click()

    def click_back_to_book_btn(self):
        self.get_back_to_book_btn().click()

    def click_add_to_collection_btn(self):
        self.get_add_to_collection_btn().click()

    def get_go_to_book_btn(self):
        return self.driver.find_element(*self.GO_TO_BOOK_BTN)

    def get_delete_account_btn(self):
        return self.driver.find_element(*self.DELETE_ACCOUNT_BTN)

    def get_delete_all_books_btn(self):
        return self.driver.find_element(*self.DELETE_ALL_BOOKS_BTN)

    def get_ok_modal_btn(self):
        return self.driver.find_element(*self.OK_MODAL_BTN)

    def get_cancel_modal_btn(self):
        return self.driver.find_element(*self.CANCEL_MODAL_BTN)

    def get_delete_book_btn(self):
        return self.driver.find_element(*self.DELETE_BOOK_BTN)

    def get_bookstore_side_btn(self):
        return self.driver.find_element(*self.BOOKSTORE_SIDE_BTN)

    def click_go_to_book_btn(self):
        self.get_go_to_book_btn().click()

    def click_delete_account_btn(self):
        self.get_delete_account_btn().click()

    def click_delete_all_books_btn(self):
        self.get_delete_all_books_btn().click()

    def click_ok_modal_btn(self):
        self.get_ok_modal_btn().click()

    def click_cancel_modal_btn(self):
        self.get_cancel_modal_btn().click()

    def click_delete_book_btn(self):
        self.get_delete_book_btn().click()

    def scroll_to_bookstore_btn(self, element):
        # Utilizar JavaScript para hacer scroll hasta el elemento
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_bookstore_side_btn(self):
        btn = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[6]/div/ul/li[2]')
        self.scroll_to_bookstore_btn(btn)
        btn.click()

    def scroll_to_profile_btn(self, element):
        # Utilizar JavaScript para hacer scroll hasta el elemento
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_profile_side_btn(self):
        btn = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[6]/div/ul/li[3]')
        self.scroll_to_profile_btn(btn)
        btn.click()

from selenium.webdriver.common.by import By
from .helper import wait_visible, wait_invisible, file_path, wait_presence


class Document:
    """Class that defines the `Document` module objects and methods."""

    def __init__(self, driver):
        """ Web Elements."""
        self._driver = driver
        self._loading_img = (By.CSS_SELECTOR, 'img[src*="loading"]')
        self._business_menu = (By.CSS_SELECTOR,
                               'li.menu-item-has-children a[href="/business"]')
        self._docs_menu_option = (By.CSS_SELECTOR, 'li > a[href*="documents"]')
        self._file_input = (By.XPATH,
                            '//span[contains(text(), "Business License")]'
                            '//following-sibling::span[1]/input[@type="file"]')
        self._uploading_msg = (By.XPATH, '//div[contains(text(), "Uploading...")]')
        self._file_container = (By.XPATH,
                                '//span[contains(text(), "Business License")]'
                                '//following-sibling::span[1]//a')

    def go_to_documents_section(self):
        wait_invisible(self._driver, self._loading_img)
        wait_visible(self._driver, self._business_menu)
        business_menu = self._driver.find_element(*self._business_menu)
        business_menu.click()
        wait_visible(self._driver, self._docs_menu_option)
        docs_menu_option = self._driver.find_element(*self._docs_menu_option)
        docs_menu_option.click()

    def upload_file(self, file_name):
        wait_presence(self._driver, self._file_input)
        upload_file_btn = self._driver.find_element(*self._file_input)
        upload_file_btn.send_keys(file_path(file_name).replace('page_objects/../', ''))
        wait_visible(self._driver, self._uploading_msg)
        wait_invisible(self._driver, self._uploading_msg)

    def verify_uploaded_file(self, file_name):
        file_container = self._driver.find_element(*self._file_container)
        assert file_container.text == file_name

    def download_file(self):
        file_container = self._driver.find_element(*self._file_container)
        file_container.click()


# -*- coding: utf-8 -*-

from component import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import WebDriverException


class Sidebar(Component):
    BASE = '//div[@data-qa-id="full"] '
    BASE_WITHOUT_QA_ID = '//div[contains(@class,"sidebar__full")]'
    CONTEXTMENU = '//div[@data-qa-id="contextmenu"] '

    INBOX_BUTTON = BASE + '//a[@data-qa-id="0"]'
    NEW_DIR =  BASE + '//div[@class="new-folder-btn__button-wrapper"]'
    FOLDER_NAME_TEXT = BASE + '//a[@title="{}"]//div[@class="nav__folder-name__txt"]'
    REMOVE_FROM_TRASH = BASE + '//div[@class="nav__folder-clear"]'
    SUBMIT_REMOVE_FROM_TRASH = '//div[@class="layer__submit-button"]'
    FOLDER_ELEM = './/a[@title="{}"]'
    DELETE_BUT = '//div[@data-qa-id="delete"]'
    FOLDER_DIV = './/a[@title="{}"]'
    SUBMIT_DELETE = '//div[@class="layer__submit-button"]'
    LINK_TRASH = '//a[@title="Корзина"]'
    LOCK_FOLDER = CONTEXTMENU + '//span[contains(text(), "Заблокировать")]'
    UNLOCK_FOLDER = CONTEXTMENU + '//span[contains(text(), "Разблокировать")]'
    

    def create_new_dir(self):
        create_dir_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NEW_DIR)
        )
        create_dir_button.click()
    
    def click_to_inbox(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INBOX_BUTTON)
        ).click()

    def waitForVisible(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.BASE_WITHOUT_QA_ID))

    def get_text_by_folder_name(self, f_name):
        F_NAME_TEXT = self.FOLDER_NAME_TEXT.format(f_name)
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(F_NAME_TEXT).text
        )

    def is_trash_empty(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.BASE))
        clear_button = self.driver.find_elements_by_xpath(self.REMOVE_FROM_TRASH)
        if len(clear_button) == 0:
            return True
        else:
            return False

    def clear_trash(self):
        if self.is_trash_empty():
            return
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.REMOVE_FROM_TRASH)).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT_REMOVE_FROM_TRASH)).click()

    def right_click_by_folder(self, folder_name):
        FOLDER_EL = self.FOLDER_ELEM.format(folder_name)
        folder = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(FOLDER_EL)
        )
        actionChains = ActionChains(self.driver)
        actionChains.context_click(folder).perform()
    
    def click_by_folder(self, folder_name):
        FOLDER_EL = self.FOLDER_ELEM.format(folder_name)
        folder = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(FOLDER_EL)
        )
        folder.click()
    
    def click_delete(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DELETE_BUT)
        )
        button.click()

    def try_click_delete (self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DELETE_BUT)
        )
        try:
            button.click()
            return True
        except WebDriverException:
            return False
    
    def submit_delete(self):
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT_DELETE)
        )
        submit.click()

    def is_folder_deleted(self, f_name):
        F_DIV = self.FOLDER_DIV.format(f_name)
        self.driver.refresh()
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.BASE_WITHOUT_QA_ID))    
        folders = self.driver.find_elements_by_xpath(F_DIV)
        if len(folders) == 0:
            return True
        else:
            return False

    def go_to_trash(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LINK_TRASH)).click()

    def click_block_folder(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LOCK_FOLDER)
        )
        button.click()
    
    def click_unlock_folder(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.UNLOCK_FOLDER)
        )
        button.click()
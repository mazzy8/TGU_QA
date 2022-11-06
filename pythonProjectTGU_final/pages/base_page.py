from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import MainPageLocators
from .locators import PersonalAccountLocators
from .locators import ChangePasswordLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os


current_dir = os.path.abspath(os.path.dirname(__file__))


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def authorization_user(self):
        self.browser = self.open()
        self.browser.find_element(*MainPageLocators.LOGIN_MAIL_FIELD).send_keys('***********')
        self.browser.find_element(*MainPageLocators.LOGIN_PASSWORD_FIELD).send_keys('11111111')
        self.browser.find_element(*MainPageLocators.BUTTON_ENTER).click()
        return self.browser

    def change_password(self):
        WebDriverWait(self.browser, 7).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".menu-header")))
        element = self.browser.find_element(By.CSS_SELECTOR, ".logo_icon")
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()
        self.browser.find_element(*ChangePasswordLocators.LOCATOR_USER_AVATAR).click()
        WebDriverWait(self.browser, 7).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "Безопасность и вход")))
        self.browser.find_element(*ChangePasswordLocators.LOCATOR_SECURITY_TAB).click()
        self.browser.find_element(*ChangePasswordLocators.LOCATOR_CHANGE_PASSWORD_BUTTON).click()
        self.browser.find_element(*ChangePasswordLocators.FIELD_OLD_CHANGE_PASSWORD_FORM).send_keys('11111111')
        self.browser.find_element(*ChangePasswordLocators.FIELD_NEW_CHANGE_PASSWORD_FORM).send_keys('11111111')
        self.browser.find_element(*ChangePasswordLocators.FIELD_REPEAT_CHANGE_PASSWORD_FORM).send_keys('11111111')
        WebDriverWait(self.browser, 7).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "form >.btn.fill")))
        self.browser.find_element(*ChangePasswordLocators.CONFIRM_BUTTON_CHANGE_PASSWORD_FORM).click()
        return self.browser

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def load_passport_form(self):
        self.browser.find_element(*PersonalAccountLocators.LOCATOR_PASSPORT_FORM).click()
        self.browser.find_element(*PersonalAccountLocators.LAST_NAME_PASSPORT_FORM).send_keys('Бутузов')
        self.browser.find_element(*PersonalAccountLocators.FIRST_NAME_PASSPORT_FORM).send_keys('Максим')
        self.browser.find_element(*PersonalAccountLocators.PATRONYMIC_PASSPORT_FORM).send_keys('Сергеевич')
        self.browser.find_element(*PersonalAccountLocators.BIRTHDAY_PASSPORT_FORM).send_keys('01.03.1989')
        self.browser.find_element(*PersonalAccountLocators.SERIES_PASSPORT_FORM).click()
        self.browser.find_element(*PersonalAccountLocators.SERIES_PASSPORT_FORM).clear()
        self.browser.find_element(*PersonalAccountLocators.SERIES_PASSPORT_FORM).send_keys('1212')
        self.browser.find_element(*PersonalAccountLocators.NUMBER_PASSPORT_FORM).click()
        self.browser.find_element(*PersonalAccountLocators.NUMBER_PASSPORT_FORM).clear()
        self.browser.find_element(*PersonalAccountLocators.NUMBER_PASSPORT_FORM).send_keys('123123')
        self.browser.find_element(*PersonalAccountLocators.ISSUE_DATE_PASSPORT_FORM).send_keys('01.03.1999')
        self.browser.find_element(*PersonalAccountLocators.DIVISION_CODE_PASSPORT_FORM).click()
        self.browser.find_element(*PersonalAccountLocators.DIVISION_CODE_PASSPORT_FORM).clear()
        self.browser.find_element(*PersonalAccountLocators.DIVISION_CODE_PASSPORT_FORM).send_keys('123123')
        self.browser.find_element(*PersonalAccountLocators.SNILS_PASSPORT_FORM).click()
        self.browser.find_element(*PersonalAccountLocators.SNILS_PASSPORT_FORM).clear()
        self.browser.find_element(*PersonalAccountLocators.SNILS_PASSPORT_FORM).send_keys('12312312312')
        self.browser.find_element(*PersonalAccountLocators.ORGANIZATION_PASSPORT_FORM).send_keys('Организация')
        self.browser.find_element(*PersonalAccountLocators.ADDRESS_PASSPORT_FORM) \
            .send_keys('Оренбургская обл, г Орск, пр-кт Ленина, д 96, кв 28')
        self.browser.find_element(By.CSS_SELECTOR, ".vue-dadata__suggestions-item").click()
        self.browser.find_element(*PersonalAccountLocators.PHONE_NUMBER_PASSPORT_FORM).click()
        self.browser.find_element(*PersonalAccountLocators.PHONE_NUMBER_PASSPORT_FORM).clear()
        self.browser.find_element(*PersonalAccountLocators.PHONE_NUMBER_PASSPORT_FORM).send_keys('1231231212')
        # browser.find_element(*MainPageSelector.CHECK_BOX_PASSPORT_FORM).click()
        file_path = os.path.join(current_dir, 'passport.jpeg')
        self.browser.find_element(*PersonalAccountLocators.ATTACH_BUTTON_PASSPORT_FORM).send_keys(file_path)
        self.browser.execute_script("window.scrollTo(0, 1080)")
        WebDriverWait(self.browser, 5).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[class='buttons'] :nth-of-type(2)")))
        self.browser.find_element(*PersonalAccountLocators.SEND_BUTTON_PASSPORT_FORM).click()
        return self.browser

    def load_document_in_form(self, button_form, attach_button, send_button):
        self.browser.find_element(*button_form).click()
        file_path = os.path.join(current_dir, 'passport.jpeg')
        self.browser.find_element(*attach_button).send_keys(file_path)
        locator_type = send_button[0]
        iam_locator = send_button[1]
        WebDriverWait(self.browser, 5).until(
            expected_conditions.element_to_be_clickable((locator_type, iam_locator)))
        self.browser.find_element(*send_button).click()
        return self.browser

    def logout_user(self):
        WebDriverWait(self.browser, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".menu-header")))
        element = self.browser.find_element(By.CSS_SELECTOR, ".logo_icon")
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()
        self.browser.find_element(*PersonalAccountLocators.SELECTOR_LOGOUT).click()
        return self.browser

    def open(self):
        self.browser.get(self.url)
        self.browser.delete_all_cookies()
        self.browser.set_window_size(1920, 1080)
        return self.browser

    def return_text_from_element_on_page(self, how, what):
        try:
            text = self.browser.find_element(how, what).text
        except NoSuchElementException:
            return "Not find element"
        return text

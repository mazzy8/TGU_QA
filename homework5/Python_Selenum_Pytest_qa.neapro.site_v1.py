from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import os
import time


class LoginPageSelector:
    LOGIN_MAIL_FIELD = (By.CSS_SELECTOR, ".fieldset:nth-child(1) input")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, ".fieldset:nth-child(2) input")
    BUTTON_ENTER = (By.CSS_SELECTOR, "button.btn.fill")
    LINK_FORGOT_PASSWORD = (By.CSS_SELECTOR, "[href='/recovery']")


class MainPageSelector:
    LOCATOR_PASSPORT_FORM = (By.CSS_SELECTOR, "[class='body documents-tiles'] :nth-of-type(1)")
    LAST_NAME_PASSPORT_FORM = (By.XPATH, '//*[@id="surname"]')
    FIRST_NAME_PASSPORT_FORM = (By.XPATH, '//*[@id="name"]')
    PATRONYMIC_PASSPORT_FORM = (By.XPATH, '//*[@id="patronymic"]')
    BIRTHDAY_PASSPORT_FORM = (By.XPATH, '//*[@id="birthday"]/div/input')
    SERIES_PASSPORT_FORM = (By.CSS_SELECTOR, 'input#passportSeries')
    NUMBER_PASSPORT_FORM = (By.CSS_SELECTOR, 'input#passportNumber')
    ISSUE_DATE_PASSPORT_FORM = (By.XPATH, '//*[@id="dateOfIssue"]/div/input')
    DIVISION_CODE_PASSPORT_FORM = (By.CSS_SELECTOR, 'input#code')
    SNILS_PASSPORT_FORM = (By.XPATH, "/html//input[@id='cardId']")
    ORGANIZATION_PASSPORT_FORM = (By.XPATH, '//*[@id="issued"]')
    ADDRESS_PASSPORT_FORM = (By.CSS_SELECTOR, '[class="vue-dadata__input"]')
    PHONE_NUMBER_PASSPORT_FORM = (By.XPATH, '//*[@id="phone"]')
    CHECK_BOX_PASSPORT_FORM = (By.XPATH, '//*[@id="privacy"]')
    LINK_POLICY_PASSPORT_FORM = (By.XPATH, "a[target='_blank']")
    ATTACH_BUTTON_PASSPORT_FORM = (By.CSS_SELECTOR, ".upload-widget > input")
    SEND_BUTTON_PASSPORT_FORM = (By.CSS_SELECTOR, "[class='buttons'] :nth-of-type(2)")

    LOCATOR_DIPLOM_FORM = (By.CSS_SELECTOR, "div:nth-of-type(2) > .body.documents-tiles > div:nth-of-type(2)")
    ATTACH_BUTTON_DIPLOM_FORM = (By.CSS_SELECTOR, ".upload-widget > input")
    SEND_BUTTON_DIPLOM_FORM = (By.CSS_SELECTOR, ".btn.fill")

    LOCATOR_CONTRACT_FORM = (By.CSS_SELECTOR,
                             ".document-page div:nth-of-type(3) .status:nth-of-type(1) .document-status")
    ATTACH_BUTTON_CONTRACT_FORM = (By.CSS_SELECTOR, ".upload-widget > input")
    SEND_BUTTON_CONTRACT_FORM = (By.CSS_SELECTOR, ".btn.fill")

    LOCATOR_DECLARATION_FORM = (By.CSS_SELECTOR,
                                "div:nth-of-type(3) > .body.documents-tiles > div:nth-of-type(2) > .document-status")
    ATTACH_BUTTON_DECLARATION_FORM = (By.CSS_SELECTOR, ".upload-widget > input")
    SEND_BUTTON_DECLARATION_FORM = (By.CSS_SELECTOR, ".btn.fill")

    LOCATOR_AGREEMENT_FORM = (By.CSS_SELECTOR, ".body.documents-tiles > div:nth-of-type(3)")
    ATTACH_BUTTON_AGREEMENT_FORM = (By.CSS_SELECTOR, ".upload-widget > input")
    SEND_BUTTON_AGREEMENT_FORM = (By.CSS_SELECTOR, ".btn.fill")

    SELECTOR_LOGOUT = (By.CSS_SELECTOR, "img[alt='logout']")


class ChangePasswordSelector:
    HEADER_TIMETABLE = (By.CSS_SELECTOR, ".header h2")
    LOCATOR_USER_AVATAR = (By.CSS_SELECTOR, ".avatar_link_name")
    LOCATOR_SECURITY_TAB = (By.LINK_TEXT, "Безопасность и вход")
    LOCATOR_CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div:nth-of-type(2) > .icon > .name")
    FIELD_OLD_CHANGE_PASSWORD_FORM = (By.CSS_SELECTOR, "input#oldPassword")
    FIELD_NEW_CHANGE_PASSWORD_FORM = (By.CSS_SELECTOR, "input#newPassword")
    FIELD_REPEAT_CHANGE_PASSWORD_FORM = (By.CSS_SELECTOR, "input#confirmPassword")
    CONFIRM_BUTTON_CHANGE_PASSWORD_FORM = (By.CSS_SELECTOR, "form >.btn.fill")


link = "https://qa.neapro.site/"
LOGIN = '********'
PASSWORD = '11111111'
timeout_for_implicitly_wait = 5
current_dir = os.path.abspath(os.path.dirname(__file__))


# авторизация на бамблебу. Получает ссылку, отдает экземпляр браузера
def authorization(site):
    service = ChromeService(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get(site)
    browser.set_window_size(1920, 1080)
    browser.delete_all_cookies()
    browser.implicitly_wait(timeout_for_implicitly_wait)
    browser.find_element(*LoginPageSelector.LOGIN_MAIL_FIELD).send_keys(LOGIN)
    browser.find_element(*LoginPageSelector.LOGIN_PASSWORD_FIELD).send_keys(PASSWORD)
    browser.find_element(*LoginPageSelector.BUTTON_ENTER).click()
    return browser


#загрузка документа в форму, получаяя селекторы формы, отдает экземпляр браузера после загрузки
def loading_document(form_locator, button_attach_locator, button_send_locator):
    browser = authorization(link)
    browser.find_element(*form_locator).click()
    file_path = os.path.join(current_dir, 'passport.jpeg')
    browser.find_element(*button_attach_locator).send_keys(file_path)
    locator_type = button_send_locator[0]
    iam_locator = button_send_locator[1]
    WebDriverWait(browser, 5).until(
        expected_conditions.element_to_be_clickable((locator_type, iam_locator)))
    browser.find_element(*button_send_locator).click()
    return browser


#выход. Получает и отдаёт экземпляр браузера
def logout(browser):
    WebDriverWait(browser, 7).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".menu-header")))
    element = browser.find_element(By.CSS_SELECTOR, ".logo_icon")
    actions = ActionChains(browser)
    actions.move_to_element(element).perform()
    browser.find_element(*MainPageSelector.SELECTOR_LOGOUT).click()
    return browser


def test_authorization_new_user():
    browser = authorization(link)
    browser.find_element(*MainPageSelector.LOCATOR_PASSPORT_FORM)
    current_url = browser.current_url
    browser.quit()
    assert 'https://qa.neapro.site/cabinet/documents' == current_url, f'Wrong mainpage - {current_url}'


def test_upload_passport_form():
    browser = authorization(link)
    browser.find_element(*MainPageSelector.LOCATOR_PASSPORT_FORM).click()
    header_form = browser.find_element(By.CSS_SELECTOR, "[class='form-title title-header']").text
    assert 'Паспорт' == header_form, f'Wrong name form - {header_form}'
    browser.find_element(*MainPageSelector.LAST_NAME_PASSPORT_FORM).send_keys('Бутузов')
    browser.find_element(*MainPageSelector.FIRST_NAME_PASSPORT_FORM).send_keys('Максим')
    browser.find_element(*MainPageSelector.PATRONYMIC_PASSPORT_FORM).send_keys('Сергеевич')
    browser.find_element(*MainPageSelector.BIRTHDAY_PASSPORT_FORM).send_keys('01.03.1989')
    browser.find_element(*MainPageSelector.SERIES_PASSPORT_FORM).click()
    browser.find_element(*MainPageSelector.SERIES_PASSPORT_FORM).clear()
    browser.find_element(*MainPageSelector.SERIES_PASSPORT_FORM).send_keys('1212')
    browser.find_element(*MainPageSelector.NUMBER_PASSPORT_FORM).click()
    browser.find_element(*MainPageSelector.NUMBER_PASSPORT_FORM).clear()
    browser.find_element(*MainPageSelector.NUMBER_PASSPORT_FORM).send_keys('123123')
    browser.find_element(*MainPageSelector.ISSUE_DATE_PASSPORT_FORM).send_keys('01.03.1999')
    browser.find_element(*MainPageSelector.DIVISION_CODE_PASSPORT_FORM).click()
    browser.find_element(*MainPageSelector.DIVISION_CODE_PASSPORT_FORM).clear()
    browser.find_element(*MainPageSelector.DIVISION_CODE_PASSPORT_FORM).send_keys('123123')
    browser.find_element(*MainPageSelector.SNILS_PASSPORT_FORM).click()
    browser.find_element(*MainPageSelector.SNILS_PASSPORT_FORM).clear()
    browser.find_element(*MainPageSelector.SNILS_PASSPORT_FORM).send_keys('12312312312')
    browser.find_element(*MainPageSelector.ORGANIZATION_PASSPORT_FORM).send_keys('Организация')
    browser.find_element(*MainPageSelector.ADDRESS_PASSPORT_FORM)\
        .send_keys('Оренбургская обл, г Орск, пр-кт Ленина, д 96, кв 28')
    browser.find_element(By.CSS_SELECTOR, ".vue-dadata__suggestions-item").click()
    browser.find_element(*MainPageSelector.PHONE_NUMBER_PASSPORT_FORM).click()
    browser.find_element(*MainPageSelector.PHONE_NUMBER_PASSPORT_FORM).clear()
    browser.find_element(*MainPageSelector.PHONE_NUMBER_PASSPORT_FORM).send_keys('1231231212')
    #browser.find_element(*MainPageSelector.CHECK_BOX_PASSPORT_FORM).click()
    file_path = os.path.join(current_dir, 'passport.jpeg')
    browser.find_element(*MainPageSelector.ATTACH_BUTTON_PASSPORT_FORM).send_keys(file_path)
    browser.execute_script("window.scrollTo(0, 1080)")
    WebDriverWait(browser, 5).until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[class='buttons'] :nth-of-type(2)")))
    browser.find_element(*MainPageSelector.SEND_BUTTON_PASSPORT_FORM).click()
    passport_button = browser.find_element(*MainPageSelector.LOCATOR_PASSPORT_FORM)
    assert passport_button, f'Not found passport button'
    browser.quit()


def test_upload_diplom_form():
    browser = loading_document(MainPageSelector.LOCATOR_DIPLOM_FORM,
                     MainPageSelector.ATTACH_BUTTON_DIPLOM_FORM, MainPageSelector.SEND_BUTTON_DIPLOM_FORM)
    diplom_button = browser.find_element(*MainPageSelector.LOCATOR_PASSPORT_FORM)
    assert diplom_button, f'Not found diplom button'
    browser.quit()


def test_upload_contract_form():
    browser = loading_document(MainPageSelector.LOCATOR_CONTRACT_FORM,
                               MainPageSelector.ATTACH_BUTTON_CONTRACT_FORM,
                               MainPageSelector.SEND_BUTTON_CONTRACT_FORM)
    contract_button = browser.find_element(*MainPageSelector.LOCATOR_CONTRACT_FORM)
    assert contract_button, f'Not found contract button'
    browser.quit()


def test_upload_declaration_form():
    browser = loading_document(MainPageSelector.LOCATOR_DECLARATION_FORM,
                               MainPageSelector.ATTACH_BUTTON_DECLARATION_FORM,
                               MainPageSelector.SEND_BUTTON_DECLARATION_FORM)
    declaration_button = browser.find_element(*MainPageSelector.LOCATOR_CONTRACT_FORM)
    assert declaration_button, f'Not found declaration button'
    browser.quit()


def test_upload_agreement_form():
    browser = loading_document(MainPageSelector.LOCATOR_AGREEMENT_FORM,
                               MainPageSelector.ATTACH_BUTTON_AGREEMENT_FORM,
                               MainPageSelector.SEND_BUTTON_AGREEMENT_FORM)
    agreement_button = browser.find_element(*MainPageSelector.LOCATOR_AGREEMENT_FORM)
    assert agreement_button, f'Not found agreement button'
    browser.quit()


def test_change_password():
    browser = authorization(link)
    assert browser.find_element(*ChangePasswordSelector.HEADER_TIMETABLE).text == 'Расписание', f'Wrong page'
    WebDriverWait(browser, 6).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".menu-header")))
    element = browser.find_element(By.CSS_SELECTOR, ".logo_icon")
    actions = ActionChains(browser)
    actions.move_to_element(element).perform()
    browser.find_element(*ChangePasswordSelector.LOCATOR_USER_AVATAR).click()
    WebDriverWait(browser, 8).until(
        expected_conditions.presence_of_element_located((By.LINK_TEXT, "Безопасность и вход")))
    browser.find_element(*ChangePasswordSelector.LOCATOR_SECURITY_TAB).click()
    browser.find_element(*ChangePasswordSelector.LOCATOR_CHANGE_PASSWORD_BUTTON).click()
    current_url = browser.current_url
    assert current_url == 'https://qa.neapro.site/cabinet/security', f'Wrong url for security form'
    browser.find_element(*ChangePasswordSelector.FIELD_OLD_CHANGE_PASSWORD_FORM).send_keys('11111111')
    browser.find_element(*ChangePasswordSelector.FIELD_NEW_CHANGE_PASSWORD_FORM).send_keys('11111111')
    browser.find_element(*ChangePasswordSelector.FIELD_REPEAT_CHANGE_PASSWORD_FORM).send_keys('11111111')
    WebDriverWait(browser, 5).until(
                  expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "form >.btn.fill")))
    browser.find_element(*ChangePasswordSelector.CONFIRM_BUTTON_CHANGE_PASSWORD_FORM).click()
    browser.quit()


def test_logout():
    browser = authorization(link)
    WebDriverWait(browser, 8).until(
                                       expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".header h2")))
    current_url = browser.current_url
    assert current_url == 'https://qa.neapro.site/schedule', f'Wrong url after authorization'
    browser = logout(browser)
    WebDriverWait(browser, 8).until(
                             expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".login-form > .title")))
    assert browser.current_url == 'https://qa.neapro.site/login', f'Wrong url after logout'
    browser.quit()





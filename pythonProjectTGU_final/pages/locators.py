from selenium.webdriver.common.by import By


class MainPageLocators:
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".fieldset:nth-child(8)")
    LOGIN_MAIL_FIELD = (By.CSS_SELECTOR, ".fieldset:nth-child(1) input")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, ".fieldset:nth-child(2) input")
    BUTTON_ENTER = (By.CSS_SELECTOR, "button.btn.fill")

    LINK_FORGOT_PASSWORD = (By.CSS_SELECTOR, "[href='/recovery']")
    EMAIL_FIELD_RESET_PASSWORD = (By.CSS_SELECTOR, "input[placeholder = 'Ваш email']")


class PersonalAccountLocators:
    HEADER_MAIN_PAGE = (By.CSS_SELECTOR, ".content.document-page > .blender")
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

    HEADER_TIMETABLE = (By.CSS_SELECTOR, ".header h2")


class ChangePasswordLocators:
    HEADER_TIMETABLE = (By.CSS_SELECTOR, ".header h2")
    LOCATOR_USER_AVATAR = (By.CSS_SELECTOR, ".avatar_link_name")
    LOCATOR_SECURITY_TAB = (By.LINK_TEXT, "Безопасность и вход")
    LOCATOR_CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div:nth-of-type(2) > .icon > .name")
    FIELD_OLD_CHANGE_PASSWORD_FORM = (By.CSS_SELECTOR, "input#oldPassword")
    FIELD_NEW_CHANGE_PASSWORD_FORM = (By.CSS_SELECTOR, "input#newPassword")
    FIELD_REPEAT_CHANGE_PASSWORD_FORM = (By.CSS_SELECTOR, "input#confirmPassword")
    CONFIRM_BUTTON_CHANGE_PASSWORD_FORM = (By.CSS_SELECTOR, "form >.btn.fill")
    HEADER_CHANGE_PASSWORD_FORM = (By.CSS_SELECTOR,
              "#__layout > div > div.content-wrapper > div > div > div.content-page > div > div > div > div.body > div")
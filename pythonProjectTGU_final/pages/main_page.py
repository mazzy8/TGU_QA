from .base_page import BasePage
from .locators import PersonalAccountLocators
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_authorization_form_and_registration_button(self):
        self.should_be_login_form()
        self.should_be_registration_button()

    def should_be_main_page(self):
        cur_url = self.browser.current_url
        assert cur_url == 'https://qa.neapro.site', f'Wrong main page, https://qa.neapro.site !=  {cur_url}'

    def should_be_login_form(self):
        login_field = self.is_element_present(*MainPageLocators.LOGIN_MAIL_FIELD)
        password_field = self.is_element_present(*MainPageLocators.LOGIN_PASSWORD_FIELD)
        assert login_field and password_field, 'Not found login form'

    def should_be_open_personal_account_after_authorization_new_user(self):
        self.authorization_user()
        assert self.is_element_present(*PersonalAccountLocators.LOCATOR_PASSPORT_FORM), f'Not found passport button'

    def should_be_open_timetable_after_authorization_old_user(self):
        self.authorization_user()
        assert self.is_element_present(*PersonalAccountLocators.HEADER_TIMETABLE), f'Not found header timetable page'

    def should_be_registration_button(self):
        registration_button = self.is_element_present(*MainPageLocators.REGISTRATION_BUTTON)
        assert registration_button, f'Not found registration_button'

    def should_be_reset_password_form(self):
        self.browser.find_element(*MainPageLocators.LINK_FORGOT_PASSWORD).click()
        assert self.is_element_present(*MainPageLocators.EMAIL_FIELD_RESET_PASSWORD),\
            f'Not found reset password button'
        cur_url = self.browser.current_url
        assert 'https://qa.neapro.site/recovery' == cur_url, f'Wrong page, reset the password url !=  {cur_url}'

from .base_page import BasePage
from .locators import PersonalAccountLocators
from .locators import ChangePasswordLocators


class PersonalAccountPage(BasePage):
    def should_be_button_passport_after_authorization_new_user(self):
        self.authorization_user()
        assert self.is_element_present(*PersonalAccountLocators.LOCATOR_PASSPORT_FORM), f'Not found passport button'

    def should_be_main_page_after_logout(self):
        self.authorization_user()
        self.logout_user()
        cur_url = self.browser.current_url
        assert cur_url == 'https://qa.neapro.site', f'Wrong main page, https://qa.neapro.site !=  {cur_url}'

    def should_be_button_passport_after_load_passport_form(self):
        self.authorization_user()
        self.load_passport_form()
        assert self.is_element_present(*PersonalAccountLocators.LOCATOR_PASSPORT_FORM), f'Not found passport button'

    def should_be_diplom_button_after_load_diplom_form(self):
        self.load_document_in_diplom_form()
        assert self.is_element_present(*PersonalAccountLocators.LOCATOR_DIPLOM_FORM), f'Not found diplom button'

    def should_be_contract_button_after_load_contract_form(self):
        self.load_document_in_contract_form()
        assert self.is_element_present(*PersonalAccountLocators.LOCATOR_CONTRACT_FORM), f'Not found contract button'

    def should_be_declaration_button_after_load_declaration_form(self):
        self.load_document_in_declaration_form()
        assert self.is_element_present(*PersonalAccountLocators.LOCATOR_DECLARATION_FORM), \
            f'Not found declaration button'

    def should_be_agreement_button_after_load_agreement_form(self):
        self.load_document_in_agreement_form()
        assert self.is_element_present(*PersonalAccountLocators.LOCATOR_AGREEMENT_FORM), \
            f'Not found agreement button'

    def load_document_in_diplom_form(self):
        self.authorization_user()
        self.load_document_in_form(PersonalAccountLocators.LOCATOR_DIPLOM_FORM,
                                   PersonalAccountLocators.ATTACH_BUTTON_DIPLOM_FORM,
                                   PersonalAccountLocators.SEND_BUTTON_DIPLOM_FORM)

    def load_document_in_contract_form(self):
        self.authorization_user()
        self.load_document_in_form(PersonalAccountLocators.LOCATOR_CONTRACT_FORM,
                                   PersonalAccountLocators.ATTACH_BUTTON_CONTRACT_FORM,
                                   PersonalAccountLocators.SEND_BUTTON_CONTRACT_FORM)

    def load_document_in_declaration_form(self):
        self.authorization_user()
        self.load_document_in_form(PersonalAccountLocators.LOCATOR_DECLARATION_FORM,
                                   PersonalAccountLocators.ATTACH_BUTTON_DECLARATION_FORM,
                                   PersonalAccountLocators.SEND_BUTTON_DECLARATION_FORM)

    def load_document_in_agreement_form(self):
        self.authorization_user()
        self.load_document_in_form(PersonalAccountLocators.LOCATOR_AGREEMENT_FORM,
                                   PersonalAccountLocators.ATTACH_BUTTON_AGREEMENT_FORM,
                                   PersonalAccountLocators.SEND_BUTTON_AGREEMENT_FORM)

    def should_be_message_after_change_password(self):
        self.authorization_user()
        self.change_password()
        text_header = self.return_text_from_element_on_page(*ChangePasswordLocators.HEADER_CHANGE_PASSWORD_FORM)
        assert text_header == 'Пароль успешно изменен!', f'Error change password, {text_header}'





from .pages.personal_account_page import PersonalAccountPage
import pytest


link = "https://qa.neapro.site/"


@pytest.mark.new_user
def test_should_be_button_passport_after_authorization_new_user(browser):
    page = PersonalAccountPage(browser, link)
    page.should_be_button_passport_after_authorization_new_user()


@pytest.mark.new_user
def test_load_passport_form(browser):
    page = PersonalAccountPage(browser, link)
    page.should_be_button_passport_after_load_passport_form()


@pytest.mark.new_user
def test_load_diplom_form(browser):
    page = PersonalAccountPage(browser, link)
    page.should_be_diplom_button_after_load_diplom_form()


@pytest.mark.new_user
def test_load_contract_form(browser):
    page = PersonalAccountPage(browser, link)
    page.should_be_contract_button_after_load_contract_form()


@pytest.mark.new_user
def test_load_declaration_form(browser):
    page = PersonalAccountPage(browser, link)
    page.should_be_declaration_button_after_load_declaration_form()


@pytest.mark.new_user
def test_load_agreement_form(browser):
    page = PersonalAccountPage(browser, link)
    page.should_be_agreement_button_after_load_agreement_form()


@pytest.mark.confirmed_user
def test_change_password_user(browser):
    page = PersonalAccountPage(browser, link)
    page.should_be_message_after_change_password()


@pytest.mark.confirmed_user
def test_logout_user(browser):
    page = PersonalAccountPage(browser, link)
    page.should_be_main_page_after_logout()

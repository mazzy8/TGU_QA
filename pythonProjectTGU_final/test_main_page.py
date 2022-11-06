from .pages.main_page import MainPage
import pytest

link = "https://qa.neapro.site/"


@pytest.mark.requirements
def test_should_be_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_main_page()


@pytest.mark.requirements
def test_should_be_authorization_form_and_registration_button(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_authorization_form_and_registration_button()


@pytest.mark.new_user
@pytest.mark.smoke
def test_authorization_new_user(browser):
    page = MainPage(browser, link)
    page.should_be_open_personal_account_after_authorization_new_user()


def test_reset_password_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_reset_password_form()

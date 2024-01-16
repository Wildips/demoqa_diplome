import allure
from allure_commons.types import Severity
from demoqa_diplome_tests.models.pages.book_store_page import book_store_page


def test_login_book_store_without_data():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Вход на книжный склад")
    allure.dynamic.story("Вход не зарегистрированным пользователем")

    # ARRANGE (GIVEN)
    book_store_page.open("login")

    # ACTIONS (WHEN)
    book_store_page.click_login()

    # ASSERT (THEN)
    book_store_page.check_search_field_absence()

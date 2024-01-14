import allure
from allure_commons.types import Severity
from demoqa_diplome_tests.data.users import BookStoreUser
from demoqa_diplome_tests.models.pages.book_store_page import BookStorePage


def test_login_book_store():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Вход на книжный склад")
    allure.dynamic.story("Вход зарегистрированным пользователем")

    book_store_page = BookStorePage()

    # ARRANGE (GIVEN)
    user = BookStoreUser(
        first_name="Some", last_name="user", user_name="Someuser", password="AAAAaa@2"
    )

    book_store_page.open("login")

    # ACTIONS (WHEN)
    book_store_page.login_form_filling(user)
    book_store_page.click_login()

    # ASSERT (THEN)
    book_store_page.check_search_field_presence()

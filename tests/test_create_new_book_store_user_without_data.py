import allure
from allure_commons.types import Severity
from demoqa_diplome_tests.models.pages.book_store_page import book_store_page


def test_create_new_book_store_user_without_data():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Регистрация пользователя книжного склада")
    allure.dynamic.story("Вход не зарегистрированным пользователем")

    # ARRANGE (GIVEN)
    book_store_page.open("register")

    # ACTIONS (WHEN)
    book_store_page.click_register_user()

    # ASSERT (THEN)
    book_store_page.check_register_frame_presence()

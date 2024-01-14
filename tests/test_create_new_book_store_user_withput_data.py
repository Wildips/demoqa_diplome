import allure
from allure_commons.types import Severity
from data.users import BookStoreUser
from models.pages.book_store_page import BookStorePage


def test_login_book_store():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Вход на книжный склад")
    allure.dynamic.story("Вход зарегистрированным пользователем")

    book_store_page = BookStorePage()

    # ARRANGE (GIVEN)
    book_store_page.open("register")

    # ACTIONS (WHEN)
    book_store_page.click_register_user()

    # ASSERT (THEN)
    book_store_page.check_register_frame_presence()

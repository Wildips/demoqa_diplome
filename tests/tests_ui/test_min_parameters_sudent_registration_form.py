import allure
from allure_commons.types import Severity
from data.users import User
from model.pages.registration_page import RegistrationPage


def test_student_registration_form_min_params(browser_session):
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Регистрация пользователя")
    allure.dynamic.story(
        "Регистрация пользователя с минимально необходимым набором параметров"
    )

    registration_page = RegistrationPage(browser_session)

    # ARRANGE (GIVEN)
    student = User(
        first_name="Some",
        last_name="User",
        email="some@user.io",
        gender="Male",
        mobile="8800008800",
        date_of_birth="1 September,1939",
        current_address="Far far away",
    )

    registration_page.open()

    # ACTIONS (WHEN)
    registration_page.form_filling(student)
    registration_page.submit_form()

    # ASSERT (THEN)
    registration_page.should_registered_user_with(student)

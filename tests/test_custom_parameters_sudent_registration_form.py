import allure
from allure_commons.types import Severity
from utils import resource
from data.users import User, Subject
from models.pages.registration_page import RegistrationPage


def test_student_registration_form_custom_param(browser_session):
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Регистрация пользователя")
    allure.dynamic.story("Регистрация пользователя без обязательных параметров")

    registration_page = RegistrationPage(browser_session)

    # ARRANGE (GIVEN)
    student = User(
        date_of_birth="1 September,1939",
        subject=Subject.hindi.value,
        hobbies="Sports",
        image=resource.image_path("test.png"),
        state="Rajasthan",
        city="Jaipur",
    )

    registration_page.open()

    # ACTIONS (WHEN)
    registration_page.form_filling(student)
    registration_page.submit_form()

    # ASSERT (THEN)
    registration_page.check_submitting_form_absense()

import allure
from allure_commons.types import Severity
from demoqa_diplome_tests.utils import resource
from demoqa_diplome_tests.data.users import Student
from demoqa_diplome_tests.models.pages.registration_page import registration_page


def test_student_registration_form():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Регистрация пользователя")
    allure.dynamic.story("Регистрация пользователя с полным набором атрибутов")

    # ARRANGE (GIVEN)
    student = Student(
        first_name="Some",
        last_name="User",
        email="some@user.io",
        gender="Male",
        mobile="8800008800",
        date_of_birth="1 September,1939",
        subject="Hindi",
        hobbies="Sports",
        image=resource.image_path("test.png"),
        current_address="Far far away",
        state="Rajasthan",
        city="Jaipur",
    )

    registration_page.open()

    # ACTIONS (WHEN)
    registration_page.form_filling(student)
    registration_page.submit_form()

    # ASSERT (THEN)
    registration_page.should_registered_user_with(student)

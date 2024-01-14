import allure
from allure_commons.types import Severity
from demoqa_diplome_tests.utils import resource
from demoqa_diplome_tests.data.users import Student
from demoqa_diplome_tests.models.pages.registration_page import RegistrationPage


def test_student_registration_form_custom_param():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Регистрация пользователя")
    allure.dynamic.story("Регистрация пользователя без обязательных параметров")

    registration_page = RegistrationPage()

    # ARRANGE (GIVEN)
    student = Student(
        date_of_birth="1 September,1939",
        subject="Hindi",
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

import allure
from allure_commons.types import Severity
from demoqa_diplome_tests.models.pages.registration_page import RegistrationPage


def test_student_registration_form_empty_param():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Регистрация пользователя")
    allure.dynamic.story("Регистрация пользователя без указания параметров")

    registration_page = RegistrationPage()

    # ARRANGE (GIVEN)
    registration_page.open()

    # ACTIONS (WHEN)
    registration_page.submit_form()

    # ASSERT (THEN)
    registration_page.check_submitting_form_absense()

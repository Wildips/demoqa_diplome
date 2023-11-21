import allure
from allure_commons.types import Severity
from data.users import User, Subject
from model.pages.registration_page import RegistrationPage


def test_student_registration_form_empty_param(browser_session):
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Регистрация пользователя")
    allure.dynamic.story("Регистрация пользователя без указания параметров")

    # browser = browser_session
    registration_page = RegistrationPage(browser_session)

    # ARRANGE

    registration_page.open()

    # ACTIONS
    # registration_page.form_filling(student)
    registration_page.submit_form()

    # ASSERT
    registration_page.check_submitting_form_absense()

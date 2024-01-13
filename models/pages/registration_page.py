import allure
from selene import have, command, be

from data.users import User
from utils.log_extending import step


class RegistrationPage:
    def __init__(self, browser):
        self.browser = browser
        self.first_name = self.browser.element('[id="firstName"]')
        self.last_name = self.browser.element('[id="lastName"]')

        self.subject = self.browser.element('[id="subjectsInput"]')

    @step
    def open(self):
        with allure.step("Открываем главную страницу"):
            self.browser.open("/automation-practice-form").wait_until(
                have.title("DEMOQA")
            )

    @step
    def form_filling(self, user: User):
        with allure.step("Заполняем форму"):
            if user.first_name != "":
                self.first_name.type(user.first_name)
            if user.last_name != "":
                self.last_name.type(user.last_name)
            if user.gender != "":
                self.browser.all("[name=gender]").element_by(
                    have.value(user.gender)
                ).element("..").click()
            if user.mobile != "":
                self.browser.element('[id="userNumber"]').type(user.mobile)
            if user.email != "":
                self.browser.element('[id="userEmail"]').type(user.email)
            if user.date_of_birth != "":
                day = user.date_of_birth.split(" ")[0]
                if len(str(day)) == 1:
                    day = f"00{str(day)}"
                else:
                    day = f"0{str(day)}"
                month = user.date_of_birth.split(" ")[1].split(",")[0]
                year = user.date_of_birth.split(" ")[1].split(",")[1]
                self.browser.element('[id="dateOfBirthInput"]').click()
                self.browser.element('[class="react-datepicker__month-select"]').type(
                    month
                )
                self.browser.element('[class="react-datepicker__year-select"]').type(
                    year
                )
                self.browser.element(
                    f".react-datepicker__day--{day}:not(.react-datepicker__day--outside-month)"
                ).click()
            if user.subject != "":
                self.subject.click().type(user.subject).press_enter()
            if user.hobbies != "":
                self.browser.all(".custom-checkbox").element_by(
                    have.exact_text(user.hobbies)
                ).click()
            if user.image != "":
                self.browser.element('[id="uploadPicture"]').set_value(user.image)
            if user.current_address != "":
                self.browser.element('[id="currentAddress"]').type(user.current_address)
            if user.state != "":
                self.browser.element('[id="react-select-3-input"]').type(
                    user.state
                ).press_enter()
            if user.state != "" and user.city != "":
                self.browser.element('[id="react-select-4-input"]').type(
                    user.city
                ).press_enter()

    @step
    def submit_form(self):
        with allure.step("Отправляем форму"):
            self.browser.element('[id="submit"]').perform(command.js.click)

    @step
    def should_registered_user_with(self, user: User | None):
        with allure.step("Проверяем соответствие введенных данных полученным"):
            element = self.browser.element(
                '[class="table table-dark table-striped table-bordered table-hover"]'
            ).all("tr td:nth-child(2)")
            if user.image:
                element.should(
                    have.texts(
                        f"{user.first_name} {user.last_name}",
                        user.email,
                        user.gender,
                        user.mobile,
                        user.date_of_birth,
                        user.subject,
                        user.hobbies,
                        user.image[user.image.find(".") - len("test") :],
                        user.current_address,
                        f"{user.state} {user.city}",
                    )
                )
            else:
                element.should(
                    have.texts(
                        f"{user.first_name} {user.last_name}",
                        user.email,
                        user.gender,
                        user.mobile,
                        user.date_of_birth,
                        user.subject,
                        user.hobbies,
                        user.image,
                        user.current_address,
                        user.state,
                    )
                )

    @step
    def check_submitting_form_absense(self):
        with allure.step("Проверяем отсутствие формы результатов сабмита"):
            self.browser.element(
                '[class="table table-dark table-striped table-bordered table-hover"]'
            ).should(be.not_.present)

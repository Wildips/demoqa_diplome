import allure
from selene import browser, have, command, be
from demoqa_diplome_tests.data.users import Student


class RegistrationPage:
    def __init__(self):
        self.browser = browser
        self.first_name = self.browser.element("#firstName")
        self.last_name = self.browser.element("#lastName")
        self.subject = self.browser.element("#subjectsInput")

    def open(self):
        with allure.step("Открываем главную страницу"):
            self.browser.open("/automation-practice-form").wait_until(
                have.title("DEMOQA")
            )

    def form_filling(self, user: Student):
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
                self.browser.element("#userNumber").type(user.mobile)
            if user.email != "":
                self.browser.element("#userEmail").type(user.email)
            if user.date_of_birth != "":
                day = user.date_of_birth.split(" ")[0]
                if len(str(day)) == 1:
                    day = f"00{str(day)}"
                else:
                    day = f"0{str(day)}"
                month = user.date_of_birth.split(" ")[1].split(",")[0]
                year = user.date_of_birth.split(" ")[1].split(",")[1]
                self.browser.element("#dateOfBirthInput").click()
                self.browser.element(".react-datepicker__month-select").type(month)
                self.browser.element(".react-datepicker__year-select").type(year)
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
                self.browser.element("#uploadPicture").set_value(user.image)
            if user.current_address != "":
                self.browser.element("#currentAddress").type(user.current_address)
            if user.state != "":
                self.browser.element("#react-select-3-input").type(
                    user.state
                ).press_enter()
            if user.state != "" and user.city != "":
                self.browser.element("#react-select-4-input").type(
                    user.city
                ).press_enter()

    def submit_form(self):
        with allure.step("Отправляем форму"):
            self.browser.element("#submit").perform(command.js.click)

    def should_registered_user_with(self, user: Student | None):
        with allure.step("Проверяем соответствие введенных данных полученным"):
            element = self.browser.element(
                ".table.table-dark.table-striped.table-bordered.table-hover"
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

    def check_submitting_form_absense(self):
        with allure.step("Проверяем отсутствие формы результатов сабмита"):
            self.browser.element(
                ".table.table-dark.table-striped.table-bordered.table-hover"
            ).should(be.not_.present)


registration_page = RegistrationPage()

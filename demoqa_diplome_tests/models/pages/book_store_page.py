import allure
from selene import browser, have, command, be
from demoqa_diplome_tests.data.users import BookStoreUser


class BookStorePage:
    def __init__(self):
        self.browser = browser
        self.user_name = self.browser.element("#userName")
        self.password = self.browser.element("#password")
        self.first_name = self.browser.element("#firstname")
        self.last_name = self.browser.element("#lastname")

    def open(self, method_name):
        with allure.step("Открываем главную страницу"):
            self.browser.open(f"/{method_name}").wait_until(have.title("DEMOQA"))

    def login_form_filling(self, user: BookStoreUser):
        with allure.step("Заполняем форму входа"):
            self.browser.element("#userName.mr-sm-2.form-control").type(user.user_name)
            self.browser.element("#password.mr-sm-2.form-control").type(user.password)

    def click_login(self):
        with allure.step("Отправляем данные для входа"):
            self.browser.element("#login").perform(command.js.click)

    def click_new_user(self):
        with allure.step("Инициируем создание нового пользователя"):
            self.browser.element("#newUser").perform(command.js.click)

    def click_register_user(self):
        with allure.step("Регистрируем нового пользователя"):
            self.browser.element("#register").perform(command.js.click)

    def should_registered_user_with(self):
        with allure.step("Проверяем наличие кнопки logout"):
            self.browser.element("#submit").should(have.attribute("type", "Log out"))

    def new_user_form_filling(self, user: BookStoreUser):
        with allure.step("Заполняем форму регистрации пользователя книжного склада"):
            self.browser.element(self.first_name).type(user.first_name)
            self.browser.element(self.last_name).type(user.last_name)
            self.browser.element(self.user_name).type(user.user_name)
            self.browser.element(self.password).type(user.password)
            self.browser.element(".recaptcha-checkbox-border").click()

    def new_user_captcha_awaiting(self):
        with allure.step("Регистрируем нового пользователя"):
            self.browser.element(".recaptcha-checkbox-border").should(be.visible)

    def check_search_field_absence(self):
        with allure.step("Проверяем отсутствие поля поиска"):
            self.browser.element("#searchBox").should(be.not_.present)

    def check_register_frame_presence(self):
        with allure.step("Проверяем отсутствие поля поиска"):
            self.browser.element(".register-wrapper").should(be.visible)

    def check_search_field_presence(self):
        with allure.step("Проверяем наличие поля поиска"):
            self.browser.element("#searchBox").should(be.present)


book_store_page = BookStorePage()

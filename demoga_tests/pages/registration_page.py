from selene import have, be
from selene.support.shared import browser
from demoga_tests import resource
import allure


class RegistrationPage:

    def open(self):
        with allure.step('Открыть форму регистрации'):
            browser.open('https://demoqa.com/automation-practice-form')
        return self

    def fill_first_name(self, value):
        with allure.step('Заполнить имя'):
            browser.element('#firstName').should(be.visible).type(value)
        return self

    def fill_last_name(self, value):
        with allure.step('Заполнить фамилию'):
            browser.element('#lastName').should(be.visible).type(value)
        return self

    def fill_email(self, value):
        with allure.step('Заполнить e-mail'):
            browser.element('#userEmail').should(be.visible).type(value)
        return self

    def fill_gender(self):
        with allure.step('Выбрать пол'):
            browser.element('label[for="gender-radio-2"]').should(be.visible).click()
        return self

    def fill_number(self, value):
        with allure.step('Заполнить номер телефона'):
            browser.element('#userNumber').should(be.visible).type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        with allure.step('Заполнить дату рождения'):
            browser.element('#dateOfBirthInput').click()
            browser.element('.react-datepicker__month-select').type(month)
            browser.element('.react-datepicker__year-select').type(year)
            browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def choose_subject(self, value):
        with allure.step('Выбрать направление'):
            browser.element('#subjectsInput').type(value).press_enter()
        return self

    def choose_hobbies(self):
        with allure.step('Выбрать хобби'):
            browser.element('label[for="hobbies-checkbox-3"]').click()
        return self

    def upload_picture(self, value):
        with allure.step('Загрузить картинку'):
            browser.element('#uploadPicture').should(be.visible).type(resource.path(value))
        return self

    def fill_current_address(self, value):
        with allure.step('Написать адрес'):
            browser.element('#currentAddress').type(value)
        return self

    def choose_state(self, value):
        with allure.step('Страна'):
            browser.element('//*[@id="react-select-3-input"]').type(value).press_enter()
        return self

    def choose_city(self, value):
        with allure.step('Город'):
            browser.element('//*[@id="react-select-4-input"]').type(value).press_enter()
        return self

    def submit_form(self):
        with allure.step('Отправить данные'):
            browser.element("#submit").execute_script("element.click()")
        return self

    def should_registered_user_with(self, full_name, email, gender, phone_number, date_of_birth, subject, hobby,
                                    picture, state, city):
        with allure.step('Проверить данные студента'):
            browser.element('.table').all('tr td:nth-child(2)').should(have.texts(
                full_name,
                email,
                gender,
                phone_number,
                date_of_birth,
                subject,
                hobby,
                picture,
                state,
                city
            )
            )
        return self

import os

from selene import browser, command, have


class RegistrationPage:
    def __init__(self):
        self.gender_male = '[for="gender-radio-1"]'

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def choose_gender(self):
        browser.element(self.gender_male).click()

    def fill_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select').element(f'[value="{year}"]').click()
        browser.element('.react-datepicker__month').element(f'.react-datepicker__day--0{day}').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def choose_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()

    def upload_picture(self):
        browser.element('#uploadPicture').send_keys(os.path.abspath('homework.png'))

    def fill_adress(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, value):
        browser.element('#state').element('#react-select-3-input').type(value).press_enter()

    def fill_city(self, value):
        browser.element('#city').element('#react-select-4-input').type(value).press_enter()

    def press_submit(self):
        browser.element('#submit').perform(command.js.scroll_into_view).click()

    def should_registered_user_with(self, full_name, email, gender, phone_number, date_of_birth, subjects, hobby,
                                    upload_picture,
                                    adress, state_and_city):
        browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(have.texts(
            full_name,
            email,
            gender,
            phone_number,
            date_of_birth,
            subjects,
            hobby,
            upload_picture,
            adress,
            state_and_city))

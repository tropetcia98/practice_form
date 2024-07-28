import os
from selene import browser, command, have
from practice_form.data.users import User


class RegistrationPage:
    def __init__(self):
        self.name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('[for="gender-radio-1"]')
        self.phone_number = browser.element('#userNumber')
        self.month = browser.element('.react-datepicker__month-select')
        self.year = browser.element('.react-datepicker__year-select')
        self.subject = browser.element('#subjectsInput')
        self.hobby = browser.element('[for="hobbies-checkbox-1"]')
        self.address = browser.element('#currentAddress')
        self.state = browser.element('#state').element('#react-select-3-input')
        self.city = browser.element('#city').element('#react-select-4-input')
        self.submit = browser.element('#submit')

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        self.name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def choose_gender(self):
        self.gender.click()

    def fill_number(self, value):
        self.phone_number.type(value)

    def fill_date_of_birth(self, value_day, value_month, value_year):
        browser.element('#dateOfBirthInput').click()
        self.month.click()
        self.month.type(value_month)
        self.year.click()
        self.year.element(f'[value="{value_year}"]').click()
        browser.element('.react-datepicker__month').element(f'.react-datepicker__day--0{value_day}').click()

    def fill_subject(self, value):
        self.subject.type(value).press_enter()

    def choose_hobbies(self):
        self.hobby.click()

    def upload_picture(self):
        browser.element('#uploadPicture').send_keys(os.path.abspath('homework.png'))

    def fill_address(self, value):
        self.address.type(value)

    def fill_state(self, value):
        self.state.type(value).press_enter()

    def fill_city(self, value):
        self.city.type(value).press_enter()

    def press_submit(self):
        self.submit.perform(command.js.scroll_into_view).click()

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.choose_gender()
        self.fill_number(user.phone_number)
        self.fill_date_of_birth(user.day_of_birth, user.month_of_birth, user.year_of_birth)
        self.fill_subject(user.subjects)
        self.choose_hobbies()
        self.upload_picture()
        self.fill_address(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.press_submit()

    def should_registered_user_with(self, user: User):
        browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(have.texts(
            f'{user.first_name} {user.last_name}',
            f'{user.email}',
            f'{user.gender}',
            f'{user.phone_number}',
            f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}',
            f'{user.subjects}',
            f'{user.hobby}',
            f'{user.picture}',
            f'{user.address}',
            f'{user.state} {user.city}'))

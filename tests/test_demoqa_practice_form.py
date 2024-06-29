import os
from selene import browser, have, be


def test_practice_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type("Roman")
    browser.element('#lastName').type("Tropin")
    browser.element('#userEmail').type("tropetcia967@gmail.com")
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('89009005555')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element('[value="1"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element('[value="1998"]').click()
    browser.element('.react-datepicker__month').element('.react-datepicker__day--011').click()
    browser.element('#subjectsInput').type('phy').press_enter()
    browser.element('#subjectsInput').type("computer").press_enter()
    browser.element(('[for="hobbies-checkbox-1"]')).click()
    browser.element(('[for="hobbies-checkbox-2"]')).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('homework.png'))
    browser.element('#currentAddress').type('116 N 2nd St, Cave City, KY 42127, USA')
    browser.element('#state').element('#react-select-3-input').type('Uttar').press_enter()
    browser.element('#city').element('#react-select-4-input').type('Mer').press_enter()
    browser.element('#submit').click()

    browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(have.exact_texts(
        'Roman Tropin',
        'tropetcia967@gmail.com',
        'Male',
        '8900900555',
        '11 March,1998',
        'Physics, Computer Science',
        'Sports, Reading',
        'homework.png',
        '116 N 2nd St, Cave City, KY 42127, USA',
        'Uttar Pradesh Merrut'))

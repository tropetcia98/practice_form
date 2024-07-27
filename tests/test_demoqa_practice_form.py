from model.pages.registration_page import RegistrationPage


def test_practice_form():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('Roman')
    registration_page.fill_last_name('Tropin')
    registration_page.fill_email('tropetcia967@gmail.com')
    registration_page.choose_gender()
    registration_page.fill_number('89009005555')
    registration_page.fill_date_of_birth('11', 'February', '1998')
    registration_page.fill_subject('physic')
    registration_page.fill_subject('computer')
    registration_page.choose_hobbies()
    registration_page.upload_picture()
    registration_page.fill_adress('116 N 2nd St, Cave City, KY 42127, USA')
    registration_page.fill_state('Uttar')
    registration_page.fill_city('Mer')
    registration_page.press_submit()

    registration_page.should_registered_user_with(
        'Roman Tropin',
        'tropetcia967@gmail.com',
        'Male',
        '8900900555',
        '11 February,1998',
        'Physics, Computer Science',
        'Sports',
        'homework.png',
        '116 N 2nd St, Cave City, KY 42127, USA',
        'Uttar Pradesh Merrut')

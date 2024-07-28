from practice_form.data.users import user
from practice_form.model.pages.registration_page import RegistrationPage


def test_practice_form():
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.register(user)
    registration_page.should_registered_user_with(user)

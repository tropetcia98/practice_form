import allure

from practice_form.data.users import user
from practice_form.pages.registration_page import RegistrationPage


def test_practice_form():
    registration_page = RegistrationPage()

    with allure.step('Открытие бразуера'):
        registration_page.open()

    with allure.step('Регистрация пользователя'):
        registration_page.register(user)

    with allure.step('Проверяем данные пользователя'):
        registration_page.should_registered_user_with(user)

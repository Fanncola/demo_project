import allure
from pages.auth_page import AuthPage
import os
import dotenv


@allure.title('Авторизация пользователя')
def test_open_auth_page():
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    auth_page = AuthPage()

    with allure.step('Открываем страницу авторизации'):
        auth_page.open()

    with allure.step('Проверяем наличие заголовка'):
        auth_page.have_title('Swag Labs')

    with allure.step('Заполняем логин и пароль'):
        auth_page.fill_auth_form(login=login, password=password)

    with allure.step('Отправляем форму авторизации'):
        auth_page.submit_form()


import allure
import os
from selene import browser, have
from pages.auth_page import AuthPage
from pages.pages import Pages

auth_page = AuthPage()


class TestAuth:

    @allure.feature('Авторизация пользователя')
    @allure.tag('auth')
    @allure.title('Успешная авторизация пользователя')
    def test_success_auth(self):
        with allure.step('Открываем страницу авторизации'):
            auth_page.open()

        with allure.step('Проверяем наличие заголовка'):
            auth_page.have_title('Swag Labs')

        with allure.step('Заполняем логин и пароль'):
            auth_page.fill_auth_form(login=os.getenv('STANDART_USER'), password=os.getenv('USER_PASSWORD'))

        with allure.step('Отправляем форму авторизации'):
            auth_page.submit_form()

        with allure.step('Пользователь находится на странице выбора товаров'):
            browser.should(have.url_containing(Pages.main_page))

    @allure.title('Авторизация заблокированным пользователем')
    def test_auth_with_locked_user(self):
        with allure.step('Открываем страницу авторизации'):
            auth_page.open()

        with allure.step('Проверяем наличие заголовка'):
            auth_page.have_title('Swag Labs')

        with allure.step('Заполняем логин и пароль'):
            auth_page.fill_auth_form(login=os.getenv('LOCKED_USER'), password=os.getenv('USER_PASSWORD'))

        with allure.step('Отправляем форму авторизации'):
            auth_page.submit_form()

        with allure.step('Отображается ошибка для забокированного пользователя'):
            auth_page.locked_user_error()

        with allure.step('Пользователь остается на странице авторизации'):
            browser.should(have.url_containing(Pages.auth_page))

    @allure.title('Авторзация пользователя с неверным паролем')
    def test_auth_with_incorrect_password(self):
        with allure.step('Открываем страницу авторизации'):
            auth_page.open()

        with allure.step('Проверяем наличие заголовка'):
            auth_page.have_title('Swag Labs')

        with allure.step('Заполняем логин и пароль'):
            auth_page.fill_auth_form(login=os.getenv('LOCKED_USER'), password=os.getenv('INCORRECT_PASSWORD'))

        with allure.step('Отправляем форму авторизации'):
            auth_page.submit_form()

        with allure.step('Отображается ошибка для забокированного пользователя'):
            auth_page.incorrect_password()

        with allure.step('Пользователь остается на странице авторизации'):
            browser.should(have.url_containing(Pages.auth_page))

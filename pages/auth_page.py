from selene import browser, have


class AuthPage:

    def __init__(self):
        self.user_name = browser.element('[data-test="username"]')
        self.password = browser.element('[data-test="password"]')
        self.submit = browser.element('[data-test="login-button"]')
        self.error_block = browser.element('[data-test="error"]')
        self.error_block_text = 'Epic sadface: Sorry, this user has been locked out.'

    @staticmethod
    def open():
        browser.open('/')

    @staticmethod
    def have_title(title):
        browser.should(have.title(title))

    def fill_auth_form(self, login, password):
        self.user_name.type(login)
        self.password.type(password)

    def submit_form(self):
        self.submit.submit()

    def locked_user_error(self):
        self.error_block.should(have.text(self.error_block_text))

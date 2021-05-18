import random

from base_page import BasePage
from locators_1.locators_city_registration import RegistrationFieldLocator, ButtonLocator


class LoginPage(BasePage):
    # def should_be_login_page(self):
    #     self.should_be_login_url()

    # self.should_be_login_form()
    # self.should_be_register_form()

    # def should_be_login_url(self):
    #     current_url = self.browser.current_url
    #     assert '/login/' in current_url
    #
    # def should_be_login_form(self):
    #     assert self.get_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
    #
    # def should_be_register_form(self):
    #     assert self.get_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def create_user_data(self, ):
        num = int(random.random() * 10000)
        first_name = f"Marko{num}"
        last_name = f"Polo{num}"
        mail_address = f"mymail{num}@mail.com"
        phone_number = f"+38093517{num}"
        password = "21071976#ED2wsqwer"
        password_confirm = password

        return first_name, last_name, mail_address, phone_number, password, password_confirm

    def add_new_user(self):
        first_name, last_name, mail_address, phone_number, password, password_confirm, = self.create_user_data()

        registration_button_first = self.get_element_present(*ButtonLocator.REGIST_BUTTON)
        registration_button_first.click()

        name_field = self.get_element_present(*RegistrationFieldLocator.FIED_NAME)
        last_name_field = self.get_element_present(*RegistrationFieldLocator.FIED_LAST_NAME)
        email_field = self.get_element_present(*RegistrationFieldLocator.EMAIL_FIELD)
        phone_field = self.get_element_present(*RegistrationFieldLocator.PHONE_FIELD)
        password_field = self.get_element_present(*RegistrationFieldLocator.PASSWORD_FIELD)
        password_confirm_search = self.get_element_present(*RegistrationFieldLocator.PASSWORD_CONFIRM_FIELD)

        self.enter_data_in_the_fill_field(name_field, first_name)
        self.enter_data_in_the_fill_field(last_name_field, last_name)
        self.enter_data_in_the_fill_field(email_field, mail_address)
        self.enter_data_in_the_fill_field(phone_field, phone_number)
        self.enter_data_in_the_fill_field(password_field, password)
        self.enter_data_in_the_fill_field(password_confirm_search, password_confirm)

        check_box_click = self.get_element_present(*ButtonLocator.CHECK_BOX_TERM)
        check_box_click.click()

        registration_button = self.get_element_present(*ButtonLocator.REGISTRATION_BUTTON_NEXT_PAGE)
        registration_button.click()



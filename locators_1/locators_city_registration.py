from selenium.webdriver.common.by import By


class RegistrationFieldLocator:
    FIED_NAME = (By.NAME, "first_name")
    FIED_LAST_NAME = (By.NAME, "last_name")
    EMAIL_FIELD = (By.NAME, "email")
    PHONE_FIELD = (By.NAME, "phone")
    PASSWORD_FIELD = (By.NAME, "password")
    PASSWORD_CONFIRM_FIELD = (By.NAME, "password_confirmation")
    CHECK_BOX_FIELD = (By.CLASS_NAME, "form-checkbox")


class ButtonLocator:
    REGIST_BUTTON = (By.XPATH, '//a[contains(text(),"Регистрация")]')
    REGISTRATION_BUTTON_NEXT_PAGE = (By.XPATH, "//button[contains(text(),'Регистрация')]")
    CHECK_BOX_TERM = (By.XPATH, "//input[@name='terms']")


class PresentElement:
    NEXT_PAGE_ELEMENT = (By.XPATH, '//span[contains(text(),"Профиль")]')


# CALENDAR_FIELD_CHECKOUT = (By.XPATH, "//div[(@data-mode='checkout')]")
# CALENDAR_FIELD_CHECKIN = (By.XPATH, "//div[(@data-mode='checkin')]")
# TODAY_CALENDAR_DATA = (By.XPATH, "//td[contains(@class,'bui-calendar__date bui-calendar__date--today')]")
# ANY_DAY = (By.XPATH, f'//td[contains(@data-date,"{add_some_day()}")]')
# NEXT_PAGE_INDICATOR = (By.XPATH, "//button[contains(@class,'show_map entry-point__map_small')]")
#
# VISIBLE_CITY_FIELD = (By.XPATH, "//ul[@aria-label='List of suggested destinations ']")
#
# DATA_CALENDAR_FIELD_2 = (By.CLASS_NAME, "bui-calendar__date bui-calendar__date--selected")
#
# SEARCH_BUTTON = (By.XPATH, "//button[contains(@class,'sb-searchbox__button')]")
#
# CALENDAR_FIELD_NEXT_PAGE = (By.XPATH, "//div[@class='bui-calendar__main b-a11y-calendar-contrasts']")

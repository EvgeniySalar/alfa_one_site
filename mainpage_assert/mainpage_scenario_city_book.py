from base_page import BasePage
from locators_1.locators_city_registration import PresentElement


class  NextPageVerification(BasePage):
    def next_page_elem_preset(self):
        city_field = self.is_not_element_present(*PresentElement.NEXT_PAGE_ELEMENT)
        return city_field


class PageVerification(NextPageVerification):

    def open_the_next_page(self):
        assert self.next_page_elem_preset().is_displayed(), "Page is not opened"
        print("Registration passed successfully")



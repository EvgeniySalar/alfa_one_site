import pytest

from login_page import LoginPage
from mainpage_assert.mainpage_scenario_city_book import PageVerification


class TestSiteFuncScr():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, chrome_drv):
        login_page = LoginPage(chrome_drv)
        # login_page.open()
        login_page.add_new_user()
        self.main_page = PageVerification(chrome_drv)
        yield

    def test_transition_the_next_page(self):

        self.main_page.open_the_next_page()
    #
    # def test_search_button_click(self):
    #     self.home_page.search_button_selection()
    #     self.main_page.open_the_next_page()
    #
    # # @pytest.mark.skip(reason="no way of currently testing this")
    # # @pytest.mark.s
    # # @pytest.mark.xfail
    # def test_calendar_field(self):
    #     # self.pages.calendar_field()
    #     self.main_page.calendar_day_today_check()
    #     self.home_page.calendar_today_data()
    #     self.home_page.calendar_field_out()
    #     self.main_page.calendar_next_day_check()
    #     self.home_page.calendar_next_day_data()
    #     self.home_page.search_button_selection()
    #     self.main_page.go_next_step()

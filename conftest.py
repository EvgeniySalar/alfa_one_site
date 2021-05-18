import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# from prestashop.url_contains.data_prestashop_url import MAIN_PAGE_URL as m
# print(m)
# from prestashop.url_contains.data_prestashop_url import MAIN_PAGE_URL as main_page_url
# print(main_page_url)
# from dataurl import MAIN_PAGE_URL


MAIN_PAGE_URL = "https://trading.alfa-one-capital.com"



@pytest.fixture(scope="session")
def chrome_drv():
    """
    Запуск драйвера через webdriver_manager.chrome
    :param :
    :return:
    """
    print("\nstart chrome browser for test..")
    mauser = webdriver.Chrome(ChromeDriverManager().install())
    mauser.maximize_window()
    mauser.implicitly_wait(30)
    mauser.get(MAIN_PAGE_URL)
    yield mauser
    print("\nquit browser..")
    mauser.quit()



    # def resource_teardown():
    #     print("module teardown")
    #     print("\nquit browser..")
    #     driver.quit()
    #     request.addfinalizer(resource_teardown)
    #     return driver

# yield driver
#     print("\nquit browser..")
#     driver.quit()
#     return driver

import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



# """
# Вариант запуска кода без прописанного пути, chromedriver, находится в папки проекта
# """
# file_name = "drivers\\chromedriver.exe"
# dvs = os.path.abspath(file_name)
# driver = webdriver.Chrome(dvs)
# driver.get("https://coderoad.ru/")
"""
Запуск драйвера через webdriver_manager.chrome
"""

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://trading.alfa-one-capital.com")

#

def test_homepage(self):
    self.driver.get("https://trading.alfa-one-capital.com")
    self.assertEqual("Alfa One Capital", self.driver.title, "webpage title is not matching")


def test_regfprm(self):
    self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/a[1]').click()
    self.driver.find_element_by_name('first_name').send_keys('Mark1')
    self.driver.find_element_by_name('last_name').send_keys('POlo')
    self.driver.find_element_by_name('email').send_keys('mark1sw@mail.ru')
    self.driver.find_element_by_name('phone').send_keys('123345671')
    self.driver.find_element_by_name('password').send_keys('123456781')
    self.driver.find_element_by_name('password_confirmation').send_keys('123456781')
    self.driver.find_element_by_class_name('form-checkbox').click()
    #time.sleep(10)
    self.driver.find_element_by_xpath('//button[contains(text(),'Регистрация')]').click()
    self.assertEqual("Alfa One Capital", self.driver.title, "webpage title is not matching")

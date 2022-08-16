from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:\\WebDriver\\bin\\chromedriver.exe')

   pytest.driver.set_window_size(1400, 1000)
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

   yield


   pytest.driver.quit()
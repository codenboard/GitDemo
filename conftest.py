import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("C:/Users/sasdg/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class testOne:

    def test_e2e(self, setup):
        self.driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
        self.driver.find_elements(By.XPATH, "//div[@class='products']/div")
        products = self.driver.find_elements(By.XPATH, "//div[@class='products']/div")

        for product in products:
            product.find_element(By.XPATH, "div/button").click()

        # time.sleep(5)
        # driver.find_element(By.XPATH, "//img[@alt = 'Cart']").click()
        #
        # driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()
        # driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys('rahulshettyacademy')
        #
        # driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
        # time.sleep(5)
        # discounted_amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
        # products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
        #
        # prices = driver.find_elements(By.XPATH, "//td[5]/p")
        # sum1 = 0
        # for price in prices:
        # sum1 = sum1 + int(price.text)
        # print(sum1)
        # amount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
        # assert sum1 == amount
        #
        # assert amount > discounted_amount

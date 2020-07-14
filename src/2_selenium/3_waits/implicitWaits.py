# 1. Implicit wait
# 2. explicit wait
# 3. python wait (time.sleep(3))
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="D:\\Devdatta\\Projects\\Python\\SeleniumPython_Practice\\resources"
                                           "\\browsers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(5)
products = len(driver.find_elements_by_css_selector(".products > div"))
assert products == 3
buttons = driver.find_elements_by_css_selector(".product .product-action button")
assert len(buttons) == 3

for btn in buttons:
    btn.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_css_selector(".action-block button").click()
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
msg = driver.find_element_by_css_selector(".promoInfo").text
assert msg == "Code applied ..!"

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="D:\\Devdatta\\Projects\\Python\\SeleniumPython_Practice\\resources"
                                           "\\browsers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
name = "devdatta"
driver.find_element_by_id("name").send_keys(name)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
alert.accept()
assert name in alert_text

driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert
alert.dismiss()


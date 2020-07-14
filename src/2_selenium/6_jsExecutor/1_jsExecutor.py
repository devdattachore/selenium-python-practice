from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\\Devdatta\\Projects\\Python\\SeleniumPython_Practice\\resources"
                                           "\\browsers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice")

driver.find_element_by_name("name").send_keys("helloooooo")
print(driver.execute_script("return document.getElementsByName('name')[0].value"))

# scroll using js exec as selenium does not support scorrling feature
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
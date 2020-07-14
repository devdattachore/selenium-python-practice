from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="D:\\Devdatta\\Projects\\Python\\SeleniumPython_Practice\\resources"
                                           "\\browsers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
driver.find_element_by_name("name").send_keys("Devdatta")
driver.find_element_by_name("email").send_keys("devdatta@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("devdatta")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//*[@type='submit']").click()
gender_select_list = Select(driver.find_element_by_id("exampleFormControlSelect1"))
gender_select_list.select_by_visible_text("Male")
print(driver.find_element_by_class_name("alert-success").text)
actAlert = driver.find_element_by_class_name("alert-success").text
expAlert = "Success! The Form has been submitted successfully!."
assert expAlert in actAlert
driver.quit()

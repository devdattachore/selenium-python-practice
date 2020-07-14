from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Devdatta\\Projects\\Python\\SeleniumPython_Practice\\resources"
                                           "\\browsers\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()
print(driver.find_element_by_tag_name("h3").text)

driver.switch_to.window(driver.window_handles[1])
print(driver.find_element_by_tag_name("h3").text)

driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name("h3").text)
driver.quit()

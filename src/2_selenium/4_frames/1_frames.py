from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Devdatta\\Projects\\Python\\SeleniumPython_Practice\\resources"
                                           "\\browsers\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")


# developers use iframe/frameset/frame in code for frames

driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("working with frames")
print(driver.find_element_by_id("tinymce").text)
driver.quit()

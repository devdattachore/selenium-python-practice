from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\\Devdatta\\Projects\\Python\\SeleniumPython_Practice\\resources"
                                           "\\browsers\\chromedriver.exe")
driver.get("https://familysearch.org/en")

action = ActionChains(driver)

action.move_to_element(driver.find_element_by_css_selector("[aria-owns='search']")).click().perform()
# Not working

action.move_to_element(driver.find_element_by_css_selector("[data-test='genealogies']")).click().perform()

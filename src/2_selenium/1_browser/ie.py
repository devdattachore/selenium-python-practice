from selenium import webdriver

driver = webdriver.Ie(executable_path="D:\\Devdatta\\Projects\\Python\\SeleniumPython_Practice\\resources"
                                           "\\browsers\\IEDriverServer.exe")
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
# driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.refresh()
driver.back()
driver.quit()

from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("--headless")

driver = webdriver.Chrome(executable_path="D:\\Devdatta\\Projects\\Python\\SeleniumPython_Practice\\resources"
                                           "\\browsers\\chromedriver.exe", options= chromeOptions)
driver.get("https://rahulshettyacademy.com/angularpractice")
print(driver.title)

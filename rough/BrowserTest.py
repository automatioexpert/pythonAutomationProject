from selenium import webdriver
#driver=webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
print(driver.title)
driver.quit()
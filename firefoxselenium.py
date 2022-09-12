from selenium import webdriver

driver =webdriver.Firefox(executable_path= 'D:\Python\geckodriver.exe')

driver.get("http://learn-automation.com")
print(driver.title)
print(driver.current_url)
driver.quit()
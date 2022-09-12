from selenium import webdriver
from selenium.webdriver.chrome.service import Service



driver = webdriver.Chrome()
driver.get("http://www.google.com")
mypagetitle= driver.title
print(mypagetitle)
print(driver.quit)
assert "Google" in mypagetitle
driver.quit()



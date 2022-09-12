from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("D:\\Python\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://accounts.google.com/ServiceLogin/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.implicitly_wait(3)

loginBox = driver.find_element(By.NAME,"identifier")
loginBox.send_keys('abhitestcode@gmail.com')

nextButton = driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/span")
print(nextButton)
nextButton.click()
driver.implicitly_wait(3)
passWordBox = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys("Abhishek123$")

nextButton = driver.find_element(By.XPATH,"//*[@id='passwordNext']/div/button/span")
nextButton.click()

print('Login Successful...!!')

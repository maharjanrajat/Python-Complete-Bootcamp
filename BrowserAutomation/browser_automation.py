from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()

browser.get('https://the-internet.herokuapp.com/login')

username = browser.find_element(By.ID, 'username')
username.send_keys("tomsmith")

password = browser.find_element(By.ID, 'password')
password.send_keys("SuperSecretPassword!")
password.send_keys(Keys.RETURN)

# button = browser.find_element(By.TAG_NAME, 'button')
# button.click()

time.sleep(5)

message_element = browser.find_element(By.CLASS_NAME, 'subheader')
print(message_element.text)

browser.close()


# https://www.sharesansar.com/existing-issues -----------> web scraping

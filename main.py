from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, time 

driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
executor_url = driver.command_executor._url
session_id = driver.session_id

print("url: " + executor_url)
print("id: " + session_id)

driver.get('https://web.whatsapp.com/')
time.sleep(10)
contact = "Azuuu"
message = "Hola Azu, soy un bot"
search_box = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
search_box.send_keys(contact)
search_box.send_keys(Keys.ENTER)
time.sleep(5) 
message_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[1]/div/div[2]")
message_box.send_keys(message)
message_box.send_keys(Keys.ENTER)
time.sleep(10)
driver.close()
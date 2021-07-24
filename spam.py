from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os, time 

def browser_driver():
    # Opciones de navegación
    options =  webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_experimental_option('excludeSwitches',['enable-automation'])

    driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')

    #Variables para inicio de sesión 
    executor_url = driver.command_executor._url
    session_id = driver.session_id

    print("url: " + executor_url)
    print("id: " + session_id)

    #Inicio del navegador
    driver.get('https://web.whatsapp.com/')

    return driver


def spam_bot(contact, message, amount):
    driver = browser_driver()
    message_count = 0
    WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "//*[@id='side']/div[1]/div/label/div/div[2]")))\
    .send_keys(contact + Keys.ENTER)
    
    while message_count < amount :
        WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                        "//*[@id='main']/footer/div[1]/div[2]/div/div[1]/div/div[2]")))\
        .send_keys(message + Keys.ENTER)
        
        time.sleep(1)
        message_count += 1


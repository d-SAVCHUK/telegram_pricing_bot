from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

print('please, print Article of product')
article = input()

s = Service("drivers/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get('https://www.massimodutti.com/es/en')
time.sleep(3)

search = driver.find_element(By.XPATH, '//*[@id="ItxHomePage"]/body/app-root/app-layout/div[1]/header-comfy-container/header-comfy-sidebar/div/div/div[3]/ul/li[1]/a')
search.click()
search.click()

search_bar = driver.find_element(By.XPATH, '//*[@id="empathy-x"]/header/div/div/input')
search_bar.send_keys(article)
time.sleep(2)

element = driver.find_element(By.CLASS_NAME, 'ebx-result-price__value')
print(element.text)

driver.get('https://www.massimodutti.com/ua/en')
time.sleep(3)

search2 = driver.find_element(By.XPATH, '//*[@id="ItxHomePage"]/body/app-root/app-layout/div[1]/header-comfy-container/header-comfy-sidebar/div/div/div[3]/ul/li[1]/a')
search2.click()
search2.click()

search_bar2 = driver.find_element(By.XPATH, '//*[@id="empathy-x"]/header/div/div/input')
search_bar2.send_keys(article)
time.sleep(2)

element2 = driver.find_element(By.CLASS_NAME, 'ebx-result-price__value')
print(element2.text)


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "./drivers/geckodriver.exe"
url = "https://qamindslab.com/"

service = Service(chrome_driver_path)
driver = webdriver.Firefox(service=service)

driver.get(url)
driver.find_element(By.XPATH,"")
time.sleep(1)
driver.quit()






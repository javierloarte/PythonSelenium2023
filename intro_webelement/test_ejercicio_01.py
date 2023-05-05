import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "./drivers/geckodriver.exe"
firefox_service = Service(chrome_driver_path)
url = "https://laboratorio.qaminds.com/"


class Ejercicio_01:

    def __init__(self):
        self.driver = None

    def open_web(self):
        self.driver = webdriver.Firefox(service=firefox_service)
        self.driver.maximize_window()
        self.driver.get(url)


    def close_web(self):
        self.driver.quit()
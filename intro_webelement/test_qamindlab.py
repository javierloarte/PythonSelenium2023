import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "./drivers/geckodriver.exe"
chrome_service = Service(chrome_driver_path)
url = "https://qamindslab.com/"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Firefox(service=chrome_service)
        self.driver.maximize_window()
        self.driver.get(url)


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"


class test_busqueda_iphone:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_search_iphone(self):
        time.sleep(3)
        element = self.driver.find_element(By.XPATH, "//a[normalize-space()='LABORATORIO']")
        assert element.is_displayed(),"Elemento de tiene que ser visisble"



import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "./drivers/geckodriver.exe"
service = Service(chrome_driver_path)
URL = "https://laboratorio.qaminds.com/"


class test_busquedaiphone:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_search_iphone(self):
        time.sleep(3)
        element = self.driver.find_element(By.XPATH, "//a[normalize-space()='LABORATORIO']")
        assert element.is_displayed(),"Elemento de tiene que ser visisble"


    def teardown_method(self):
        self.driver.quit()
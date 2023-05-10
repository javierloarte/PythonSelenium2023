import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = "./drivers/geckodriver.exe"
firefox_service = Service(chrome_driver_path)
url = "https://laboratorio.qaminds.com/"


class TestEjercicio04:

    def setup_method(self):
        self.driver = webdriver.Firefox(service=firefox_service)
        self.driver.maximize_window()
        self.driver.get(url)

    def test_buscaLaptop(self):
        # Opcion Laptops
        time.sleep(3)
        menu_lista = self.driver.find_element(By.XPATH, "//a[normalize-space()='Laptops & Notebooks']")
        menu_lista.click()
        element = self.driver.find_element(By.XPATH, "//a[normalize-space()='Windows (0)']")
        time.sleep(1)
        element.click()




    def teardown_method(self):
        self.driver.quit()
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = "./drivers/geckodriver.exe"
firefox_service = Service(chrome_driver_path)
url = "https://laboratorio.qaminds.com/"



class TestEjercicio05:

    def setup_method(self):
        self.driver = webdriver.Firefox(service=firefox_service)
        self.driver.maximize_window()
        self.driver.get(url)

    def test_validaNombre(self):

        # Validar Macbook
        time.sleep(1)
        elemente01 = self.driver.find_element(By.XPATH, "//a[normalize-space()='MacBook']")
        assert "MacBook" in elemente01.text

        # Validar Iphone
        time.sleep(1)
        elemente02 = self.driver.find_element(By.XPATH, "//a[normalize-space()='iPhone']")
        assert "iPhone" in elemente02.text


        # Validar Canon
        time.sleep(1)
        elemente04 = self.driver.find_element(By.XPATH, "//a[normalize-space()='Canon EOS 5D']")
        assert "Canon" in elemente04.text



    def teardown_method(self):
        self.driver.quit()
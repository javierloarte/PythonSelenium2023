import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = "./drivers/geckodriver.exe"
firefox_service = Service(chrome_driver_path)
url = "https://laboratorio.qaminds.com/"



class TestEjercicio04:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=firefox_service)
        self.driver.maximize_window()
        self.driver.get(url)

    def test_buscaLaptop(self):
        # Opcion Laptops / Windows
        time.sleep(3)
        menu_lista = self.driver.find_element(By.XPATH, "//a[normalize-space()='Laptops & Notebooks']")
        menu_lista.click()
        element = self.driver.find_element(By.XPATH, "//a[normalize-space()='Windows (0)']")
        time.sleep(1)
        element.click()

        # Opcion No hay products
        time.sleep(3)
        elementText = self.driver.find_element(By.XPATH, "//*[@id='content']")
        assert "no products" in elementText.text
        print("Validacion Correcta  no items")

        # Opcion Continuar
        time.sleep(1)
        elementContinua = self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary']")
        elementContinua.click()

        # Ventana Home
        time.sleep(1)
        elementUrl = self.driver.current_url
        print(elementUrl)
        assert "route=common/home" in elementUrl
        print("Validacion Correcta de URL")



    def teardown_method(self):
        self.driver.quit()
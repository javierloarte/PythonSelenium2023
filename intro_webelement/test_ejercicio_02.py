import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = "./drivers/geckodriver.exe"
firefox_service = Service(chrome_driver_path)
url = "https://laboratorio.qaminds.com/"


class TestEjercicio02:

    def setup_method(self):
        self.driver = webdriver.Firefox(service=firefox_service)
        self.driver.maximize_window()
        self.driver.get(url)

    def test_buscarTablet(self):

        # Opcion tablet
        time.sleep(3)
        element = self.driver.find_element(By.XPATH, "//a[normalize-space()='Tablets']")
        assert element.is_displayed(),"No se encuentra la opcion"
        element.click()

        # Seleccionar tablet
        time.sleep(3)
        elementTablet = self.driver.find_element(By.XPATH, "//a[normalize-space()='Samsung Galaxy Tab 10.1']")
        assert elementTablet.is_displayed(), "No existe opcion"
        elementTablet.click()

        # Validar costo de item
        time.sleep(3)
        itemPrecio = self.driver.find_element(By.XPATH,"//h2[normalize-space()='$241.99']")
        assert itemPrecio.is_displayed(), "El precio no coincide"
        print("Validacion Correcta")

        # Validar costo de item
        time.sleep(3)
        elementAdd = self.driver.find_element(By.XPATH, "//button[@id='button-cart']")
        elementAdd.click()
        elementSucces = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
        assert elementSucces.is_displayed(), "No se agrego item"
        print("Success")

        # Validar conteo
        itemConteo = self.driver.find_element(By.XPATH, "//span[@id='cart-total']")
        assert itemConteo.text != " 1 item(s) - $241.99"
        print("Se agrego item")


    def teardown_method(self):
        self.driver.quit()
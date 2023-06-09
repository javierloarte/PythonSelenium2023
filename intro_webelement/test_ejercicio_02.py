import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = "./drivers/geckodriver.exe"
firefox_service = Service(chrome_driver_path)
url = "https://laboratorio.qaminds.com/"

class TestEjercicio02:

    def setup_method(self):
        self.driver = webdriver.Firefox(service=firefox_service)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(url)

    def test_buscarTablet(self):

        # Opcion tablet
       # time.sleep(3)
        element = self.driver.find_element(By.XPATH, "//a[normalize-space()='Tablets']")
        assert element.is_displayed(),"No se encuentra la opcion"
        element.click()

        # Validar item tablet
        time.sleep(3)
        elementTablet = self.driver.find_element(By.XPATH, "//a[normalize-space()='Samsung Galaxy Tab 10.1']")
        assert elementTablet.is_displayed(), "No existe producto"
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
        assert "Success" in elementSucces.text
        print("Success")

        # Agregar a wishlist
        time.sleep(3)
        elementwish = self.driver.find_element(By.XPATH, "//button[@type='button']//i[@class='fa fa-heart']")
        elementwish.click()

        # Validar conteo
        time.sleep(3)
        itemConteo = self.driver.find_element(By.XPATH, "//span[@id='cart-total']")
        assert itemConteo.text != " 1 item(s) - $241.99"
        print("Se agrego item")


    def teardown_method(self):
        self.driver.quit()
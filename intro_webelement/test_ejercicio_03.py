import time
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = "./drivers/geckodriver.exe"
firefox_service = Service(chrome_driver_path)
url = "https://laboratorio.qaminds.com/index.php?route=account/login"


class TestEjercicio03:

    def setup_method(self):
        self.driver = webdriver.Firefox(service=firefox_service)
        self.driver.maximize_window()
        self.driver.get(url)


    def test_validacionLogin(self):
        # ingresar correo
        time.sleep(3)
        elementCorreo = self.driver.find_element(By.XPATH, "//input[@id='input-email']")
        elementCorreo.send_keys("123@gmail.com")

        # ingresar password
        time.sleep(1)
        elementClave = self.driver.find_element(By.XPATH, "//input[@id='input-password']")
        elementClave.send_keys("654321")

        # Seleccionar boton
        time.sleep(3)
        elementBoton = self.driver.find_element(By.XPATH, "//input[@value='Login']")
        elementBoton.click()

        # Validar mensaje
        time.sleep(3)
        elementWarning = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
        ##assert elementWarning.text == "Warning: No match for E-Mail Address and/or Password."
        assert "Warning" in elementWarning.text
        print("Mensaje Alerta correcto")



    def teardown_method(self):
        self.driver.quit()
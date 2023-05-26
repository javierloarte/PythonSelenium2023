from selenium.webdriver.common.by import By

from factory.webdriver_factory import get_driver

url = "https://laboratorio.qaminds.com/"


class TestPractico03:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(url)

    def test_search_laptop(self):
        # buscar Laptop
        elementcurrency = self.driver.find_element(By.XPATH, "//strong[normalize-space()='$']")
        assert "$" in elementcurrency.text
        search_input = self.driver.find_element(By.NAME, "search")
        assert search_input.is_displayed() and search_input.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        search_input.send_keys("Samsung")
        btnBuscar = self.driver.find_element(By.XPATH, "//i[@class='fa fa-search']")
        btnBuscar.click()
        elementSamsung = self.driver.find_element(By.XPATH, "//a[normalize-space()='Samsung SyncMaster 941BW']")
        elementSamsung.click()
        primerValor = self.driver.find_element(By.XPATH, "//h2[normalize-space()='$242.00']")

        elementDolar = self.driver.find_element(By.XPATH, "//button[@class='btn btn-link dropdown-toggle']")
        elementDolar.click()
        elementEuro = self.driver.find_element(By.XPATH, "//button[@name='EUR']")
        elementEuro.click()
        segundoValor = self.driver.find_element(By.XPATH,"//h2[contains(text(),'189.87€')]")
        assert primerValor != segundoValor



       # assert "1 item(s) - $122.00" in carrito.text


    def teardown_method(self):
        self.driver.quit()

from selenium.webdriver.common.by import By

from factory.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://laboratorio.qaminds.com/"

class TestPruebaUno:

    def setup_method(self):
        self.driver = get_driver()
        self.wait_driver = WebDriverWait(self.driver, 15)
        self.driver.get(URL)

    def test_search_display(self):
        # Escribir Display
        search_search = self.driver.find_element(By.NAME, "search")
        assert search_search.is_displayed() and search_search.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        search_search.send_keys("Display")

        # Seleccionar Buscar
        btnBuscar = self.driver.find_element(By.XPATH, "//i[@class='fa fa-search']")
        btnBuscar.click()

        # NO ObtenerResultado
     #   self.__find_visible_element(By.XPATH, "//p[contains(text(),'There is no product that matches the search criter')]")

        # Search in produc description
        checkOpcion = self.driver.find_element(By.XPATH, "//input[@id='description']")
        checkOpcion.is_selected()
        btnSearch = self.driver.find_element(By.XPATH, "//input[@id='button-search']")
        btnSearch.click()
    #    esperar = self.__find_visible_element(By.XPATH, "///img[@title='MacBook Pro']")




    def __find_visible_element(self, by: By, value: str):
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))


    def teardown_method(self):
        self.driver.quit()
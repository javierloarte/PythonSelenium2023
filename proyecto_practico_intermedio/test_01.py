from selenium.webdriver.common.by import By

from factory.webdriver_factory import get_driver

URL = "https://laboratorio.qaminds.com/"


class TestPractico:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)

    def test_search_display(self):
        # Escribir Iphone
        search_input = self.driver.find_element(By.NAME, "search")
        assert search_input.is_displayed() and search_input.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        search_input.send_keys("Display")
        btnBuscar = self.driver.find_element(By.XPATH, "//i[@class='fa fa-search']")
        btnBuscar.click()
        checkOpcion = self.driver.find_element(By.CSS_SELECTOR, "#description")
        checkOpcion.is_selected()
        search_dos = self.driver.find_element(By.XPATH, "//input[@id='button-search']")
        search_dos.click()

    def teardown_method(self):
        self.driver.quit()

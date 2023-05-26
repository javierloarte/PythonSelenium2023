from selenium.webdriver.common.by import By

from factory.webdriver_factory import get_driver

url = "https://laboratorio.qaminds.com/"


class TestPractico:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(url)

    def test_search_display(self):
        # Escribir Iphone
        search_input = self.driver.find_element(By.NAME, "search")
        assert search_input.is_displayed() and search_input.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        search_input.send_keys("Display")
        btnBuscar = self.driver.find_element(By.XPATH, "//i[@class='fa fa-search']")
        btnBuscar.click()
        element = self.driver.find_element(By.ID, "description")
        element.is_selected()
        element.click()
        search_dos = self.driver.find_element(By.ID, "button-search")
        search_dos.click()
        items = self.driver.find_element(By.XPATH, "//div[@class='col-sm-6 text-right']")
        assert "4" in items.text



    def teardown_method(self):
        self.driver.quit()

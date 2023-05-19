from selenium.webdriver.common.by import By

from factory.webdriver_factory import get_driver

url = "https://laboratorio.qaminds.com/"

class Practica01:


    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(url)

    def test_search_display(self):
        # Escribir Display
        search_display = self.driver.find_element(By.NAME, "search")
        assert search_display.is_displayed() and search_display.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        search_display.send_keys("Display")



    def teardown_method(self):
        self.driver.quit()
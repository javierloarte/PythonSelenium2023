from selenium.webdriver.common.by import By

from factory.webdriver_factory import get_driver

url = "https://laboratorio.qaminds.com/"


class TestPractico03:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(url)

    def test_search_laptop(self):
        # buscar Laptop
        elementmenu = self.driver.find_element(By.XPATH, "//a[normalize-space()='Desktops']")
        elementmenu.click()
        elementmac = self.driver.find_element(By.XPATH, "//a[normalize-space()='Mac (1)']")
        elementmac.click()
        item_imac = self.driver.find_element(By.XPATH, "//a[normalize-space()='iMac']")
        assert "iMac" in item_imac.text
        item_imac.click()
        btnagregar = self.driver.find_element(By.XPATH, "//button[@id='button-cart']")
        btnagregar.click()
        flayersuccess = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
        assert flayersuccess.is_displayed() and flayersuccess.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        assert "Success" in flayersuccess.text
        carrito = self.driver.find_element(By.XPATH, "//span[@id='cart-total']")
        assert "1 item(s) - $122.00" in carrito.text


    def teardown_method(self):
        self.driver.quit()

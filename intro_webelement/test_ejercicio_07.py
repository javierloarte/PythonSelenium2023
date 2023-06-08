import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_driver_path = "./drivers/geckodriver.exe"
firefox_service = Service(chrome_driver_path)
url = "https://demoqa.com/select-menu"


class TestEjercicio04:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=firefox_service)
        self.driver.maximize_window()
        self.driver.get(url)

    def test_Standard_multi_select(self):
        # Opcion Laptops / Windows
        time.sleep(2)
        elementlista = self.driver.find_element(By.ID, "cars")
        select = Select(elementlista)
        time.sleep(1)
        select.select_by_visible_text("Volvo")
        time.sleep(1)
        select.select_by_visible_text("Audi")
        assert select.first_selected_option.text == "Volvo", "Validacion Erronea"





    def teardown_method(self):
        self.driver.quit()
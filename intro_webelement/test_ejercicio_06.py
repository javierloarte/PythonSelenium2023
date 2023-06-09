import time
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


chrome_driver_path = "./drivers/geckodriver.exe"
firefox_service = Service(chrome_driver_path)
url = "https://demoqa.com/select-menu"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Firefox(service=firefox_service)
        self.driver.maximize_window()
        self.driver.get(url)

    def test_old_style_select(self):
        time.sleep(2)
        element = self.driver.find_element(By.ID, "oldSelectMenu")
        select = Select(element)
        select.select_by_visible_text("Green")
        select.select_by_value("4")
        assert select.first_selected_option.text == "Purple"
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()
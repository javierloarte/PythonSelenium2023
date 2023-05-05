import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "./drivers/geckodriver.exe"
firefox_service = Service(chrome_driver_path)
url = "https://laboratorio.qaminds.com/"


class TestEjercicio01:

    def open_web(self):
        self.driver = webdriver.Firefox(service=firefox_service)
        self.driver.maximize_window()
        self.driver.get(url)

    def test_course_button(self):
        time.sleep(3)
        element = self.driver.find_element(By.XPATH, "//a[normalize-space()='LABORATORIO']")
        assert element.is_displayed(),"Elemento de tiene que ser visisble"


    def close_web(self):
        self.driver.quit()
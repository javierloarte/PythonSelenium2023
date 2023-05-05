import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "./drivers/geckodriver.exe"
firefox_service = Service(chrome_driver_path)
url = "https://laboratorio.qaminds.com/"


class TestEjercicio01:

    def setup_method(self):
        self.driver = webdriver.Firefox(service=firefox_service)
        self.driver.maximize_window()
        self.driver.get(url)

    def test_course_button(self):
        time.sleep(3)
        element = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        assert element.is_displayed(),"Elemento de tiene que ser visisble"
        element.send_keys("iphone")
        elementbtn = self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
        elementbtn.click()


    def teardown_method(self):
        self.driver.quit()
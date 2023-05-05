import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "./drivers/geckodriver.exe"
firefox_service = Service(chrome_driver_path)
url = "https://laboratorio.qaminds.com/"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Firefox(service=firefox_service)
        self.driver.maximize_window()
        self.driver.get(url)

    def test_course_button(self):
        time.sleep(3)
        element = self.driver.find_element(By.XPATH, "//a[normalize-space()='LABORATORIO']")
        assert element.is_displayed(),"Elemento de tiene que ser visisble"



    def teardown_method(self):
        self.driver.quit()
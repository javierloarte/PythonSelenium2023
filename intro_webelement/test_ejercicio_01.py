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
        self.driver.implicitly_wait(10)
        self.driver.get(url)

    def test_course_button(self):
        time.sleep(3)
        element = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        assert element.is_displayed(),"Elemento de tiene que ser visisble"
        element.send_keys("iphone")
        elementbtn = self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
        elementbtn.click()

        # Validate course page
        time.sleep(3)
        # assert self.driver.current_url == "https://qamindslab.com/courses", "URL tiene que ser la de cursos"
        elementIphone = self.driver.find_element(By.XPATH,"//img[@title='iPhone']")
        assert elementIphone.is_displayed(), "La imagen si existe"
        print("Validacion Correcta")

    def teardown_method(self):
        self.driver.quit()
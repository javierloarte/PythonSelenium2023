from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



chrome_driver_path = "./drivers/geckodriver.exe"
firefox_service = Service(chrome_driver_path)
url = "https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html"


class TestEjercicio08:

    def setup_method(self):
        self.driver = webdriver.Firefox(service=firefox_service)
        self.driver.implicitly_wait(2)
        self.wait_driver = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()
        self.driver.get(url)

    def test_Downland(self):
        button = self.__find_clickable_element(By.XPATH, "//button[@id='downloadButton']")

    def __find_clickable_element(self, by: By, value: str):
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def teardown_method(self):
        self.driver.quit()
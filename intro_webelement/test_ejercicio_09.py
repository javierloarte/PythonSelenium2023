from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



chrome_driver_path = "./drivers/geckodriver.exe"
firefox_service = Service(chrome_driver_path)
url = "https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html"


class TestEjercicio09:

    def setup_method(self):
        self.driver = webdriver.Firefox(service=firefox_service)
        self.driver.implicitly_wait(2)
        self.wait_driver = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()
        self.driver.get(url)

    def test_Descarga(self):
        button = self.__find_clickable_element(By.XPATH, "//button[@id='downloadButton']")
        button.click()
        label = self.__find_by_text(By.XPATH, "//div[@class='progress-label']", "Complete!")
        print(label)
        element = self.driver.find_element(By.XPATH, "//div[@class='progress-label']")
        assert "Complete" in element.text
        self.__find_clickable_element(By.XPATH, "//button[normalize-space()='Close']")


    def __find_clickable_element(self, by: By, value: str):
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_by_text(self, by: By, value: str, text: str):
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))



    def teardown_method(self):
        self.driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "./drivers/geckodriver.exe"
firefox_service = Service(chrome_driver_path)
url = "https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html"



class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=firefox_service)
        self.driver.implicitly_wait(1)
        self.wait_driver = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()
        self.driver.get(url)

    def test_slow_loading_page(self):
        # Obtener el elemento, y el estado importa
        dialogo = self.__find_clickable_element(By.ID, "autoclosable-btn-success")
        dialogo.click()
        self.__find_visible_element(By.XPATH, "//*[@class='alert alert-success alert-autocloseable-success']")
        self.__wait_until_disappears(By.XPATH, "//*[@class='alert alert-success alert-autocloseable-success']")

    def __find_clickable_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_visible_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    def __find_by_text(self, by: By, value: str, text: str) -> WebElement:
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))

    def __wait_until_disappears(self, by: By, value: str) -> WebElement:
        self.wait_driver.until(EC.invisibility_of_element((by, value)))

    def teardown_method(self):
        self.driver.quit()
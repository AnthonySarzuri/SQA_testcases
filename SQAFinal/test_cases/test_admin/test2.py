import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        chrome_service = Service(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.driver.get('http://localhost:3000')
        yield
        self.driver.quit()
        print("Prueba finalizada correctamente.")

    def login(self, email, password):
        self.driver.find_element(By.XPATH, "//div[@class='relative']//input[@type='email']").send_keys(email)
        self.driver.find_element(By.XPATH, "//div[@class='relative']//input[@type='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

    def check_login_success(self):
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, "//h2[contains(text(), 'Bienvenido')]")
            self.driver.get('http://localhost:3000/welcome')
            return "Login exitoso"
        except Exception:
            return "Login fallido"

    def test_login(self):
        self.login("liliana@gmail.com", "lilianaC")
        actual = self.check_login_success()
        esperado = "Login exitoso"
        assert actual == esperado, f"FALLÓ: Se esperaba '{esperado}', pero se obtuvo '{actual}'"

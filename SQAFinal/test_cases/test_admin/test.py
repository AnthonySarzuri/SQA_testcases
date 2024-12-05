import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestLoginError:
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

    def check_credentials_error(self, expected_message):
        time.sleep(2)
        try:
            actual_message_element = self.driver.find_element(By.XPATH, "//p[text()='Credenciales no válidas']")
            actual_message = actual_message_element.text
        except Exception:
            actual_message = "No se encontró el mensaje de error"
        return actual_message

    def test_login_error(self):
        self.login("liliana@gmail.com", "lilianac")
        actual_message = self.check_credentials_error("Credenciales no válidas")
        esperado = "Credenciales no válidas"
        if actual_message == esperado:
            print(f"Resultado: {actual_message}")
        else:
            print(f"FALLÓ: No se recibió el mensaje esperado. Obtenido: '{actual_message}'")
        assert actual_message == esperado, f"FALLÓ: Se esperaba '{esperado}', pero se obtuvo '{actual_message}'"

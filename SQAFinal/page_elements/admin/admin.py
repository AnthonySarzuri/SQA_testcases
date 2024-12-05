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
        yield
        self.driver.quit()
        print("Prueba finalizada correctamente.")

    def test_login_exitoso(self):
        self.driver.get('http://localhost:3000')
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//div[@class='relative']//input[@type='email']").send_keys("liliana@gmail.com")
        self.driver.find_element(By.XPATH, "//div[@class='relative']//input[@type='password']").send_keys("lilianaC")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

        try:
            welcome_element = self.driver.find_element(By.XPATH, "//h2[contains(text(), 'Bienvenido')]")
            actual = "Login exitoso" if welcome_element else "Login fallido"
        except Exception:
            actual = "Login fallido"

        esperado = "Login exitoso"
        print(f"Resultado obtenido: {actual}")
        assert actual == esperado, f"FALLÓ: Se esperaba '{esperado}', pero se obtuvo '{actual}'"

    def test_login_fallido(self):
        self.driver.get('http://localhost:3000')
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//div[@class='relative']//input[@type='email']").send_keys("usuario_incorrecto@gmail.com")
        self.driver.find_element(By.XPATH, "//div[@class='relative']//input[@type='password']").send_keys("clave_incorrecta")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

        try:
            error_message = self.driver.find_element(By.XPATH, "//p[contains(text(), 'Credenciales incorrectas')]")
            actual = "Login fallido" if error_message else "Login exitoso"
        except Exception:
            actual = "Login fallido"

        esperado = "Login fallido"
        print(f"Resultado obtenido: {actual}")
        assert actual == esperado, f"FALLÓ: Se esperaba '{esperado}', pero se obtuvo '{actual}'"

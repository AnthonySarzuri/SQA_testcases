import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestLoginValidation:
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

    def validate_locators(self):
        locators = [
            "//a[@href='/pacientes']",
            "//a[@href='/terapeutas']",
            "//a[@href='/internos']"
        ]
        missing_locators = []
        for locator in locators:
            try:
                self.driver.find_element(By.XPATH, locator)
                print(f"Elemento con locator '{locator}' está presente en la página.")
            except Exception:
                missing_locators.append(locator)

        if missing_locators:
            return f"No se encontraron los siguientes locators: {', '.join(missing_locators)}. El usuario no es un administrador."
        return "Todos los locators están presentes."

    def test_validate_login_and_locators(self):
        self.login("can@gmail.com", "72005945CA")
        actual_login = self.check_login_success()
        assert actual_login == "Login exitoso", f"FALLÓ: Se esperaba 'Login exitoso', pero se obtuvo '{actual_login}'"

        locators_result = self.validate_locators()
        expected_message = "Todos los locators están presentes."
        assert locators_result == expected_message, f"FALLÓ: Se esperaba '{expected_message}', pero se obtuvo '{locators_result}'"

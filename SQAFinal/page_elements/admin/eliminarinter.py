import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestEliminarInterno:
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
        try:
            welcome_element = self.driver.find_element(By.XPATH, "//h2[contains(text(), 'Bienvenido')]")
            return "Login exitoso" if welcome_element else "Login fallido"
        except Exception:
            return "Login fallido"

    def navigate_to_internos(self):
        self.driver.find_element(By.XPATH, "//a[@href='/internos']").click()
        print("Navegando a la página de Internos...")
        time.sleep(2)

    def delete_interno(self):
        try:
            delete_button = self.driver.find_element(By.XPATH, "(//button[@class='bg-red-600 text-white px-2 py-1 rounded hover:bg-red-700 flex items-center'])[2]")
            delete_button.click()
            print("Botón de eliminar clickeado. Esperando alerta...")

            alert = self.driver.switch_to.alert
            alert.accept()
            print("Alerta aceptada. Interno eliminado exitosamente.")
            return "Interno eliminado correctamente"
        except Exception as e:
            print(f"Error al eliminar el interno: {e}")
            return "Error al eliminar el interno"

    def test_eliminar_interno(self):
        # Login
        self.login("liliana@gmail.com", "lilianaC")
        actual_login = self.check_login_success()
        assert actual_login == "Login exitoso", f"FALLÓ: Se esperaba 'Login exitoso', pero se obtuvo '{actual_login}'"

        self.navigate_to_internos()

        resultado_eliminacion = self.delete_interno()
        esperado = "Interno eliminado correctamente"
        assert resultado_eliminacion == esperado, f"FALLÓ: Se esperaba '{esperado}', pero se obtuvo '{resultado_eliminacion}'"

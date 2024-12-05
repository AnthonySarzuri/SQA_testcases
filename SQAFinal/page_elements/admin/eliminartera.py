import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestEliminarTerapeuta:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        chrome_service = Service(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.driver.get('http://localhost:3000')
        yield
        self.driver.quit()
        print("Prueba completada correctamente.")

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

    def navigate_to_terapeutas(self):
        self.driver.find_element(By.XPATH, "//a[@href='/terapeutas']").click()
        time.sleep(2)

    def delete_terapeuta(self):
        try:
            delete_button = self.driver.find_element(By.XPATH, "(//button[@class='bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600 flex items-center'])[2]")
            delete_button.click()
            print("Se hizo clic en el botón de eliminar.")

            alert = self.driver.switch_to.alert
            alert.accept()
            print("Se aceptó la alerta de confirmación.")
            return "Terapeuta eliminado correctamente"
        except Exception as e:
            print(f"Error al eliminar el terapeuta: {e}")
            return "Error al eliminar el terapeuta"

    def test_eliminar_terapeuta(self):

        self.login("liliana@gmail.com", "lilianaC")
        actual_login = self.check_login_success()
        assert actual_login == "Login exitoso", f"FALLÓ: Se esperaba 'Login exitoso', pero se obtuvo '{actual_login}'"

        self.navigate_to_terapeutas()

        resultado_eliminacion = self.delete_terapeuta()
        esperado = "Terapeuta eliminado correctamente"
        assert resultado_eliminacion == esperado, f"FALLÓ: Se esperaba '{esperado}', pero se obtuvo '{resultado_eliminacion}'"

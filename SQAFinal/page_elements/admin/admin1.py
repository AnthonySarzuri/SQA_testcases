import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestPacientes:
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

    def test_login_exitoso(self):
        self.login("liliana@gmail.com", "lilianaC")
        actual = self.check_login_success()
        esperado = "Login exitoso"
        print(f"Resultado obtenido: {actual}")
        assert actual == esperado, f"FALLÓ: Se esperaba '{esperado}', pero se obtuvo '{actual}'"

    def test_navegar_a_pacientes(self):
        self.login("liliana@gmail.com", "lilianaC")
        actual = self.check_login_success()
        assert actual == "Login exitoso", "No se pudo realizar el login exitosamente."

        self.driver.find_element(By.XPATH, "//a[@href='/pacientes']").click()
        time.sleep(2)
        actual_url = self.driver.current_url
        esperado_url = "http://localhost:3000/pacientes"
        print(f"Resultado obtenido: {actual_url}")
        assert actual_url == esperado_url, f"FALLÓ: Se esperaba '{esperado_url}', pero se obtuvo '{actual_url}'"

    def test_ver_historial_paciente(self):
        self.login("liliana@gmail.com", "lilianaC")
        actual = self.check_login_success()
        assert actual == "Login exitoso", "No se pudo realizar el login exitosamente."

        self.driver.find_element(By.XPATH, "//a[@href='/pacientes']").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "(//button[@class='bg-green-500 text-white px-3 py-1 rounded hover:bg-green-600 flex items-center'])[1]").click()
        time.sleep(2)
        actual_url = self.driver.current_url
        esperado_url = "http://localhost:3000/historial"
        print(f"Resultado obtenido: {actual_url}")
        assert actual_url == esperado_url, f"FALLÓ: Se esperaba '{esperado_url}', pero se obtuvo '{actual_url}'"

    def test_verificar_textos(self):
        self.login("liliana@gmail.com", "lilianaC")
        actual = self.check_login_success()
        assert actual == "Login exitoso", "No se pudo realizar el login exitosamente."

        xpath_correcto = "//input[contains(@id, 'Recupera')]"
        texto_correcto = "¿Has olvidado tu USUARIO?"
        actual_texto_correcto = self.driver.find_element(By.XPATH, xpath_correcto).get_attribute("value")
        print(f"Texto obtenido: {actual_texto_correcto}")
        assert actual_texto_correcto == texto_correcto, f"FALLÓ: Se esperaba '{texto_correcto}', pero se obtuvo '{actual_texto_correcto}'"

        texto_incorrecto = "¿Has olvidado tu USUARIO"
        actual_texto_incorrecto = self.driver.find_element(By.XPATH, xpath_correcto).get_attribute("value")
        print(f"Texto obtenido: {actual_texto_incorrecto}")
        assert actual_texto_incorrecto != texto_incorrecto, f"FALLÓ: No se esperaba '{texto_incorrecto}', pero se obtuvo '{actual_texto_incorrecto}'"

    def test_regresar_a_home(self):
        self.login("liliana@gmail.com", "lilianaC")
        actual = self.check_login_success()
        assert actual == "Login exitoso", "No se pudo realizar el login exitosamente."

        self.driver.find_element(By.XPATH, "//a[@href='/pacientes']").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//button[@class='bg-yellow-600 text-white px-4 py-2 rounded hover:bg-yellow-700 flex items-center']").click()
        time.sleep(2)
        actual_url = self.driver.current_url
        esperado_url = "http://localhost:3000/welcome"
        print(f"Resultado obtenido: {actual_url}")
        assert actual_url == esperado_url, f"FALLÓ: Se esperaba '{esperado_url}', pero se obtuvo '{actual_url}'"

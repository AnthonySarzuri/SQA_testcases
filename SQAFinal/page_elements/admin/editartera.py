import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestEditarTerapeuta:
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

    def navigate_to_terapeutas(self):
        self.driver.find_element(By.XPATH, "//a[@href='/terapeutas']").click()
        print("Navegando a la página de Terapeutas...")
        time.sleep(2)

    def edit_terapeuta(self, nuevo_nombre):
        try:
            self.driver.find_element(By.XPATH, "//button[@class = 'bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600 flex items-center']").click()
            print("Entrando a la página de edición de terapeuta...")
            time.sleep(2)

            nombre_input = self.driver.find_element(By.XPATH, "//input[@name='nombre']")
            nombre_input.clear()
            nombre_input.send_keys(nuevo_nombre)
            print(f"Nuevo nombre ingresado: {nuevo_nombre}")

            self.driver.find_element(By.XPATH, "//button[@class = 'w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700 flex items-center justify-center']").click()
            print("Guardando los cambios...")
            time.sleep(2)

            return "Cambios guardados correctamente"
        except Exception as e:
            print(f"Error al editar el terapeuta: {e}")
            return "Error al editar el terapeuta"

    def return_to_home(self):
        self.driver.find_element(By.XPATH, "//button[@class='bg-yellow-600 text-white px-4 py-2 rounded hover:bg-yellow-700 flex items-center']").click()
        print("Regresando a la página principal...")
        time.sleep(2)

    def test_editar_terapeuta(self):
        # Login
        self.login("liliana@gmail.com", "lilianaC")
        actual_login = self.check_login_success()
        assert actual_login == "Login exitoso", f"FALLÓ: Se esperaba 'Login exitoso', pero se obtuvo '{actual_login}'"

        self.navigate_to_terapeutas()

        nuevo_nombre = "Steven Modificado"
        resultado_edicion = self.edit_terapeuta(nuevo_nombre)
        esperado = "Cambios guardados correctamente"
        assert resultado_edicion == esperado, f"FALLÓ: Se esperaba '{esperado}', pero se obtuvo '{resultado_edicion}'"

        self.return_to_home()

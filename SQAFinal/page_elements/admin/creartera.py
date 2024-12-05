import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestTerapeutas:
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

    def navigate_create_terapeuta(self):
        self.driver.find_element(By.XPATH, "//a[@href='/terapeutas/nuevo']").click()
        print("Navegando a la página de creación de un nuevo terapeuta...")
        time.sleep(2)

    def create_terapeuta(self, datos_terapeuta):
        try:
            self.driver.find_element(By.XPATH, "//input[@name='nombre']").send_keys(datos_terapeuta['nombre'])
            self.driver.find_element(By.XPATH, "//input[@name='apellido']").send_keys(datos_terapeuta['apellido'])
            self.driver.find_element(By.XPATH, "//input[@name='telefono']").send_keys(datos_terapeuta['telefono'])
            self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(datos_terapeuta['email'])
            self.driver.find_element(By.XPATH, "//input[@name='especialidad']").send_keys(datos_terapeuta['especialidad'])
            self.driver.find_element(By.XPATH, "//input[@name='licencia_medica']").send_keys(datos_terapeuta['licencia_medica'])
            self.driver.find_element(By.XPATH, "//input[@name='fecha_nacimiento']").send_keys(datos_terapeuta['fecha_nacimiento'])

            self.driver.find_element(By.XPATH, "//button[@onclick='generarContraseña()']").click()
            time.sleep(1)

            password_generated = self.driver.find_element(By.XPATH, "//input[@name='password']").get_attribute("value")
            print(f"Contraseña generada: {password_generated}")

            if 'foto' in datos_terapeuta:
                self.driver.find_element(By.XPATH, "//input[@name='foto']").send_keys(datos_terapeuta['foto'])
                print("Foto cargada correctamente.")

            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            print("Nuevo terapeuta guardado exitosamente.")
            time.sleep(2)

            return "Terapeuta creado exitosamente"
        except Exception as e:
            print(f"Error al crear el terapeuta: {e}")
            return "Error al crear el terapeuta"

    def test_crear_terapeuta(self):
        self.login("liliana@gmail.com", "lilianaC")
        actual = self.check_login_success()
        assert actual == "Login exitoso", f"FALLÓ: Se esperaba 'Login exitoso', pero se obtuvo '{actual}'"

        self.navigate_to_terapeutas()

        self.navigate_create_terapeuta()

        datos_terapeuta = {
            "nombre": "Bruce",
            "apellido": "Wayne",
            "telefono": "71111111",
            "email": "bruceWayne@gmail.com",
            "especialidad": "Psicología",
            "licencia_medica": "33333333",
            "fecha_nacimiento": "10-05-2002",
            "foto": r"C:\Users\Tristan\Downloads\bruce.jpg"
        }

        resultado = self.create_terapeuta(datos_terapeuta)
        esperado = "Terapeuta creado exitosamente"
        assert resultado == esperado, f"FALLÓ: Se esperaba '{esperado}', pero se obtuvo '{resultado}'"

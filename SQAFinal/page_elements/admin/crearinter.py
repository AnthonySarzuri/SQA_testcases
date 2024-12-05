import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestInternos:
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

    def navigate_create_interno(self):
        self.driver.find_element(By.XPATH, "//a[@href='/internos/crear']").click()
        print("Navegando a la página de creación de un nuevo interno...")
        time.sleep(2)

    def create_interno(self, datos_interno):
        try:
            self.driver.find_element(By.XPATH, "//input[@name='nombre']").send_keys(datos_interno['nombre'])
            self.driver.find_element(By.XPATH, "//input[@name='apellido']").send_keys(datos_interno['apellido'])
            self.driver.find_element(By.XPATH, "//input[@name='telefono']").send_keys(datos_interno['telefono'])
            self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(datos_interno['email'])
            self.driver.find_element(By.XPATH, "//input[@name='fecha_nacimiento']").send_keys(datos_interno['fecha_nacimiento'])

            self.driver.find_element(By.XPATH, "//button[@onclick='generarContraseña()']").click()
            time.sleep(1)

            password_generated = self.driver.find_element(By.XPATH, "//input[@name='password']").get_attribute("value")
            print(f"Contraseña generada: {password_generated}")

            if 'foto' in datos_interno:
                self.driver.find_element(By.XPATH, "//input[@name='foto']").send_keys(datos_interno['foto'])
                print("Foto cargada correctamente.")

            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            print("Nuevo interno guardado exitosamente.")
            time.sleep(2)

            return "Interno creado exitosamente"
        except Exception as e:
            print(f"Error al crear el interno: {e}")
            return "Error al crear el interno"

    def wait_for_interno_to_appear(self, nombre):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//h3[contains(text(), '{nombre}')]"))
            )
            print("Interno creado y visible en la lista.")
            return "Interno visible"
        except Exception as e:
            print(f"Error al esperar que el interno aparezca: {e}")
            return "Interno no visible"

    def test_crear_interno(self):
        # Login
        self.login("liliana@gmail.com", "lilianaC")
        actual = self.check_login_success()
        assert actual == "Login exitoso", f"FALLÓ: Se esperaba 'Login exitoso', pero se obtuvo '{actual}'"

        self.navigate_to_internos()

        self.navigate_create_interno()

        datos_interno = {
            "nombre": "Clark",
            "apellido": "Kent",
            "telefono": "71111111",
            "email": "clark@gmail.com",
            "fecha_nacimiento": "10-05-2002",
            "foto": r"C:\Users\Tristan\Downloads\clark.jpg"
        }

        resultado = self.create_interno(datos_interno)
        esperado = "Interno creado exitosamente"
        assert resultado == esperado, f"FALLÓ: Se esperaba '{esperado}', pero se obtuvo '{resultado}'"

        visibilidad = self.wait_for_interno_to_appear(datos_interno["nombre"])
        esperado_visibilidad = "Interno visible"
        assert visibilidad == esperado_visibilidad, f"FALLÓ: Se esperaba '{esperado_visibilidad}', pero se obtuvo '{visibilidad}'"

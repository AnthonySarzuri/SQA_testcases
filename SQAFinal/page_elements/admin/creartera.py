from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def login(driver, email, password):
    driver.get('http://localhost:3000')
    driver.find_element(By.XPATH, "//div[@class='relative']//input[@type='email']").send_keys(email)
    driver.find_element(By.XPATH, "//div[@class='relative']//input[@type='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

def check_login_success(driver):
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "//h2[contains(text(), 'Bienvenido')]")
        print("Login exitoso.")
        return True
    except Exception:
        print("Login fallido.")
        return False

def navigate_to_terapeutas(driver):
    driver.find_element(By.XPATH, "//a[@href='/terapeutas']").click()
    print("Navegando a la página de Terapeutas...")
    time.sleep(2)

def navigate_create_terapeuta(driver):
    driver.find_element(By.XPATH, "//a[@href='/terapeutas/nuevo']").click()
    print("Navegando a la página de creación de un nuevo terapeuta...")
    time.sleep(2)

def create_terapeuta(driver, datos_terapeuta):
    try:
        driver.find_element(By.XPATH, "//input[@name='nombre']").send_keys(datos_terapeuta['nombre'])
        driver.find_element(By.XPATH, "//input[@name='apellido']").send_keys(datos_terapeuta['apellido'])
        driver.find_element(By.XPATH, "//input[@name='telefono']").send_keys(datos_terapeuta['telefono'])
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(datos_terapeuta['email'])
        driver.find_element(By.XPATH, "//input[@name='especialidad']").send_keys(datos_terapeuta['especialidad'])
        driver.find_element(By.XPATH, "//input[@name='licencia_medica']").send_keys(datos_terapeuta['licencia_medica'])
        driver.find_element(By.XPATH, "//input[@name='fecha_nacimiento']").send_keys(datos_terapeuta['fecha_nacimiento'])

        driver.find_element(By.XPATH, "//button[@onclick='generarContraseña()']").click()
        time.sleep(1)

        password_generated = driver.find_element(By.XPATH, "//input[@name='password']").get_attribute("value")
        print(f"Contraseña generada: {password_generated}")

        if 'foto' in datos_terapeuta:
            driver.find_element(By.XPATH, "//input[@name='foto']").send_keys(datos_terapeuta['foto'])
            print("Foto cargada correctamente.")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("Nuevo terapeuta guardado exitosamente.")
        time.sleep(2)
    except Exception as e:
        print(f"Error al crear el terapeuta: {e}")

def main():
    driver = setup_driver()

    try:
        login(driver, "liliana@gmail.com", "lilianaC")
        if not check_login_success(driver):
            return

        navigate_to_terapeutas(driver)

        navigate_create_terapeuta(driver)

        datos_terapeuta = {
            "nombre": "Bruce",
            "apellido": "Wayne",
            "telefono": "71123456",
            "email": "bruce@gmail.com",
            "especialidad": "Psicología",
            "licencia_medica": "11111111",
            "fecha_nacimiento": "10-05-2002",
            "foto": r"C:\Users\Tristan\Downloads\bruce.jpg"
        }

        create_terapeuta(driver, datos_terapeuta)

    finally:
        driver.quit()
        print("Prueba visual completada.")

if __name__ == "__main__":
    main()

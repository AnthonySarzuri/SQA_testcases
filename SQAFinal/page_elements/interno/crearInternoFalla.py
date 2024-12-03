from selenium import webdriver
from selenium.webdriver.common.by import By
import time

users = [
    ("liliana@gmail.com", "lilianaC"),
    ("can@gmail.com", "72005945CA"),
    ("sg@gmail.com", "40938985SG")
]

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def login(driver, email, password):
    driver.get('http://localhost:3000')
    driver.find_element(By.XPATH, "//div[@class='relative']//input[@type='email']").send_keys(email)
    driver.find_element(By.XPATH, "//div[@class='relative']//input[@type='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

def is_login_successful(driver):
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "//h2[contains(text(), 'Bienvenido')]")
        return True
    except Exception:
        return False

def main():
    driver = setup_driver()
    try:
        email, password = users[1]
        print(f"Iniciando sesión con: {email}")
        login(driver, email, password)

        if not is_login_successful(driver):
            print("Inicio de sesión fallido. Las credenciales no son válidas.")
            return

        # Navegar a la lista de pacientes
        driver.find_element(By.XPATH, "//a[@href='/pacientes']").click()
        print("Para ver pacientes.")

        time.sleep(2)

        # Intentar crear un nuevo paciente
        driver.find_element(By.XPATH, "//i[@class='fas fa-user-plus mr-2']").click()
        print("Navegando a la creación de un nuevo paciente.")

        # Llenar el formulario de creación
        driver.find_element(By.XPATH, "//input[@name='persona_id']").send_keys("7942515")
        driver.find_element(By.XPATH, "//input[@name='nombre']").send_keys("Anthony")
        driver.find_element(By.XPATH, "//input[@name='apellido']").send_keys("Sarzuri")
        driver.find_element(By.XPATH, "//input[@name='telefono']").send_keys("62494843")
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("sa@gmail.com")
        driver.find_element(By.XPATH, "//input[@name='fecha_nacimiento']").send_keys("06/10/2002")
        driver.find_element(By.XPATH, "//select[@name='genero']//option[@value='M']").click()
        driver.find_element(By.XPATH, "//input[@name='direccion']").send_keys("C Lourdes n2095")
        driver.find_element(By.XPATH, "//input[@name='numero_seguro']").send_keys("12456487")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("Formulario enviado, esperando redirección...")

        start_time = time.time()
        while time.time() - start_time < 5:
            if driver.current_url == "http://localhost:3000/pacientes":
                print("Redirección exitosa a la lista de pacientes.")
                break
            time.sleep(0.5)
        else:
            print(f"Esperado: {"http://localhost:3000/pacientes"} | Actual: {driver.current_url} | No se editó en 5 segundos.")

    finally:
        driver.quit()
        print("Prueba visual completada")

if __name__ == "__main__":
    main()
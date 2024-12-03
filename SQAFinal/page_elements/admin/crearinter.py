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

def navigate_to_internos(driver):
    driver.find_element(By.XPATH, "//a[@href='/internos']").click()
    print("Navegando a la página de Internos...")
    time.sleep(2)

def navigate_create_interno(driver):
    driver.find_element(By.XPATH, "//a[@href='/internos/crear']").click()
    print("Navegando a la página de creación de un nuevo interno...")
    time.sleep(2)

def create_interno(driver, datos_interno):

    try:

        driver.find_element(By.XPATH, "//input[@name='nombre']").send_keys(datos_interno['nombre'])
        driver.find_element(By.XPATH, "//input[@name='apellido']").send_keys(datos_interno['apellido'])
        driver.find_element(By.XPATH, "//input[@name='telefono']").send_keys(datos_interno['telefono'])
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(datos_interno['email'])
        driver.find_element(By.XPATH, "//input[@name='fecha_nacimiento']").send_keys(datos_interno['fecha_nacimiento'])


        driver.find_element(By.XPATH, "//button[@onclick='generarContraseña()']").click()
        time.sleep(1)


        password_generated = driver.find_element(By.XPATH, "//input[@name='password']").get_attribute("value")
        print(f"Contraseña generada: {password_generated}")


        if 'foto' in datos_interno:
            driver.find_element(By.XPATH, "//input[@name='foto']").send_keys(datos_interno['foto'])
            print("Foto cargada correctamente.")


        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("Nuevo interno guardado exitosamente.")
        time.sleep(2)
    except Exception as e:
        print(f"Error al crear el interno: {e}")

def main():
    driver = setup_driver()

    try:

        login(driver, "liliana@gmail.com", "lilianaC")
        if not check_login_success(driver):
            return


        navigate_to_internos(driver)


        navigate_create_interno(driver)


        datos_interno = {
            "nombre": "Clark",
            "apellido": "Kent",
            "telefono": "71234567",
            "email": "clark.kent@gmail.com",
            "fecha_nacimiento": "10-05-2002",
            "foto": r"C:\Users\Tristan\Downloads\clark.jpg"
        }


        create_interno(driver, datos_interno)

    finally:
        driver.quit()
        print("Prueba visual completada.")

if __name__ == "__main__":
    main()

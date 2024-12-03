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
        welcome_element = driver.find_element(By.XPATH, "//h2[contains(text(), 'Bienvenido')]")
        if welcome_element:
            print("Login exitoso, navegando a la página de bienvenida...")
    except Exception:
        print("Login fallido, credenciales no válidas.")
        driver.quit()
        return False
    return True

def navigate_to_internos(driver):

    driver.find_element(By.XPATH, "//a[@href='/internos']").click()
    print("Navegando a la página de Internos...")
    time.sleep(2)

def edit_interno(driver, nuevo_nombre):

    try:

        driver.find_element(By.XPATH, "//a[contains(@href, '/internos/editar')]").click()
        print("Entrando a la página de edición de interno...")
        time.sleep(2)


        nombre_input = driver.find_element(By.XPATH, "//input[@name='nombre']")
        nombre_input.clear()
        nombre_input.send_keys(nuevo_nombre)
        print(f"Nuevo nombre ingresado: {nuevo_nombre}")


        driver.find_element(By.XPATH, "//button[@class='w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700 flex items-center justify-center']").click()
        print("Guardando los cambios...")
        time.sleep(2)

        print("Cambios guardados correctamente.")
    except Exception as e:
        print(f"Error al editar el interno: {e}")

def return_to_home(driver):

    driver.find_element(By.XPATH, "//button[@class='bg-yellow-600 text-white px-4 py-2 rounded hover:bg-yellow-700 flex items-center']").click()
    print("Regresando a la página principal...")
    time.sleep(2)

def main():
    driver = setup_driver()

    try:

        login(driver, "liliana@gmail.com", "lilianaC")
        if not check_login_success(driver):
            return


        navigate_to_internos(driver)


        nuevo_nombre = "Cristhian Modificado"
        edit_interno(driver, nuevo_nombre)


        return_to_home(driver)

    finally:
        time.sleep(5)
        driver.quit()
        print("Prueba visual completada")

if __name__ == "__main__":
    main()

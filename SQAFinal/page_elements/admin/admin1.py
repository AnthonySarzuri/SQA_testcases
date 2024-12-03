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

def navigate_to_pacientes(driver):
    driver.find_element(By.XPATH, "//a[@href='/pacientes']").click()
    print("Navegando a la página de Pacientes...")
    time.sleep(2)

def view_historial(driver):
    driver.find_element(By.XPATH, "(//button[@class='bg-green-500 text-white px-3 py-1 rounded hover:bg-green-600 flex items-center'])[1]").click()
    print("Visualizando el historial del paciente Marc Spector...")
    time.sleep(2)


def return_to_list(driver):
    driver.find_element(By.XPATH, "//a[@href='/pacientes']").click()
    print("Regresando al listado de pacientes...")
    time.sleep(2)

def return_to_home(driver):
    driver.find_element(By.XPATH, "//button[@class='bg-yellow-600 text-white px-4 py-2 rounded hover:bg-yellow-700 flex items-center']").click()
    print("Regresando a la página principal...")
    time.sleep(2)

def main():
    driver = setup_driver()

    try:
        # Login
        login(driver, "liliana@gmail.com", "lilianaC")
        if not check_login_success(driver):
            return

        navigate_to_pacientes(driver)

        view_historial(driver)

        return_to_list(driver)

        return_to_home(driver)

    finally:
        time.sleep(5)
        driver.quit()
        print("Prueba visual completada")

if __name__ == "__main__":
    main()

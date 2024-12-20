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
        # V
        welcome_element = driver.find_element(By.XPATH, "//h2[contains(text(), 'Bienvenido')]")
        if welcome_element:
            print("Login exitoso, navegando a la página de bienvenida...")
    except Exception:
        print("Login fallido, credenciales no válidas.")
        driver.quit()
        return False
    return True

def navigate_to_pacientes(driver):
    """Navega a la página de Pacientes."""
    driver.find_element(By.XPATH, "//a[@href='/pacientes']").click()
    print("Navegando a la página de Pacientes...")
    time.sleep(2)

def view_historial(driver):

    driver.find_element(By.XPATH, "(//button[@class='bg-green-500 text-white px-3 py-1 rounded hover:bg-green-600 flex items-center'])[2]").click()
    print("Visualizando el historial del paciente Marc Spector...")
    time.sleep(2)
# form
    fill_diagnosis_form(driver)

def fill_diagnosis_form(driver):

    try:

        add_button_xpath = "//button//i[@class='fas fa-plus-circle mr-2']"
        driver.find_element(By.XPATH, add_button_xpath).click()
        print("Botón para agregar diagnóstico pulsado...")
        time.sleep(2)

        observaciones_xpath = "//textarea[@name='observaciones']"
        driver.find_element(By.XPATH, observaciones_xpath).send_keys("Paciente presenta avances moderados.")
        time.sleep(2)

        puntuacion_xpath = "//select[@name='puntuacion']//option[@value='neutral']"
        driver.find_element(By.XPATH, puntuacion_xpath).click()
        time.sleep(2)

        enfermedad_xpath = "//select[@name='enfermedad_id']//option[@value='6']"
        driver.find_element(By.XPATH, enfermedad_xpath).click()
        time.sleep(2)

        agregar_diagnostico_xpath = "//button//i[@class='fas fa-plus-circle mr-2']"
        driver.find_element(By.XPATH, agregar_diagnostico_xpath).click()

        print("Formulario llenado y diagnóstico agregado correctamente.")
    except Exception as e:
        print(f"Error al llenar el formulario: {e}")



def main():
    driver = setup_driver()

    try:
        # Login
        login(driver, "sg@gmail.com", "40938985SG")
        if not check_login_success(driver):
            return

        # Navegar a Pacientes
        navigate_to_pacientes(driver)

        # Ver Historial
        view_historial(driver)

    finally:
        time.sleep(5)
        driver.quit()
        print("Prueba visual completada")

if __name__ == "__main__":
    main()
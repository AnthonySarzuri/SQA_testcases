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

def delete_terapeuta(driver):
    try:
        delete_button = driver.find_element(By.XPATH, "(//button[@class='bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600 flex items-center'])[2]")
        delete_button.click()
        print("Botón de eliminar clickeado. Esperando alerta...")

        alert = driver.switch_to.alert
        alert.accept()
        print("Alerta aceptada. Terapeuta eliminado exitosamente.")

        time.sleep(2)
    except Exception as e:
        print(f"Error al eliminar el terapeuta: {e}")

def main():
    driver = setup_driver()

    try:
        login(driver, "liliana@gmail.com", "lilianaC")
        if not check_login_success(driver):
            return

        navigate_to_terapeutas(driver)

        delete_terapeuta(driver)

    finally:
        driver.quit()
        print("Prueba de eliminación completada.")

if __name__ == "__main__":
    main()

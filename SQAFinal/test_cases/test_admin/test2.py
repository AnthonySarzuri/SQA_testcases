from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup_driver():
    """Configura el WebDriver y maximiza la ventana del navegador."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def login(driver, email, password):
    """Realiza el login en la aplicación."""
    driver.get('http://localhost:3000')
    driver.find_element(By.XPATH, "//div[@class='relative']//input[@type='email']").send_keys(email)
    driver.find_element(By.XPATH, "//div[@class='relative']//input[@type='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

def check_login_success(driver):
    """Verifica si el login fue exitoso y navega a la página de bienvenida."""
    time.sleep(2)  # Espera a que se procese el login
    try:
        # Verifica si hay un elemento que indica un inicio de sesión exitoso
        welcome_element = driver.find_element(By.XPATH, "//h2[contains(text(), 'Bienvenido')]")
        if welcome_element:
            print("Login exitoso, navegando a la página de bienvenida...")
            driver.get('http://localhost:3000/welcome')
    except Exception as e:
        print("Login fallido, credenciales no válidas.")

def main():
    driver = setup_driver()

    try:
        login(driver, "liliana@gmail.com", "lilianaC")
        check_login_success(driver)
    finally:
        time.sleep(5)
        driver.quit()
        print("Prueba visual completada")

if __name__ == "__main__":
    main()
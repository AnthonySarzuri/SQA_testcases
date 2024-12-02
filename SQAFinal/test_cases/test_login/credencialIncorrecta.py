"""
Antes de ejecutar el test, ejecutar el siguiente comando para instalar la librería necesaria

pip install selenium webdriver-manager
"""

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

def check_credentials_error(driver, expected_message):

    time.sleep(2)  # Espera a que aparezca el mensaje
    try:
        actual_message_element = driver.find_element(By.XPATH, "//p[text()='Credenciales no válidas']")
        actual_message = actual_message_element.text
    except Exception as e:
        actual_message = "No se encontró el mensaje de error"

    if actual_message == expected_message:
        print(f"Esperado: '{expected_message}' Actual: '{actual_message}'")
    else:
        print(f"Esperado: '{expected_message}' Actual: '{actual_message}'")

def main():
    expected_message = "Credenciales no válidas"
    driver = setup_driver()

    try:
        login(driver, "noreply@domain.com", "password")
        check_credentials_error(driver, expected_message)
    finally:
        time.sleep(5)
        driver.quit()
        print("Prueba visual completada")

if __name__ == "__main__":
    main()
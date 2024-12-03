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

        driver.find_element(By.XPATH, "//a[@href='/pacientes']").click()
        print("Para ver pacientes.")

        time.sleep(2)

    finally:
        driver.quit()
        print("Prueba visual completada")

if __name__ == "__main__":
    main()
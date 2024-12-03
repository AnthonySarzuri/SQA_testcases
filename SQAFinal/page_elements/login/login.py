from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

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

def determine_user_type(driver):
    user_type = None
    try:
        admin_links = [
            driver.find_element(By.XPATH, "//a[@href='/pacientes']"),
            driver.find_element(By.XPATH, "//a[@href='/terapeutas']"),
            driver.find_element(By.XPATH, "//a[@href='/internos']")
        ]
        if all(admin_links):
            user_type = "administrador"
            return user_type
    except Exception:
        pass

    try:
        interno_links = [
            driver.find_element(By.XPATH, "//a[@href='/pacientes']"),
            driver.find_element(By.XPATH, "//a[@href='/enfermedades']")
        ]
        if all(interno_links):
            user_type = "interno"
            return user_type
    except Exception:
        pass

    user_type = "terapeuta"
    return user_type

def logout(driver):
    time.sleep(5)
    driver.find_element(By.XPATH, "//form[@action='/logout']").submit()
    print("Sesión cerrada.")

def main():
    driver = setup_driver()
    try:
        email, password = random.choice(users)
        print(f"Iniciando sesión con: {email}")
        login(driver, email, password)

        if not is_login_successful(driver):
            print("Inicio de sesión fallido. Las credenciales no son válidas.")
            return

        user_type = determine_user_type(driver)
        print(f"El tipo de usuario es: {user_type}")
        logout(driver)

    finally:
        time.sleep(2)
        driver.quit()
        print("Prueba visual completada")

if __name__ == "__main__":
    main()
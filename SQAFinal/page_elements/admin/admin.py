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
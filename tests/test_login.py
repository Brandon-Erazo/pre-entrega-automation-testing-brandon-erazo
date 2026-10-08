import pytest # se importa la librería pytest para poder utilizar sus funcionalidades, como la ejecución de pruebas y la generación de reportes
from selenium import webdriver # Se importa la clase webdriver del módulo selenium para poder controlar el navegador web y realizar acciones de automatización en él
from selenium.webdriver.common.by import By # El módulo By se importa para poder localizar elementos en la página web utilizando diferentes estrategias, como ID, nombre, clase, etc.
# import time # el módulo time se importa para poder usar la función sleep y pausar la ejecución del script si es necesario


def test_login_exitoso():
    # Iniciar el navegador
    driver = webdriver.Chrome()

    try: 
        # Abrir la página de inicio de sesión de SauceDemo
        driver.get("https://www.saucedemo.com/")

        # localizar elementos de la página de inicio de sesión y realizar acciones sobre ellos
        usuario = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        boton_login = driver.find_element(By.ID,"login-button")

        # Completar el formulario
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")

        # Hacer login
        boton_login.click()

        # Validar el URL despues del login
        assert "inventory.html" in driver.current_url
        # Validar texto del logo de la página de inventario
        logo = driver.find_element(By.CLASS_NAME,"app_logo")
        assert logo.text == "Swag Labs"
        # Validar el título de la página de inventario
        titulo = driver.find_element(By.CSS_SELECTOR,'[data-test="title"]')
        assert titulo.text == "Products"

    finally:
            driver.quit()   

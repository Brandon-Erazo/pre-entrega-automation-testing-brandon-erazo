import pytest # se importa la librería pytest para poder utilizar sus funcionalidades, como la ejecución de pruebas y la generación de reportes
from selenium import webdriver # Se importa la clase webdriver del módulo selenium para poder controlar el navegador web y realizar acciones de automatización en él
from selenium.webdriver.common.by import By # El módulo By se importa para poder localizar elementos en la página web utilizando diferentes estrategias, como ID, nombre, clase, etc.

def test_inventory_exitoso():
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

        #Verificar que el título de la página es "Swag Labs"
        assert driver.title == "Swag Labs"

        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0 # Verificar que hay productos en la página de inventario

        primer_producto = productos[0]

        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

        assert nombre_producto == "Sauce Labs Backpack" # Verificar que el nombre del primer producto es "Sauce Labs Backpack"
        assert precio_producto == "$29.99" # Verificar que el precio del primer producto es "$29.99"

        #Verificar menu hamburguesa
        menu_hamburguesa = driver.find_element(By.ID, "react-burger-menu-btn")

        assert menu_hamburguesa.is_displayed() # Verificar que el menú hamburguesa está visible

        #Verificar filtro
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

        assert filtro.is_displayed() # Verificar que el filtro está visible

    finally:
            driver.quit()
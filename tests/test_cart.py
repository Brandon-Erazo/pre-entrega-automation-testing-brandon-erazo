import pytest # se importa la librería pytest para poder utilizar sus funcionalidades, como la ejecución de pruebas y la generación de reportes
from selenium import webdriver # Se importa la clase webdriver del módulo selenium para poder controlar el navegador web y realizar acciones de automatización en él
from selenium.webdriver.common.by import By # El módulo By se importa para poder localizar elementos en la página web utilizando diferentes estrategias, como ID, nombre, clase, etc.
# import time # el módulo time se importa para poder usar la función sleep y pausar la ejecución del script si es necesario

from selenium.webdriver.support.ui import WebDriverWait # Se importa la clase WebDriverWait del módulo selenium.webdriver.support.ui para poder esperar de manera explícita a que ciertos elementos estén presentes o visibles en la página antes de interactuar con ellos
from selenium.webdriver.support import expected_conditions as EC # Se importa el módulo expected_conditions del paquete selenium.webdriver.support para poder utilizar condiciones predefinidas que se pueden esperar, como la presencia o visibilidad de un elemento

def test_cart():
    # Iniciar el navegador
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 10) # Se crea una instancia de WebDriverWait con un tiempo de espera máximo de 10 segundos

    try: 
        # Abrir la página de inicio de sesión de SauceDemo
        driver.get("https://www.saucedemo.com/")

        # localizar elementos de la página de inicio de sesión y realizar acciones sobre ellos
        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user") # Esperar hasta que el elemento con ID "user-name" esté presente en la página
        password = driver.find_element(By.ID,"password")
        boton_login = driver.find_element(By.ID,"login-button")

        # Completar el formulario
        password.send_keys("secret_sauce")

        # Hacer login
        boton_login.click()

        primer_producto = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))) # Esperar hasta que el primer producto esté presente en la página de inventario
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        boton_add_to_cart = primer_producto.find_element(By.TAG_NAME, "button")

        boton_add_to_cart.click() # Hacer clic en el botón "Add to cart" del primer producto

        contador_carrito = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))) # Esperar hasta que el contador del carrito esté presente en la página
        assert contador_carrito.text == "1" # Verificar que el contador del carrito muestra "1"

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link"))).click() # Hacer clic en el enlace del carrito de compras

        nombre_producto_en_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text # Esperar hasta que el producto en el carrito esté visible en la página
        assert nombre_producto_en_carrito == nombre_producto # Verificar que el producto en el carrito es el mismo que se agregó
    
    finally:
        driver.quit()
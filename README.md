Pre-entrega Automation Testing – SauceDemo

Proyecto de automatización de pruebas funcionales para el sitio SauceDemo, desarrollado con Python, Pytest y Selenium WebDriver.

🎯 Propósito del proyecto

El objetivo es automatizar los principales flujos de la aplicación SauceDemo para validar su correcto funcionamiento de forma repetible y rápida:

Login con credenciales válidas
Verificación del catálogo de productos
Interacción con el carrito de compras (añadir primer producto y verificar ítem en carrito)

🛠️ Tecnologías utilizadas
Tecnología	Uso
Python	Lenguaje de programación principal
Pytest	Framework de testing para estructurar y ejecutar las pruebas
Selenium WebDriver	Automatización de la interfaz web
pytest-html	Generación de reportes HTML
Git / GitHub	Control de versiones y distribución del código

📋 Requisitos previos
Python 3.9 o superior
Google Chrome instalado
Git

Selenium 4.6+ incluye Selenium Manager, que descarga automáticamente el ChromeDriver compatible con tu versión de Chrome. No es necesario instalarlo manualmente.

⚙️ Instalación de dependencias
Clonar el repositorio:
bash
   git clone <URL_DEL_REPOSITORIO>
   cd pre-entrega-automation-testing
(Recomendado) Crear y activar un entorno virtual:
bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
Instalar las dependencias, una por una:
Dependencia	Para qué sirve	Comando
Pytest	Framework para estructurar y ejecutar las pruebas	pip install pytest
Pytest-HTML	Plugin de Pytest que genera el reporte en HTML	pip install pytest-html
Selenium WebDriver	Automatización del navegador	pip install selenium
O bien, todas juntas en un solo comando:
bash
   pip install pytest pytest-html selenium
Verificar la instalación:
bash
   python --version
   pytest --version
   pip show pytest-html
   pip show selenium
▶️ Ejecución de las pruebas

Ejecutar todas las pruebas y generar el reporte HTML:

bash
pytest -v --html=reporte.html

Al finalizar, abrir el archivo reporte.html en el navegador para ver el detalle de los resultados.

🔗 Control de versiones

El código se gestiona con Git y se aloja en GitHub:

bash
git add .
git commit -m "Descripción del cambio"
git push origin main

👤 Autor: Brandon Erazo

Proyecto realizado como pre-entrega del curso de Automation Testing.
# Pre-entrega Automation Testing – SauceDemo

Proyecto de automatización de pruebas funcionales para el sitio [SauceDemo](https://www.saucedemo.com), desarrollado con Python, Pytest y Selenium WebDriver.

## 🎯 Propósito del proyecto

El objetivo es automatizar los principales flujos de la aplicación SauceDemo para validar su correcto funcionamiento de forma repetible y rápida:

- **Login** con credenciales válidas
- **Verificación del catálogo** de productos
- **Interacción con el carrito de compras** (añadir el primer producto y verificar el ítem en el carrito)

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| **Python** | Lenguaje de programación principal |
| **Pytest** | Framework de testing para estructurar y ejecutar las pruebas |
| **Selenium WebDriver** | Automatización de la interfaz web |
| **pytest-html** | Generación de reportes HTML |
| **Git / GitHub** | Control de versiones y distribución del código |

## 📋 Requisitos previos

- Python 3.9 o superior
- Google Chrome instalado
- Git

> Selenium 4.6+ incluye **Selenium Manager**, que descarga automáticamente el ChromeDriver compatible con tu versión de Chrome. No es necesario instalarlo manualmente.

## ⚙️ Instalación de dependencias

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Brandon-Erazo/pre-entrega-automation-testing-brandon-erazo.git
   cd pre-entrega-automation-testing-brandon-erazo
   ```

2. Instalar las dependencias, una por una:

   | Dependencia | Para qué sirve | Comando |
   |---|---|---|
   | **Pytest** | Framework para estructurar y ejecutar las pruebas | `pip install pytest` |
   | **Pytest-HTML** | Plugin de Pytest que genera el reporte en HTML | `pip install pytest-html` |
   | **Selenium WebDriver** | Automatización del navegador | `pip install selenium` |

   O bien, todas juntas en un solo comando:

   ```bash
   pip install pytest pytest-html selenium
   ```

3. Verificar la instalación:

   ```bash
   python --version
   pytest --version
   pip show pytest-html
   pip show selenium
   ```

## ▶️ Ejecución de las pruebas

Ejecutar todas las pruebas y generar el reporte HTML:

```bash
pytest -v --html=reports/reporte.html
```

Al finalizar, abrir el archivo `reports/reporte.html` en el navegador para ver el detalle de los resultados.

## 📁 Estructura del proyecto

```
pre-entrega-automation-testing-brandon-erazo/
├── reports/
│   └── reporte.html
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_cart.py
├── .gitignore
└── README.md
├── pytest.ini
```

## 🧪 Credenciales de prueba (SauceDemo)

| Usuario | Contraseña |
|---|---|
| `standard_user` | `secret_sauce` |

## 👤 Autor

**Brandon Erazo**

Proyecto realizado como pre-entrega del curso de Automation Testing.

from Functions.Functions import Functions as Selenium

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException


class Test_002(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome() #Abrir Chrome
        self.driver.implicitly_wait(10) #Esperamos 10 segundos
        self.driver.maximize_window() #Maximizamos la ventana
        
        #Ingresamos a la página
        self.driver.get("https://shop.thonet-vander.com/")
        time.sleep(2)
        
    def test_002(self):
        Selenium.get_json_file(self, "thonet")
        #Inicio de sesión
        login_button = Selenium.get_elements(self, "Loggin_button")  
        self.assertTrue(login_button.is_displayed(), "El botón 'Iniciar sesión' no se encuentra.")
        login_button.click()
        
        #email
        email = Selenium.get_elements(self, "Email")
        email.send_keys("automationtestsNoe@outlook.com")
        
        #password
        password = Selenium.get_elements(self, "Password")
        password.send_keys("testautomation")
        time.sleep(2)
        
        #Ingresar
        ingresar = Selenium.get_elements(self, "Ingresar")
        self.assertTrue(ingresar.is_displayed(), "El botón 'Ingresar' no se encuentra.")
        ingresar.click()
        time.sleep(5)
        
        #Validar cuenta
        cuenta = Selenium.get_elements(self, "Cuenta")
        texto_cuenta = cuenta.text
        texto_esperado = "Hola, Noelia"
        self.assertEqual(texto_cuenta, texto_esperado, f"La cuenta ({texto_cuenta}) no coincide con la esperada ({texto_esperado})")
        print("Es la cuenta correcta.")
        
        #Buscar producto
        buscador = Selenium.get_elements(self, "Buscador")
        buscador.send_keys("VX75")
        time.sleep(1)
        buscador.send_keys(Keys.RETURN)
        time.sleep(5)
        
        #Validar producto
        producto1 = Selenium.get_elements(self, "Producto1")
        texto_producto1 = producto1.text
        texto_esperado1 = "VX75"
        self.assertEqual(texto_producto1, texto_esperado1, f"El producto ({texto_producto1}) no coincide con el esperado ({texto_esperado1})")
        print("Es el producto correcto.")
        
        #Click en producto buscado
        VX75 = Selenium.get_elements(self, "VX75")
        VX75.click()
        time.sleep(5)
        
        #Validar botón Agregar al carrito
        agregar_carrito = Selenium.get_elements(self, "Agregar_carrito")
        texto_carrito = agregar_carrito.text
        esperado_carrito = "Agregar al carrito"
        self.assertEqual(texto_carrito, esperado_carrito, f"El botón ({texto_carrito}) no se encuentra ({esperado_carrito})")
        print("Es botón es visible.")
        
        #Click en Agregar al carrito
        agregar_carrito.click()
        time.sleep(5)
       
        #Validar producto en la cart
        producto_carrito = Selenium.get_elements(self, "Producto_carrito")
        textoproducto_carrito = producto_carrito.text
        productocarrito_esperado = "VX75"
        self.assertEqual(textoproducto_carrito, productocarrito_esperado, f"El producto ({textoproducto_carrito}) no coincide con el solicitado ({productocarrito_esperado})")
        print("El producto coincide con el solicitado.")
        
        #Validar Ir a mi carrito
        iracarrito = Selenium.get_elements(self, "Ir_carrito")
        texto_iracarrito = iracarrito.text
        esperado_iracarrito = "Ir a mi carrito"
        self.assertEqual(texto_iracarrito, esperado_iracarrito, f"El botón ({texto_iracarrito}) no se encuentra ({esperado_iracarrito})")
        print("Se visualiza correctamente el botón 'Ir a mi carrito'.")
        
        #Click Ir a mi carrito
        iracarrito.click()
        time.sleep(5)
        
        #Validar estar en Mi carrito
        micarrito = Selenium.get_elements(self, "Mi_carrito")
        validarcarrito = micarrito.text
        esperado_micarrito = "Mi Carrito"
        self.assertEqual(validarcarrito, esperado_micarrito, f"No se encuentra en la sección Mi Carrito")
        print("Se encuentra en la sección Mi Carrito")
        
        self.driver.save_screenshot('../Data/Evidencia/captura2.png')
        time.sleep(5)
        
        #({})
    def tearDown(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
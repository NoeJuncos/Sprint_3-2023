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


class Test_001(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome() #Abrir Chrome
        self.driver.implicitly_wait(10) #Esperamos 10 segundos
        self.driver.maximize_window() #Maximizamos la ventana
        
        #Ingresamos a la página
        self.driver.get("https://shop.thonet-vander.com/")
        time.sleep(2)

    def test_001(self):
        Selenium.get_json_file(self, "thonet")
        #Inicio de sesión
        login_button = Selenium.get_elements(self, "Loggin_button")   
        #self.driver.find_element(By.XPATH, "//header/div[2]/div[1]/div[3]/div[1]/div[1]/li[2]/a[1]")
        self.assertTrue(login_button.is_displayed(), "El botón 'Iniciar sesión' no se encuentra.")
        login_button.click()
        
        #email
        email = Selenium.get_elements(self, "Email")
        #email = self.driver.find_element(By.ID, "inputEmail")
        email.send_keys("automationtestsNoe@outlook.com")
        #password
        password = Selenium.get_elements(self, "Password")
        #password = self.driver.find_element(By.ID, "inputPassword")
        password.send_keys("testautomation")
        time.sleep(2)
        
        #Ingresar
        ingresar = Selenium.get_elements(self, "Ingresar")
        #ingresar = self.driver.find_element(By.XPATH, "//button[contains(text(),'INGRESÁ')]")
        self.assertTrue(ingresar.is_displayed(), "El botón 'Ingresar' no se encuentra.")
        ingresar.click()
        time.sleep(5)
        
        #Validar cuenta
        cuenta = Selenium.get_elements(self, "Cuenta")
        #cuenta = self.driver.find_element(By.XPATH, "//header/div[2]/div[1]/div[3]/div[1]/div[1]/li[1]/a[1]")
        texto_cuenta = cuenta.text
        texto_esperado = "Hola, Noelia"
        self.assertEqual(texto_cuenta, texto_esperado, f"La cuenta ({texto_cuenta}) no coincide con la esperada ({texto_esperado})")
        print("Es la cuenta correcta.")
        
        #Buscar producto
        buscador = Selenium.get_elements(self, "Buscador")
        #buscador = self.driver.find_element(By.ID, "buscador_buscar")
        buscador.send_keys("VX75")
        time.sleep(1)
        buscador.send_keys(Keys.RETURN)
        time.sleep(5)
        
        #Validar producto
        producto1 = Selenium.get_elements(self, "Producto1")
        #producto1 = self.driver.find_element(By.XPATH, "//h2[contains(text(),'VX75')]")
        texto_producto1 = producto1.text
        texto_esperado1 = "VX75"
        self.assertEqual(texto_producto1, texto_esperado1, f"El producto ({texto_producto1}) no coincide con el esperado ({texto_esperado1})")
        print("Es el producto correcto.")
        
        #Click en producto buscado
        VX75 = Selenium.get_elements(self, "VX75")
        #VX75 = self.driver.find_element(By.CSS_SELECTOR, "#imagen_second_152")
        VX75.click()
        time.sleep(5)
        
        #Click en +1 2 veces para que sean 3 productos
        sumar = Selenium.get_elements(self, "Sumar")
        #sumar = self.driver.find_element(By.XPATH, "//body/div[@id='contenido']/div[2]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/button[2]")
        sumar.click()
        time.sleep(1)
        sumar.click()
        time.sleep(2)
        
        #Validar botón Agregar al carrito
        agregar_carrito = Selenium.get_elements(self, "Agregar_carrito")
        #agregar_carrito = self.driver.find_element(By.XPATH, "//button[@id='argregarAlCarrito']")
        texto_carrito = agregar_carrito.text
        esperado_carrito = "Agregar al carrito"
        self.assertEqual(texto_carrito, esperado_carrito, f"El botón ({texto_carrito}) no se encuentra ({esperado_carrito})")
        print("Es botón es visible.")
        
        #Click en Agregar al carrito
        agregar_carrito.click()
        time.sleep(5)
        
        #Validar producto y cantidad en la cart
        producto_carrito = Selenium.get_elements(self, "Producto_carrito")
        #producto_carrito = self.driver.find_element(By.XPATH, "//a[contains(text(),'VX75')]")
        textoproducto_carrito = producto_carrito.text
        productocarrito_esperado = "VX75"
        self.assertEqual(textoproducto_carrito, productocarrito_esperado, f"El producto ({textoproducto_carrito}) no coincide con el solicitado ({productocarrito_esperado})")
        print("El producto coincide con el solicitado.")
        
        cantidad_carrito = Selenium.get_elements(self, "Cantidad_carrito")
        #cantidad_carrito = self.driver.find_element(By.CSS_SELECTOR, "#cantidad_459048")
        texto_cantidad = cantidad_carrito.text
        cantidad_esperada = "3"
        self.assertEqual(texto_cantidad, cantidad_esperada, f"La cantidad ({texto_cantidad}) no coincide con la solicitada ({cantidad_esperada})")
        print("La cantidad coincide con la solicitada.")
        time.sleep(5)
        
              
        
    def tearDown(self):
        pass



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
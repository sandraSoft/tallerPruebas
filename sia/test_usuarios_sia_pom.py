import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.inicio import Inicio
from pages.perfil import Perfil


class TestUsuariosSiaPom(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://acad.ucaldas.edu.co/Default.aspx")

    def tearDown(self):
        self.driver.quit()

    def test_login_funcionario(self):
        pagina_inicio = Inicio(self.driver)
        pagina_inicio.escribir_usuario("12345")
        pagina_inicio.escribir_contrasena("12345")
        pagina_inicio.click_ok()

        pagina_perfil = Perfil(self.driver)
        nombre_usuario = pagina_perfil.obtener_nombre_usuario()

        self.assertEqual("Funcionario de Prueba Becas", nombre_usuario)

        pagina_perfil.salir()

    def test_menu_becario(self):
        pagina_inicio = Inicio(self.driver)
        pagina_inicio.escribir_usuario("12345678")
        pagina_inicio.escribir_contrasena("12345678")
        pagina_inicio.click_ok()

        pagina_perfil = Perfil(self.driver)
        pagina_perfil.seleccionar_perfil(1)

        dashboard = Dashboard(self.driver)
        nombre_menu = dashboard.obtener_nombre_menu()

        self.assertEqual("Asuntos Estudiantiles", nombre_menu)

        dashboard.salir()

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestUsuariosSia(unittest.TestCase):

    def test_login_funcionario(self):
        driver = webdriver.Edge()
        driver.get("https://acad.ucaldas.edu.co/Default.aspx")

        usuario = driver.find_element(By.NAME, "ctl00$cphMaster$txtUsuario")
        contrasena = driver.find_element(By.NAME, "ctl00$cphMaster$txtContrasena")
        boton_ingresar = driver.find_element(By.NAME, "ctl00$cphMaster$btnIniciar")

        usuario.send_keys("12345")
        contrasena.send_keys("12345")
        boton_ingresar.click()

        etiqueta_nombre = driver.find_element(
            By.XPATH,
            "/html/body/form/center/table/tbody/tr[2]/td/div/div[11]/center/table/tbody/tr[1]/td[2]/b/i/span")

        self.assertEqual("Funcionario de Prueba Becas", etiqueta_nombre.text)

        enlace_salir = driver.find_element(By.LINK_TEXT, "Salir")
        enlace_salir.click()
        driver.quit()

    def test_menu_becario(self):
        driver = webdriver.Edge()
        driver.get("https://acad.ucaldas.edu.co/Default.aspx")

        usuario = driver.find_element(By.NAME, "ctl00$cphMaster$txtUsuario")
        contrasena = driver.find_element(By.NAME, "ctl00$cphMaster$txtContrasena")
        boton_ingresar = driver.find_element(By.NAME, "ctl00$cphMaster$btnIniciar")

        usuario.send_keys("12345678")
        contrasena.send_keys("12345678")
        boton_ingresar.click()

        select = driver.find_element(By.NAME, "ctl00$cphMaster$ddlPerfiles")
        perfil = Select(select)
        perfil.select_by_index(1)

        menu = driver.find_element(By.XPATH, "/html/body/form/center/table/tbody/tr[2]/td/div/div[11]/table/tbody/tr/td[1]/div/div/table/tbody/tr/td[2]/span/table/tbody/tr/td[2]")

        self.assertEqual("Asuntos Estudiantiles", menu.text)

        enlace_salir = driver.find_element(By.LINK_TEXT, "[Salir Modo Seguro]")
        enlace_salir.click()
        driver.quit()

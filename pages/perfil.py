from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Perfil:
    def __init__(self, driver):
        self.driver = driver

    def seleccionar_perfil(self, posicion):
        select = self.driver.find_element(By.NAME, "ctl00$cphMaster$ddlPerfiles")
        perfil = Select(select)
        perfil.select_by_index(posicion)

    def obtener_nombre_usuario(self):
        etiqueta_nombre = self.driver.find_element(
            By.XPATH,
            "/html/body/form/center/table/tbody/tr[2]/td/div/div[11]/center/table/tbody/tr[1]/td[2]/b/i/span")
        return etiqueta_nombre.text

    def salir(self):
        enlace_salir = self.driver.find_element(By.LINK_TEXT, "Salir")
        enlace_salir.click()

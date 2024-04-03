from selenium.webdriver.common.by import By


class Inicio:
    def __init__(self, driver):
        self.driver = driver

    def escribir_usuario(self, usuario):
        self.driver.find_element(By.NAME, "ctl00$cphMaster$txtUsuario").send_keys(usuario)

    def escribir_contrasena(self, contrasena):
        self.driver.find_element(By.NAME, "ctl00$cphMaster$txtContrasena").send_keys(contrasena)

    def click_ok(self):
        self.driver.find_element(By.NAME, "ctl00$cphMaster$btnIniciar").click()

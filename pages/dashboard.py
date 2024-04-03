from selenium.webdriver.common.by import By


class Dashboard:
    def __init__(self, driver):
        self.driver = driver

    def obtener_nombre_menu(self):
        menu = self.driver.find_element(By.XPATH,
                                   "/html/body/form/center/table/tbody/tr[2]/td/div/div[11]/table/tbody/tr/td[1]/div/div/table/tbody/tr/td[2]/span/table/tbody/tr/td[2]")

        return menu.text

    def salir(self):
        enlace_salir = self.driver.find_element(By.LINK_TEXT, "[Salir Modo Seguro]")
        enlace_salir.click()

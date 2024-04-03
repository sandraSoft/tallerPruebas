from selenium import webdriver
from selenium.webdriver.common.by import By


def prueba_acceso_sia():
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
    print(etiqueta_nombre.text)
    enlace_salir = driver.find_element(By.LINK_TEXT, "Salir")
    enlace_salir.click()
    driver.quit()


if __name__ == '__main__':
    prueba_acceso_sia()

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestAvanzados(unittest.TestCase):

    def test_wait_select(self):
        driver = webdriver.Edge()

        driver.implicitly_wait(5)
        driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer")

        # wait = WebDriverWait(driver, 2)
        # wait.until(lambda d: driver.find_element(By.ID, "userSelect").is_displayed())

        selector_vista = Select(driver.find_element(By.ID, "userSelect"))
        selector_vista.select_by_visible_text("Harry Potter")

        boton = driver.find_element(By.CLASS_NAME, "btn-default")
        boton.click()

        nombre = driver.find_element(By.CSS_SELECTOR, ".fontBig")
        self.assertEqual("Harry Potter", nombre.text)
        driver.find_element(By.CSS_SELECTOR, ".logout").click()
        driver.quit()

    def test_javascript_wait(self):
        driver = webdriver.Edge()

        driver.implicitly_wait(5)
        driver.get("https://www.ecosia.org/")
        frase_busqueda = "Functional Testing"

        campo_busqueda = driver.find_element(By.NAME, "q")
        campo_busqueda.send_keys(frase_busqueda)
        driver.find_element(By.CLASS_NAME, "search-form__submit").click()

        enlace = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
        driver.execute_script("arguments[0].click()", enlace)
        # wait = WebDriverWait(driver, 2)
        # wait.until(lambda d: driver.find_element(By.ID, "userSelect").is_displayed())

        WebDriverWait(driver, 10).until(ec.title_contains("Wikipedia"))
        self.assertTrue("Wikipedia" in driver.title)

        driver.quit()

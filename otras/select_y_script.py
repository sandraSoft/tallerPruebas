import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class TestLoginSelect(unittest.TestCase):

    def test_select(self):
        driver = webdriver.Edge()

        #driver.implicitly_wait(5)
        driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer")

        wait = WebDriverWait(driver, 2)
        wait.until(lambda d: driver.find_element(By.ID, "userSelect").is_displayed())

        selector_vista = Select(driver.find_element(By.ID, "userSelect"))
        selector_vista.select_by_visible_text("Harry Potter")

    def test_javascript(self):
        driver = webdriver.Firefox()

        driver.implicitly_wait(5)
        driver.get("https://www.ecosia.org/")
        fraseBusqueda = "Functional Testing"

        campoBusqueda = driver.find_element(By.NAME, "q")
        campoBusqueda.send_keys(fraseBusqueda)
        driver.find_element(By.CLASS_NAME, "search-form__submit").click()

        enlace = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
        driver.execute_script("arguments[0].click()", enlace)
        self.assertTrue("Wikipedia" in driver.title)

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UkolovnikTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_pridani_ukolu(self):
        self.driver.get("ZDE DAT CESTU K HTML UKOLOVNIK.HTML")

        time.sleep(2)

        input_box = self.driver.find_element(By.ID,"ukol")
        button = self.driver.find_element(By.ID,"pridat")

        input_box.send_keys("Nakoupit")

        button.click()
        #
        # input_box = self.driver.find_element(By.ID, "ukol")
        # button = self.driver.find_element(By.ID, "pridat")
        #
        # input_box.send_keys("Nakoupit")
        #
        # button.click()
        # input_box = self.driver.find_element(By.ID, "ukol")
        # button = self.driver.find_element(By.ID, "pridat")
        #
        # input_box.send_keys("Nakoupit")
        #
        # button.click()
        # input_box = self.driver.find_element(By.ID, "ukol")
        # button = self.driver.find_element(By.ID, "pridat")
        #
        # input_box.send_keys("Nakoupit")
        #
        # button.click()
        # input_box = self.driver.find_element(By.ID, "ukol")
        # button = self.driver.find_element(By.ID, "pridat")
        #
        # input_box.send_keys("Nakoupit")
        #
        # button.click()

        time.sleep(2)

        items = self.driver.find_elements(By.CSS_SELECTOR,"#seznam li")

        self.assertEqual(len(items),1)
        self.assertIn("Nakoupit",items[0].text)

        delete_button = items[0].find_element(By.TAG_NAME,"button")
        delete_button.click()
        items_new = self.driver.find_elements(By.CSS_SELECTOR,"#seznam li")
        time.sleep(2)
        self.assertEqual(len(items_new),0)

    def tearDown(self):
        self.driver.quit()


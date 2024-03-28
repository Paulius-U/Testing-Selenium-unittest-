import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def test_registration1(self):
        self.driver.get("http://suninjuly.github.io/registration1.html")
        self.assertEqual(self.driver.title, "Registration")
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Paulius")
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Ulevičius")
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("paulius.ule@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

    def test_registration2(self):
        self.driver.get("http://suninjuly.github.io/registration2.html")
        self.assertEqual(self.driver.title, "Registration")
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Paulius")
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Ulevičius")
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("paulius.ule@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

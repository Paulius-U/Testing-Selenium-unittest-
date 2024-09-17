import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

@pytest.fixture(scope="class", autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

class TestRegistration:
    def test_registration1(self, driver):
        driver.get(link)        
        driver.find_element(By.CSS_SELECTOR, ".form-control.first").send_keys("Paulius")
        driver.find_element(By.CSS_SELECTOR, ".form-control.second").send_keys("Ulevičius")
        driver.find_element(By.CSS_SELECTOR, ".form-control.third").send_keys("paulius.ule@gmail.com")
        driver.find_element(By.CLASS_NAME, "btn-default").click()
        assert "Congratulations! You have successfully registered!" == format(driver.find_element(By.TAG_NAME, "h1").text)

class TestRegistration2:
    def test_registration2(self, driver):
        driver.get(link2)
        driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input").send_keys("Paulius")
        driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input").send_keys("paulius.ule@gmail.com")
        driver.find_element(By.CLASS_NAME, "btn-default").click()
        assert "Congratulations! You have successfully registered!" == format(driver.find_element(By.TAG_NAME, "h1").text)
        
        
class TestRegistration3:
    def test_registration3(self, driver):
        driver.get(link)        
        driver.find_element(By.CSS_SELECTOR, ".form-control.first").send_keys("Paulius")
        driver.find_element(By.CSS_SELECTOR, ".form-control.second").send_keys("Ulevičius")
        driver.find_element(By.CLASS_NAME, "btn-default")
        assert driver.find_element(By.TAG_NAME, "h1").is_displayed()

class TestRegistration4:
    def test_registration4(self, driver):
        driver.get(link)        
        driver.find_element(By.CSS_SELECTOR, ".form-control.first").send_keys("Paulius")
        driver.find_element(By.CSS_SELECTOR, ".form-control.second").send_keys("Ulevičius")
        driver.find_element(By.CLASS_NAME, "btn-default")
        assert "Congratulations! You have successfully registered!" == format(driver.find_element(By.TAG_NAME, "h1").text)
        
if __name__ == "__main__":
    pytest.main()
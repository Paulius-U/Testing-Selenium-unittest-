from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = "C:\\Program Files (x86)\\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path=PATH, options=options)

link = "http://suninjuly.github.io/simple_form_find_task.html"
driver.get(link)

name = driver.title
print("-------------------------------")
print("Name of webpage: ", name)

element = driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input")
element.send_keys("Paulius")
element = driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("Ulevičius")
element = driver.find_element(By.XPATH, "/html/body/div/form/div[3]/input").send_keys("Vilkaviškis")
element = driver.find_element(By.XPATH, '//*[@id="country"]').send_keys("Vilnius")
driver.find_element(By.XPATH, '//*[@id="submit_button"]').click()
# input("Press...")

alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
alert.accept()
driver.quit()

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

PATH = "C:\\Program Files (x86)\\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path=PATH, options=options)

link = "http://suninjuly.github.io/redirect_accept.html"
driver.get(link)

button = driver.find_element(By.CLASS_NAME, "btn-primary")
button.click()

driver.switch_to.window(driver.window_handles[1])

a = driver.find_element(By.ID, "input_value").get_attribute("innerHTML")
print(a)

a = int(a)

def calculate_function(x):
    result = math.log(abs(12 * math.sin(x)))
    return result

function_value = calculate_function(a)
print(function_value)

answer = driver.find_element(By.ID, "answer")
answer.send_keys(str(function_value))

button2 = driver.find_element(By.CLASS_NAME, "btn-primary")
button2.click()

alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
alert.accept()
driver.quit()
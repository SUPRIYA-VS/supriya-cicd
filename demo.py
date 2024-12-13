from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
chrome_driver = webdriver.Chrome()

#opening web  url
chrome_driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(2)

#print title
print("page title : ",chrome_driver.title)

#print url
print("page url : ",chrome_driver.current_url)

#enter input to name field
chrome_driver.find_element(By.NAME,"name").send_keys("supriya")
chrome_driver.find_element(By.NAME,"email").send_keys("supriya.v@unisys.com")
chrome_driver.find_element(By.ID,"exampleInputPassword1").send_keys("supriya36")
chrome_driver.find_element(By.ID,"exampleCheck1").click()
chrome_driver.find_element(By.ID,"exampleFormControlSelect1").click()
time.sleep(2)
dropdown = chrome_driver.find_element(By.ID,"exampleFormControlSelect1")
select = Select(dropdown)
select.select_by_index(1) 
time.sleep(2)
chrome_driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
time.sleep(2)
chrome_driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(2)
message = chrome_driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message, f"Expected success message to contain 'Success', but got: {message}"
time.sleep(5)

#saving screenshot
chrome_driver.save_screenshot("pagehome1.png")
print("current page screenshot saved")

#closing driver
chrome_driver.quit()
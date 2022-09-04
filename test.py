
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


print("sample test case started")  
driver = webdriver.Chrome("./driver/chromedriver.exe")

driver.maximize_window()

driver.get("https://www.youtube.com/")

driver.find_element(By.CSS_SELECTOR, '[name="search_query"]').send_keys("TWICE")
driver.find_element(By.CSS_SELECTOR, '[name="search_query"]').send_keys(Keys.ENTER)
# driver.find_element(By.ID, "thumbnail").click()

print(driver.title)


driver.close()

print("sample test case successfully completed")  
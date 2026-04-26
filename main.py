from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
query="transformer"
driver.get("https://www.amazon.in/s?k={query}transformers&crid=26URRF10IZDDE&sprefix=transformers%2Caps%2C450&ref=nb_sb_noss_1")
#assert "Python" in driver.title
elem = driver.find_element(By.CLASS_NAME, "puis-card-container")
print(elem.get_attribute("outerHTML"))
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
time.sleep(60) 
driver.close()

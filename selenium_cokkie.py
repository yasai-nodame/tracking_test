from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

options = Options()

driver = webdriver.Chrome(options=options)

print('driver:', driver)
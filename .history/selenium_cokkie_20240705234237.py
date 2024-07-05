from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

options = Options()
options.binary_location = r"D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"


driver = webdriver.Chrome(options=options)

# print('Current cokkies:', cokkies)
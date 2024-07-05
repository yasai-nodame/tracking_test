from selenium import webdriver

driver = webdriver.Chrome('"D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"')

driver.get('https://www.youtube.com/?app=desktop&hl=ja')

cokkies = driver.get_cookies()

print('Current cokkies:', cokkies)
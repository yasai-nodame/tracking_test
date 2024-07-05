from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.youtube.com/?app=desktop&hl=ja')

cokkies = driver.get_cookies()

print('Current cokkies:', cokkies)
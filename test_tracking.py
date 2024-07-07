import requests 

url = 'https://www.youtube.com/?app=desktop&hl=ja'

session = requests.session()
response = session.get(url)

cokkie = response.cookies

print(cokkie)
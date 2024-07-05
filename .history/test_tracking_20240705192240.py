import requests 

url = 'https://www.youtube.com/?app=desktop&hl=ja'

response = requests.get(url)

print(response)
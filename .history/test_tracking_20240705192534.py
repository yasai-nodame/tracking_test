import requests 

url = 'https://www.youtube.com/?app=desktop&hl=ja'

response = requests.get(url)

for key, value in response.headers.items():
    print('key:',key)
    print('value:', value)
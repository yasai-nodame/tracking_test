import requests 

url = 'https://www.youtube.com/?app=desktop&hl=ja'

response = requests.get(url)

cookies = response.cookies

print('cookies:', cookies)

next_requests = requests.get(url, cookies=cookies)

print('next_requests.requests.header:', next_requests.request.headers)
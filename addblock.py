import requests 
from urllib.parse import urlparse 

blocked_domains = ['www.youtube.com']

def should_block(url):
    parse_url = urlparse(url)
    domain = parse_url.netloc
    for blocked_domain in blocked_domains:
        if blocked_domain in domain:
            return True 
    return False


def make_request(url):
    if should_block(url):
        print(f'{url}へのリクエストをブロックしました。')
        return 
    response = requests.get(url)
    print(f'{url} からのレスポンス: {response.status_code}')


make_request('https://www.twitch.tv/')
make_request('https://www.youtube.com/?app=desktop&hl=ja')
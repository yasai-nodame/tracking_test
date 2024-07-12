from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from selenium_wire_block import webdriver 
from time import sleep

import random 

BLOCK_URLS = [
    'googleads.g.doubleclick.net/pagead/',
    'www.youtube.com/pagead/interaction',
    'https://www.google.com/pagead/lvz',
    'https://www.google.co.jp/pagead/lvz',
    'https://static.doubleclick.net/instream',
    'https://tpc.googlesyndication.com/soder',
    
]

# リクエストをインターセプトする
def interceptor(request):
    for block_url in BLOCK_URLS:
        if block_url in request.url:
            print(f'ブロッキングURL: {request.url}')
            request.abort()
        else:
            print(f'リクエストURL: {request.url}')
            

# ランダムなユーザーエージェントを取得する
def get_random_user_agent():
    user_agents = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/31.0.1650.18 Mobile/11B554a Safari/8536.25',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4',
        'Mozilla/5.0 (Linux; Android 4.2.1; M040 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; M351 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    ]
    return random.choice(user_agents)

service = Service(
    executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
)

options = Options()
options.add_argument(f'user-agent={get_random_user_agent()}')

# webdriverの作成
driver = webdriver.Chrome(service=service, options=options)
driver.request_interceptor = interceptor

driver.get('https://www.youtube.com/?app=desktop&hl=ja')

sleep(300)


# user_agentを消して、request_inseptorだけでブロックされるか試してみる。


# selenium_wireによって webdriverのinterceptorで広告をブロックできたが、ブロックというよりは err:net faild302みたいな
# おそらく、httpヘッダーにCORSがないため、同一オリジンじゃない広告を取得するのに失敗してる気がする。
# その理由が、リクエストされる前にinterceptorすることによって、エラーを引き起こしてるんじゃないかと推測してます。
# ここらへんは試していかないとわからない。
# まず試す
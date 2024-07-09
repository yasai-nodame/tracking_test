from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random
from time import sleep




# user_agent random設定
def get_random_user_agent():
    user_agent = [
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
    
    return  random.choice(user_agent)



# google chrome最新版でも可能になってる。 chromedriverのpathを指定。
service = Service(
    executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
)
options = Options()
options.add_argument('--headless')
options.add_argument(f'user-agent={get_random_user_agent()}')
options.add_argument('--load-extension=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4\\Extensions\\cfhdojbkjhnklbpkdaibdccddilifddb')

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.google.com/search?q=youtube&oq=&gs_lcrp=EgZjaHJvbWUqCQgAEEUYOxjCAzIJCAAQRRg7GMIDMgkIARBFGDsYwgMyCQgCEEUYOxjCAzIJCAMQRRg7GMIDMgkIBBBFGDsYwgMyCQgFEEUYOxjCAzIJCAYQRRg7GMIDMgkIBxBFGDsYwgPSAQoyNjk4ODFqMGoxqAIIsAIB&sourceid=chrome&ie=UTF-8')

cookies = driver.get_cookies()

print('cocokie 1回目:', cookies)

for cookie in cookies:
    if cookie.get('name'):
        session_id = cookie.get('value')
        print(f'session id: {session_id}')
        
driver.delete_all_cookies()

options_1 = Options()
options_1.add_argument(f'user-agent={get_random_user_agent()}')
options_1.add_argument('--load-extension=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4\\Extensions\\cfhdojbkjhnklbpkdaibdccddilifddb')

driver_1 = webdriver.Chrome(service=service, options=options_1)
cookes_second = driver_1.get_cookies() # delete_all_cookies()を行って 確認したら[]になっていた。つまりクッキー情報は、削除されてる。


print('cookies 2回目:', cookes_second)
print(f'user-agent:{get_random_user_agent()}')
sleep(60)






"""
    from selenium import webdriver

# ブラウザを起動
driver = webdriver.Chrome()

# ウェブサイトにアクセス
driver.get("https://example.com")

# クッキーの一覧を取得
cookies = driver.get_cookies()
print("Current cookies:", cookies)

# 不要なクッキーを削除する
for cookie in cookies:
    if 'persistent_cookie_id' in cookie['name']:
        driver.delete_cookie(cookie['name'])

# 新しいクッキーを設定する（必要に応じて）
driver.add_cookie({'name': 'new_cookie', 'value': 'value'})

# ブラウザを閉じる
driver.quit()

"""

# torネットワークデフォルトだと、youtubeの広告をブロックできない。
# cookie削除とランダムなuser_agentを追加しただけでは、youtubeの広告をブロックできない。
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# google chrome最新版でも可能になってる。 chromedriverのpathを指定。
service = Service(
    executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
)
options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.google.com/search?q=youtube&oq=&gs_lcrp=EgZjaHJvbWUqCQgAEEUYOxjCAzIJCAAQRRg7GMIDMgkIARBFGDsYwgMyCQgCEEUYOxjCAzIJCAMQRRg7GMIDMgkIBBBFGDsYwgMyCQgFEEUYOxjCAzIJCAYQRRg7GMIDMgkIBxBFGDsYwgPSAQoyNjk4ODFqMGoxqAIIsAIB&sourceid=chrome&ie=UTF-8')

cookies = driver.get_cookies()

print('cocokie 1回目:', cookies)

for cookie in cookies:
    if cookie.get('name'):
        session_id = cookie.get('value')
        print(f'session id: {session_id}')
        
driver.delete_all_cookies()

cookes_second = driver.get_cookies() # delete_all_cookies()を行って 確認したら[]になっていた。つまりクッキー情報は、削除されてる。

print('cookies 2回目:', cookes_second)








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
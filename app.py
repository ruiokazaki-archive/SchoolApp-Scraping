import requests
from bs4 import BeautifulSoup
import settings

print("urlを入力してください")
url = input()

id = settings.ID
pw = settings.PW

login_info = {
    "c": "login_2",
    "flg_auto": "1",
    "token_a": "",
    "id": id,
    "pw" : pw,
}

# セッションスタート
session = requests.session()

# POSTでログインURLに送信
url_login = "https://comp-app.ecc-sv.com/app/index.php?c=login_1&token_a="

# 成功すればログイン先のページのHTMLが返却される
res = session.post(url_login, data=login_info)

# ほしいurlをgetする
geturl = session.get(url)

# htmlに変更
soup = BeautifulSoup(geturl.content, "html.parser")

for script in soup(["script", "style"]):
    script.decompose()

text = soup.get_text()

lines = [line.strip() for line in text.splitlines()]

text = "\n".join(line for line in lines if line)

# 表示する
print(text)

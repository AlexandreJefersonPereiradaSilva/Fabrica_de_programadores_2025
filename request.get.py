import requests, os, bs4
url = 'https://www.twitch.tv/' # url inicial
os.makedirs('bing', exist_ok=True)
while not url.endswith('#'):
    print(f"dowloando pajé {url}")
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
print(soup)


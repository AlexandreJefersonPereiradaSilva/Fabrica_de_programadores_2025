from bs4 import BeautifulSoup
import requests

url = 'https://youtube.com'
resposta = requests.get(url)
artube_clash = resposta.content

soup = BeautifulSoup(artube_clash, 'html.parser')

links =soup.find_all('p')
for link in links:
    print("texto: {%s}, URL: {%s}" % (link.text, link.get('href')))
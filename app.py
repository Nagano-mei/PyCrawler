import requests
from bs4 import BeautifulSoup

response = requests.get("https://bbs.hupu.com/bxj")
soup = BeautifulSoup(response.text, "html.parser")

lists = soup.select(".for-list")
for list_news in lists:
    print(list_news.select_one(".truetit").getText())
    print(list_news.select_one(".aulink").getText())